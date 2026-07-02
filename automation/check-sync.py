#!/usr/bin/env python3
"""Cross-platform consistency check for the research-digest repo.

Verifies that the published Deep Summaries stay internally consistent, which is
what keeps the site correct across the three places that touch this repo (the
cloud editor, the WSL machine, and GitHub):

  1. Every row in _data/summaries.yml has a matching summaries/<slug>/index.html
     (a manifest row without a page is a dead listing / broken modal).
  2. Every summaries/<slug>/index.html has a matching manifest row (a page
     without a row is an invisible orphan - this is what a mis-run publisher that
     dropped a manifest entry would leave behind).

Exit 0 when consistent, 1 on any drift. Prints a human-readable report.

Dependency-free and path-agnostic (repo root is derived from this file's
location), so it runs the same on the cloud container, WSL, and GitHub Actions.

Optional:
  --git   also `git fetch` and warn (not fail) if the checkout is behind
          origin/main. Intended for local/WSL use; skip it in CI.
"""
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(REPO, "_data", "summaries.yml")
SUMMARIES = os.path.join(REPO, "summaries")


def manifest_slugs(path):
    """Return the list of slugs declared in _data/summaries.yml (in file order)."""
    slugs = []
    try:
        text = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        return slugs
    for line in text.split("\n"):
        m = re.match(r'- slug:\s*"(.*)"\s*$', line)
        if m:
            slugs.append(m.group(1))
    return slugs


def folder_slugs(path):
    """Return the slugs of summaries/<slug>/ folders that contain an index.html."""
    out = []
    if not os.path.isdir(path):
        return out
    for name in sorted(os.listdir(path)):
        if os.path.isfile(os.path.join(path, name, "index.html")):
            out.append(name)
    return out


def git_behind_origin():
    """Return (behind, ahead) commit counts vs origin/main, or None if unavailable."""
    try:
        subprocess.run(["git", "-C", REPO, "fetch", "--quiet", "origin", "main"],
                       check=False, timeout=30)
        out = subprocess.check_output(
            ["git", "-C", REPO, "rev-list", "--left-right", "--count", "HEAD...origin/main"],
            text=True, timeout=30).strip().split()
        ahead, behind = int(out[0]), int(out[1])
        return behind, ahead
    except Exception:
        return None


def main():
    m_slugs = manifest_slugs(MANIFEST)
    f_slugs = folder_slugs(SUMMARIES)
    m_set, f_set = set(m_slugs), set(f_slugs)

    rows_without_folder = sorted(m_set - f_set)
    folders_without_row = sorted(f_set - m_set)

    errors = []
    print("research-digest sync check")
    print("  manifest rows : %d (%s)" % (len(m_slugs), MANIFEST))
    print("  summary pages : %d (%s/)" % (len(f_slugs), SUMMARIES))

    if not m_slugs and os.path.isfile(MANIFEST):
        errors.append("manifest parsed to 0 entries but the file exists (parse/format problem)")

    if rows_without_folder:
        errors.append("%d manifest row(s) with no summaries/<slug>/index.html (broken listing):" % len(rows_without_folder))
        for s in rows_without_folder:
            errors.append("    - " + s)
    if folders_without_row:
        errors.append("%d summary page(s) with no manifest row (invisible orphan):" % len(folders_without_row))
        for s in folders_without_row:
            errors.append("    - " + s)

    if "--git" in sys.argv:
        gb = git_behind_origin()
        if gb is not None:
            behind, ahead = gb
            if behind:
                print("  WARNING: local checkout is %d commit(s) behind origin/main (pull to sync)" % behind)
            if ahead:
                print("  note: local checkout is %d commit(s) ahead of origin/main (unpushed)" % ahead)

    if errors:
        print("\nDRIFT DETECTED:")
        for e in errors:
            print("  " + e)
        print("\nFix: ensure each summaries/<slug>/ folder has a matching row in")
        print("_data/summaries.yml and vice versa, then commit and push.")
        return 1

    print("\nOK: manifest and summary pages are consistent (%d entries)." % len(m_slugs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
