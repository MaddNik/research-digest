# Per-paper post format

Each paper is published as its OWN post file in `_posts/`, named
`_posts/YYYY-MM-DD-<short-slug>.md` (today's date, a short hyphenated slug from
the title). Front matter and body follow this shape exactly:

```
---
title: "<exact paper title>"
date: YYYY-MM-DD HH:MM:00 +0200
categories: [<ONE topic>]
tags: [<2 to 4 paper-specific keywords>]
link: <canonical article URL>
byline: "<First Author et al. (arXiv:XXXX or IACR ePrint 20XX/NNN, Mon DD YYYY)>"
description: "<one short sentence summarizing the paper, shown on the card>"
---

<A longer summary, 4 to 6 sentences, grounded only in the abstract. This is shown
in the popup. No hype, no claims the source does not make.>
```

Rules:
- `categories` must be exactly ONE of these canonical values (this drives the
  per-topic pages): `Photonics`, `PQC`, `FHE`, `Cryptography`, `Hardware Security`.
- `tags` are specific to the paper (for example `lattice`, `silicon-photonics`,
  `side-channel`), lowercase and hyphenated. Do NOT use the broad topic name as a tag.
- `description` is the SHORT summary (one sentence). The body is the LONG summary.
- Give papers in the same run staggered minutes in `date` (08:01, 08:02, ...) so
  ordering is stable.
- Do NOT use em dashes anywhere. Do NOT use emojis anywhere.
- Spell out math symbols in prose (write "O(n squared)", "3.1 square mm",
  "microseconds") so the cards and feed render cleanly.
```
