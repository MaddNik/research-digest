# Weekly Frontier Digest — autonomous run prompt

This is the prompt executed by the scheduled cloud agent every Friday. It is
fully self-contained (no dependency on any prior conversation). The real GitHub
username, repo, and a Personal Access Token are substituted in when the cloud
routine is created — **this committed copy intentionally keeps placeholders so
no secret is stored in the repository.**

---

You are producing this week's "Frontier Research Digest" — a curated roundup of
new research papers, published as a post on a Jekyll/Chirpy GitHub Pages blog.

## 1. Set up the repository

Clone the blog repo into a working directory and configure git identity:

```bash
git clone https://__GH_USERNAME__:__GH_PAT__@github.com/__GH_USERNAME__/__REPO__.git digest && cd digest
git config user.name "Frontier Digest Bot"
git config user.email "nikshipth@akhetonics.com"
```

## 2. Research — find this week's notable papers

Cover these five topics. For each, find the most notable papers published or
posted in the **last 7 days** (if a topic genuinely has nothing new this week,
say so rather than padding):

1. **Photonics** — integrated/silicon photonics, photonic computing, optical interconnects, quantum photonics
2. **Post-Quantum Cryptography (PQC)** — lattice/code/hash/isogeny schemes, NIST standardization, implementations
3. **Fully Homomorphic Encryption (FHE)** — schemes, accelerators, libraries, applications
4. **Cryptography** — protocols, primitives, cryptanalysis, zero-knowledge, MPC
5. **Hardware security** — side-channel & fault attacks, secure/trusted hardware, TEEs, supply-chain

Primary sources to search (use web search + fetch the actual abstract pages):
- **arXiv** listings/search — e.g. `https://arxiv.org/list/physics.optics/recent`, `cs.CR`, `quant-ph`; and `https://arxiv.org/a/` search by date.
- **IACR ePrint** — `https://eprint.iacr.org/` (recent papers feed) for PQC/FHE/crypto/hardware.
- Conference / journal announcements where relevant (CHES/TCHES, Eurocrypt, Crypto, Optica, Nature Photonics).

Aim for roughly **5–8 strong papers per topic** (Deep coverage). Prefer
substance over volume — skip incremental or off-topic results.

## 3. Verify every summary (this is mandatory)

For each paper you include:
1. Fetch the actual abstract / paper page at the URL.
2. Write a 2–4 sentence summary **grounded only in the abstract** — no claims the
   source doesn't make, no hype.
3. Re-read the abstract and confirm the title, authors, date, venue, and every
   factual claim in your summary match the source. If you cannot verify a paper
   or its link, **drop it** — do not guess.
4. Use the canonical permanent link (arXiv abs page or ePrint page), not a PDF
   mirror or a search-result URL.

## 4. Write the post

Create `_posts/YYYY-MM-DD-frontier-digest-YYYY-MM-DD.md` (today's date, Friday).
Follow the structure in `automation/POST_TEMPLATE.md` exactly:
- YAML front matter with `title`, `date` (today, 08:00:00 +0200), `categories: [Digest]`, and topic `tags`.
- One `##` section per topic, each paper as `### [Title](url)` followed by an
  italic byline (`*Authors · Venue/arXiv id · date*`) and the verified summary.
- Keep the leading `.prompt-info` callout noting summaries are AI-generated and verified.

Use lowercase-hyphenated tags: `photonics`, `pqc`, `fhe`, `cryptography`, `hardware-security`.

## 5. Publish

```bash
git add _posts/
git commit -m "Frontier Digest — YYYY-MM-DD"
git push origin HEAD
```

The repo's GitHub Actions workflow (`.github/workflows/pages-deploy.yml`) builds
and deploys the site automatically on push — you do **not** need to build Jekyll
yourself. After pushing, confirm the commit landed (`git log -1`), then report:
the number of papers per topic, the post filename, and the commit hash.

If the push fails (auth/network), retry once; if it still fails, report the exact
error so the token or repo settings can be fixed.
