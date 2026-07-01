# Research Tracker

A personal research feed at [MaddNik.github.io/research-digest](https://MaddNik.github.io/research-digest).

Papers, conference notes, and deep summaries — mainly cryptography, hardware security, and optical communications. Published weekly via a cron job that runs on Friday evenings.

## Structure

- `_posts/` — one post per paper, tagged by topic
- `summaries/` — deep summaries generated from source PDFs
- `_data/summaries.yml` — manifest of published summaries
- `automation/` — polling and publishing scripts (excluded from Jekyll build)

## Running locally

```
bundle install
bundle exec jekyll serve
```

Requires Ruby and Bundler. The site uses the [Chirpy](https://github.com/cotes2333/jekyll-theme-chirpy) theme.

## Deep summaries

Each paper card has a "Generate Deep Summary" button. Clicking it opens a pre-filled GitHub issue with the `summary-request` label. A poller (`automation/poll-and-summarize.sh`) runs on the WSL host, picks up new issues, generates a summary via Claude, and publishes it to `summaries/`.

To request a summary for a paper not yet in the tracker, open an issue manually with the `summary-request` label and fill in the source URL.

## Bookmarks

Bookmarks are stored in `localStorage` under the key `rt_lists`. Two lists: **Bookmarked** (gold) and **To-Read** (blue). The right panel and topbar dropdown reflect the current list state; the My Research page shows everything together.
