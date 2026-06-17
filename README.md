# Frontier Research Digest

An automatically curated weekly blog of new research papers in **photonics,
post-quantum cryptography (PQC), fully homomorphic encryption (FHE),
cryptography, and hardware security**. Built on the [Chirpy][chirpy] Jekyll theme
and hosted on GitHub Pages.

A scheduled cloud agent runs every **Friday**, researches the week's notable
papers, verifies each summary against its source, and pushes a new post here.
GitHub Actions then builds and deploys the site.

## One-time setup

### 1. Create the GitHub repo and push this site

```bash
# from inside this directory
git init -b main
git add -A
git commit -m "Initial site"

# Fill in your GitHub username, then create the repo and push.
# (Requires the GitHub CLI `gh`, or create the repo manually in the web UI.)
gh repo create research-digest --public --source=. --remote=origin --push
# --- OR manually: create an empty repo named "research-digest" on github.com, then:
# git remote add origin https://github.com/<USERNAME>/research-digest.git
# git push -u origin main
```

### 2. Set your GitHub username in the config

Replace the `__GH_USERNAME__` placeholders (one command):

```bash
sed -i 's/__GH_USERNAME__/<YOUR_USERNAME>/g' _config.yml
git commit -am "Set GitHub username" && git push
```

If you name the repo `research-digest`, the site lives at
`https://<username>.github.io/research-digest` (the default `baseurl` is already
`/research-digest`). If you instead name the repo `<username>.github.io`, set
`baseurl: ""` in `_config.yml`.

### 3. Enable GitHub Pages

Repo → **Settings → Pages → Build and deployment → Source = GitHub Actions**.
The included workflow (`.github/workflows/pages-deploy.yml`) builds on every push
to `main`. Watch the first run under the **Actions** tab.

### 4. The weekly agent

The weekly run is a local cron job (`crontab -l` shows it) that fires every
Friday and invokes `automation/run-weekly.sh`. That script runs the headless
Claude CLI with `automation/local-run-prompt.md`: research, verify against the
source, write one post per paper, commit, and push. Git auth uses the global
credential helper (`~/.git-credentials`), so no token is stored in the repo.

To run it on demand: `./automation/run-weekly.sh` (logs land in
`automation/logs/`).

## Local preview (optional)

Requires Ruby + Bundler:

```bash
bundle install
bundle exec jekyll s
```

## License

Site content: yours. Theme: [MIT][mit] ([Chirpy][chirpy]).

[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/
[mit]: ./LICENSE
