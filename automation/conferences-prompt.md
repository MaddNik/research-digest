You maintain the Conferences list for a personal research-tracking site
(Jekyll/Chirpy on GitHub Pages). You are running non-interactively (headless) in
the local git checkout at `/home/nik/research-digest`, which is already
authenticated to push to GitHub. Work entirely within this directory.

Style rules: do NOT use em dashes, do NOT use emojis.

## 1. Sync the repo
Run `git pull --rebase` first.

## 2. Research upcoming conferences
Find notable UPCOMING conferences (events whose dates are in the future relative
to today) in the semiconductor and/or photonics domains. Cover both areas, with
an emphasis on Europe where relevant, for example:
- Semiconductor / FPGA / EDA / circuits: FPL, ACM/SIGDA FPGA, DATE, DAC, ISSCC,
  ESSERC (ESSCIRC), CICC, VLSI Symposium, Hot Chips, ICCAD.
- Photonics: OFC, ECOC, CLEO, SPIE Photonics West, IEEE Photonics Conference,
  Integrated Photonics Research.
Include any others you find that fit "semiconductor and/or photonics" and look
significant. Aim for roughly 8 to 15 upcoming entries.

For each, use WebSearch and open the official conference site with WebFetch to
confirm the details. Drop any conference you cannot verify.

## 3. Write the data file
Overwrite `_data/conferences.yml` with the verified upcoming list. Use exactly
this shape, one entry per conference:

```yaml
- name: "<full name, with acronym>"
  domain: <Semiconductor | Photonics>
  continent: <Europe | North America | Asia | South America | Africa | Oceania | Online>
  location: "<City, Country>"
  dates: "<human readable dates, for example September 1 to 4, 2026>"
  start: <YYYY-MM-DD start date, for sorting>
  about: "<one or two sentences on what the conference is about>"
  url: "<official conference URL, or empty string if none found>"
  submission: "<paper submission deadline, human readable, or omit if unknown>"
  earlybird: "<early-bird registration deadline, human readable, or omit if unknown>"
  late_deadline: "<late / regular / on-site registration deadline, or omit if unknown>"
  speakers:
    - "<Name (role, affiliation) - talk title, e.g. Jane Doe (Keynote, MIT) - Photonic computing>"
    - "<another confirmed keynote / invited / panel speaker>"
  panel: "<one short sentence on the panel or program highlights, or omit if unknown>"
```

Rules:
- Only include conferences whose `start` date is in the future.
- `start` must be a valid YYYY-MM-DD date (used for sorting on the page).
- `continent` is the continent of the host city (the page groups conferences by it).
  Use "Online" only for fully virtual events.
- Prefer the official site for `url`; if you cannot find a reliable one, set `url: ""`.
- `submission`, `earlybird`, `late_deadline`, `speakers`, and `panel` are OPTIONAL.
  Include a field only if you can VERIFY it from the official site or program; OMIT the
  field entirely (do not write an empty value or a guess) when the information is not
  available or not yet announced. These render in a collapsible "Panel & speakers"
  sub-menu and a deadlines line, so only add them when they are real and relevant.
- `speakers` is a list of confirmed keynote / invited / panel speakers (a few of the
  most notable is enough); omit the whole list if none are announced yet.
- Keep the explanatory comment lines at the top of the file.
- No em dashes, no emojis.

## 4. Publish
```
git add _data/conferences.yml
git commit -m "Update conferences, <today's date>"
git push origin main
```
The GitHub Actions workflow builds and deploys automatically on push. After
pushing, confirm with `git log -1 --oneline`, then report the number of
conferences listed and the commit hash. If the push fails, retry once; if it
still fails, print the exact error.
