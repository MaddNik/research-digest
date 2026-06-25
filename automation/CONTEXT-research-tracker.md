# Compact Summary — Research Tracker session

> Compacted context from the long-running "research-tracker" Claude Code session
> (cwd `/home/nik/research-material`, repo `MaddNik/research-digest`).

## 1. Primary Request and Intent

Building a **personal research-tracking website** on GitHub Pages. Original ask: a cron job that weekly (Fridays) scrubs the internet for research papers on **Photonics, PQC, FHE, cryptography, and hardware security**, producing a blog-format report with titles, short summaries, and source hyperlinks.

Evolved into a full personal research dashboard. Cumulative requirements:
- Per-topic category pages; one post per paper; per-paper tags (show topic/subheading, not hashtags).
- Click-to-popup **modal** for long summaries, linking to source.
- **Conferences** tracker (monthly), grouped by continent (location, focus, dates, link).
- Renamed **"Research Tracker"** (personal site, not a "digest").
- Homepage: compact **category tile filter** (client-side), latest run only.
- **TFHE sub-sections** on FHE page: TFHE, FPGA implementations, TFHE-on-FPGA intersection, curated resources.
- **Bookmarks**: "To read" + "Saved" in localStorage; "My Research" area; right-panel lists; two tight top-bar icons by search box.
- **Summaries section**: publish summarize-anything HTML docs from `~/research-material/` automatically (auto-commit), each linking to source; same TFHE/FPGA filter tiles.
- Tags page = collapsible tile sections by domain; Categories page removed; sectioned sidebar nav (TOPICS / BROWSE / ABOUT).

**Standing constraints (non-negotiable):** No em dashes anywhere. No emojis on the site. Properly formatted **LaTeX equations** ("no more n^2 or m_1^x"). Code/pseudocode in code blocks.

**Admin:** GitHub PAT (`ghp_Qf8...`) was pasted in plaintext — rotate it.

## 2. Key Technical Concepts

- **Jekyll + Chirpy v7.5.0**, deployed via **GitHub Actions** (`.github/workflows/pages-deploy.yml` includes htmlproofer "Test site"). No local Ruby/Jekyll; validate by pushing + polling the Actions run via GitHub API.
- **Headless automation:** `claude -p --dangerously-skip-permissions` via local **cron** on WSL (systemd active).
- **Git auth:** `credential.helper store` → `~/.git-credentials`; classic PAT with **`repo` + `workflow`** scopes (`~/.gh_pat`).
- Chirpy customized via forked includes/layouts (override theme files by same name).
- **localStorage** features: bookmark lists (key `rt_lists` with `saved`/`toread`), tag filtering, modal popups.
- **summarize-anything skill:** `python3 -m scripts.cli {probe|detect|parse-pdf|build-html}` from `/home/nik/.claude/skills/summarize-anything`; outputs `summary.html`, `content.json`, `assets/`, `source.pdf` under `~/research-material/<category>/<slug>-<date>/`. `content.json`: `title, source_type, level, verified, tags, sections[]` (section = `heading, body_html, figures[]`).
- **MathJax 3** (jsdelivr CDN) injected at publish time for LaTeX.
- **htmlproofer** flags: `--disable-external --ignore-files "/summaries/"`; `<a>` without `href` = "missing reference" (keep `href="#"`).
- **IACR ePrint blocks bots** (Cloudflare 403); fetch PDFs via Wayback `web.archive.org/.../id_/...` or open-access mirrors (Springer, Semantic Scholar).
- **python3 only** (no `python` alias); PyMuPDF (`fitz`) + Pillow installed.

**CRITICAL BUG:** Chirpy HTML compression collapses inline `<script>` to one line, so `//` line comments swallow the rest. **Never use `//` line comments in inline scripts** (use `/* */`). Static files under `summaries/` have no front matter and are NOT minified.

## 3. Files and Resources

**Repo / hosting**
- Repo `MaddNik/research-digest` (public). Working dir `/home/nik/research-digest`. Live: https://maddnik.github.io/research-digest/ (baseurl `/research-digest`).
- `_config.yml` — title "Research Tracker", `avatar: /assets/img/logo.png`, `exclude` includes `automation/`.
- `.github/workflows/pages-deploy.yml` — build + htmlproofer (`--ignore-files "/summaries/"`) + deploy.

**Layouts (`_layouts/`)**: `home.html`, `topic.html`, `fhe.html`, `conferences.html`, `tags.html`, `summaries.html`, `my-research.html`, `page.html` (prefers `page.heading`), `paper.html`, `default.html`.

**Includes (`_includes/`)**: `paper-cards.html`, `paper-modal.html` (shared style + modal JS), `resource-cards.html`, `recommended-papers.html`, `conferences-panel.html`, `research-panel.html`, `sidebar.html` (sectioned nav via `group:`), `topbar.html` (tight To-read/Saved icons), `bookmarks-js.html`.

**Data (`_data/`)**: `topics.yml` (category order + full names), `conferences.yml`, `tfhe_resources.yml` (TFHE-on-FPGA = entries tagged both `tfhe`+`fhe-fpga`: MATCHA arXiv 2202.08814, FPT 2211.13696, parameterizable TFHE processor 2510.23483), `summaries.yml` (generated manifest, 16 summaries: slug/title/url/date/pub/source_type/source_url/pdf/tags).

