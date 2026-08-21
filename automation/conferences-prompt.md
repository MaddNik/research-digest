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
an emphasis on Europe where relevant.

There is no web-search tool available. Start from this fixed seed list of
official homepages (fetch each with `fetch_url`, mode text) and follow the
links on each page to find the current or next edition's dates, location, and
program:
- Semiconductor / FPGA / EDA / circuits:
  FPL: https://fpl.org/
  ACM/SIGDA FPGA: https://www.isfpga.org/
  DATE: https://www.date-conference.com/
  DAC: https://dac.com/
  ISSCC: https://www.isscc.org/
  ESSERC (successor to ESSCIRC/ESSDERC, merged 2024): https://www.esserc2026.org/
    (this one rotates to a year-numbered domain each edition; if that URL is
    stale, fetch https://www.esserc2026.org/ anyway and follow any "next
    edition" link, or fall back to searching IEEE CEDA's event listing if you
    have another verified URL for it)
  CICC: https://www.ieee-cicc.org/
  VLSI Symposium: https://www.vlsisymposium.org/
  Hot Chips: https://hotchips.org/
  ICCAD: https://iccad.com/
- Photonics:
  OFC: https://www.ofcconference.org/
  ECOC: https://www.ecocexhibition.com/
  CLEO: https://cleoconference.org/
  SPIE Photonics West: https://spie.org/conferences-and-exhibitions/photonics-west
  IEEE Photonics Conference (IPC): https://ieee-ipc.org/
  Integrated Photonics Research (IPR, part of Optica's Advanced Photonics
    Congress): https://www.optica.org/events/congress/advanced_photonics_congress/

These homepages sometimes redirect or link to a year-specific subdomain (e.g.
`2026.fpl.org`) for the current edition; follow those links with another
`fetch_url` call rather than guessing the year-numbered URL yourself. Include
any other conference you're confident fits "semiconductor and/or photonics"
and look significant, fetched from a URL you already have (not searched for).
Aim for roughly 8 to 15 upcoming entries. Drop any conference you cannot
verify from the fetched page content.

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
