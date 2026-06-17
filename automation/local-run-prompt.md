You are producing this week's "Frontier Research Digest" and publishing it to a
Jekyll/Chirpy GitHub Pages blog. You are running non-interactively (headless) in
the local git checkout at `/home/nik/research-digest`, which is already
authenticated to push to GitHub. Work entirely within this directory.

## 1. Sync the repo
Run `git pull --rebase` first so you are building on the latest state.

## 2. Research this week's notable papers
Cover these five topics. For each, find the most notable papers **posted or
published in the last 7 days**. If a topic genuinely has nothing new this week,
say so in that section rather than padding it.

1. **Photonics** — integrated/silicon photonics, photonic computing, optical interconnects, quantum photonics
2. **Post-Quantum Cryptography (PQC)** — lattice/code/hash/isogeny schemes, NIST standardization, implementations
3. **Fully Homomorphic Encryption (FHE)** — schemes, accelerators, libraries, applications
4. **Cryptography** — protocols, primitives, cryptanalysis, zero-knowledge, MPC
5. **Hardware security** — side-channel & fault attacks, secure/trusted hardware, TEEs, supply chain

Search these primary sources with WebSearch, and open the actual abstract pages
with WebFetch:
- arXiv recent listings/search: physics.optics, quant-ph, cs.CR
- IACR ePrint: https://eprint.iacr.org/ (recent feed) for PQC/FHE/crypto/hardware
- Venue announcements where relevant (TCHES/CHES, Eurocrypt, Crypto, Optica, Nature Photonics)

Aim for ~5–8 strong papers per topic. Prefer substance over volume; skip
incremental or off-topic results.

## 3. Verify every summary (mandatory)
For each paper you include:
1. Open the actual abstract/paper page (WebFetch the URL).
2. Write a 2–4 sentence summary grounded **only** in the abstract — no claims the
   source does not make, no hype.
3. Re-check that the title, authors, date, venue, and every factual claim in your
   summary match the source. If you cannot verify a paper or its link, **drop it.**
4. Use the canonical permanent link (arXiv `abs` page or ePrint page), not a PDF
   mirror or a search-result URL.

## 4. Write the post
Create `_posts/YYYY-MM-DD-frontier-digest-YYYY-MM-DD.md` using today's date.
Follow `automation/POST_TEMPLATE.md` exactly:
- YAML front matter: `title: "Frontier Digest — <Mon DD, YYYY>"`, `date: <today> 08:00:00 +0200`,
  `categories: [Digest]`, `tags: [photonics, pqc, fhe, cryptography, hardware-security]`.
- One `##` section per topic; each paper as `### [Title](url)`, then an italic
  byline `*Authors · Venue/arXiv id · date*`, then the verified summary.
- Keep the leading `.prompt-info` callout noting summaries are AI-generated and verified.
Use lowercase-hyphenated tags exactly as above.

## 5. Publish
```
git add _posts/
git commit -m "Frontier Digest — <today's date>"
git push origin main
```
The GitHub Actions workflow builds and deploys automatically on push — do **not**
build Jekyll yourself. After pushing, confirm with `git log -1 --oneline`, then
report: papers per topic, the post filename, and the commit hash. If the push
fails, retry once; if it still fails, print the exact error.