**Automation (`automation/`)**: `run-weekly.sh` + `local-run-prompt.md`; `run-conferences.sh` + `conferences-prompt.md`; `publish-summaries.py` (walks `~/research-material`, copies summaries to `summaries/<slug>/`, parses source URL + date, builds manifest, post-processes each `index.html` via `inject()`: sticky back-bar, "Full text" link, figure lightbox, "Figure N" labels, MathJax); `sync-summaries.sh` (publisher + git push, wired as global Stop hook in `~/.claude/settings.json`).

**Tabs (`_tabs/`)**: photonics, pqc, fhe, cryptography, hardware-security (TOPICS); conferences, summaries, tags, archives (BROWSE); about (ABOUT). Categories removed from nav (non-nav `categories.md` kept for breadcrumbs).

**Other**: `assets/img/logo.png` (namemc Minecraft face); `~/research-material/` 16 summary dirs across `tfhe-foundations`, `tfhe-fpga-accelerators`, `fhe-fpga-accelerators`, `fhe-surveys`, `boolean-fhe-tfhe-rtl` (all retain `source.pdf`). Memory: `research-digest-automation.md`, `no-emdashes.md`.

**Cron:** `0 12 * * 5 run-weekly.sh` (papers, Fri noon); `13 9 1 * * run-conferences.sh` (conferences, 1st of month).

## 4. Decisions and Conventions

- One post per paper (topic = Chirpy category; tags = keywords). Modal popups for long summaries; newest-first home grouped/filtered by category.
- Cards show a topic chip (transparent bg, thin border), muted short summary, explicit `--heading-color` titles (because `#post-list` scope was removed to avoid duplicate IDs).
- Local cron over cloud (cloud routine needs `environment_id`/Claude GitHub app the assistant can't provision). Cloud (Option A: GitHub Actions + `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token`) explored, not implemented.
- Summaries: source PDFs not committed when source URL parsed; em dashes stripped; tags carried to manifest; algorithms/pseudocode verbatim in `<pre><code>`.
- Auto-publish via global Stop hook. Validate every change by pushing + polling the Actions run.

## 5. Errors and Fixes

- Push rejected (no `workflow` scope) → user added scope.
- Pages build failed at "Setup Pages" → enabled via API `POST /pages {"build_type":"workflow"}`.
- htmlproofer "'a' missing reference" → restored `href="#"` on modal link.
- Breadcrumbs after removing Categories tab → kept non-nav `categories.md`.
- FHE filter dead → `//` comment swallowed in minified inline script; removed. (No-`//` rule.)
- ePrint 403 (GSW/FHEW, no Wayback) → fetched from Springer open-access / content mirror.
- Low-contrast titles → set `--heading-color`. Dark-mode white card box → set `--card-bg`. " | Research Tracker" tab title → renamed home layout to `home`. Slow builds → extended poll windows.

## 6. Current State (working & live)

- Live, auto-deploying on push; both cron jobs installed.
- Homepage category tile filter; 5 topic pages; conferences by continent; collapsible Tags page; sectioned sidebar; Categories removed.
- Personal lists (To-read + Saved) in localStorage, top-bar icons, right panel, My Research page.
- FHE sub-filter (TFHE / FPGA implementations / TFHE-on-FPGA) + curated resources.
- **16 summaries published**, each its own page with figures + algorithms, filterable by tag, modal popup. Auto-publish Stop hook works.

## 7. Most Recent Work & Pending  (== the current task)

Last user prompt: information still cut off from pre-existing summaries, plus:
1. **Equation preview/popover** wherever an equation is referenced inline in a summary (like the figure hover-preview, but for equations).
2. Fix meta line `"PDF (text-layer), arXiv:2202.08814 · full view"`: **"full view"** hyperlinks to the article in a **new tab**; replace **"PDF (text-layer…)"** with the **publisher**.
3. Add a **"Concepts" tag/section** for supporting knowledge (NTT, multiplication-less integer FFT/iFFT) and seed more supporting concepts.
4. **Equations recreated properly** (LaTeX) — non-negotiable.
5. **Code/pseudocode in code blocks**.

**WIP at break (uncommitted):** editing `automation/publish-summaries.py` (equation-preview CSS/JS in `ENHANCE_HEAD`/`ENHANCE_TAIL`, MathJax `pageReady` hook, computed `publisher` + `meta_line` in manifest) and `_layouts/summaries.html` (card meta uses publisher line, "Full view" → source in new tab, added "Concepts" filter tile). Python parses OK.

**Pending (regenerate-all approved earlier):** regenerate all 16 summaries with generous figure crops (no cut labels/captions), sequential `assets/figN.png` referenced as "Figure N", LaTeX equations, pseudocode in `<pre><code>`, publisher info; preserve each `content.json` title/tags/source_type. (1 done: `mk-tfhe-multi-key-2026-06-24`.) Add Concepts tag + seed supporting-concept summaries. Then run `publish-summaries.py`, commit all, push, poll build, verify.

**Remaining 15 slugs:** tfhe-fast-fhe-over-torus, gsw-he-from-lwe, fhew-bootstrapping-under-a-second, first-tfhe-faster-bootstrapping, wop-pbs-larger-precision, pbs-dnn-inference, lmkcdey-fhew-small-eval-keys, tfhe-parameter-optimization, heax-architecture-encrypted-data, fab-fpga-accelerator-bootstrappable-fhe, sok-fhe-accelerators, matcha-accelerator-fhe-over-torus, fpt-fixed-point-accelerator-torus-fhe, parameterizable-tfhe-processor, strix-tfhe-accelerator.

**Outstanding:** rotate the exposed GitHub PAT.
