You are producing this week's batch of "Research Tracker" papers and
publishing them to a Jekyll/Chirpy GitHub Pages blog. You are running
non-interactively (headless) in the local git checkout at
`/home/nik/research-digest`, which is already authenticated to push to GitHub.
Work entirely within this directory.

Important style rules for everything you write: do NOT use em dashes, do NOT use
emojis, and spell out math symbols in prose (for example "O(n squared)",
"microseconds", "3.1 square mm").

## 1. Sync the repo
Run `git pull --rebase` first so you are building on the latest state.

## 2. Research this week's notable papers
Cover these five topics. For each, find the most notable papers posted or
published in the last 7 days. If a topic genuinely has nothing new this week,
skip it rather than padding.

1. Photonics: integrated and silicon photonics, photonic computing, optical interconnects, quantum photonics
2. Post-Quantum Cryptography (PQC): lattice, code, hash, isogeny schemes, NIST standardization, implementations
3. Fully Homomorphic Encryption (FHE): schemes, accelerators, libraries, applications
4. Cryptography: protocols, primitives, cryptanalysis, zero-knowledge, MPC
5. Hardware security: side-channel and fault attacks, secure and trusted hardware, TEEs, supply chain

Search these primary sources with WebSearch, and open the actual abstract pages
with WebFetch:
- arXiv recent listings and search: physics.optics, quant-ph, cs.CR
- IACR ePrint: https://eprint.iacr.org/ (recent feed) for PQC, FHE, crypto, hardware
- Venue announcements where relevant (TCHES/CHES, Eurocrypt, Crypto, Optica, Nature Photonics)

Aim for about 5 to 8 strong papers per topic. Prefer substance over volume; skip
incremental or off-topic results.

## 3. Verify every summary (mandatory)
For each paper you include:
1. Open the actual abstract or paper page (WebFetch the URL).
2. Write the summaries grounded only in the abstract. No claims the source does
   not make, no hype.
3. Confirm that the title, authors, date, venue, and every factual claim match
   the source. If you cannot verify a paper or its link, drop it.
4. Use the canonical permanent link (arXiv `abs` page or ePrint page), not a PDF
   mirror or a search-result URL.

## 4. Write one post PER PAPER
For each verified paper, create a separate file
`_posts/YYYY-MM-DD-<short-slug>.md` using today's date and a short hyphenated
slug from the title. Follow `automation/POST_TEMPLATE.md` exactly:
- `categories` is exactly ONE canonical topic: `Photonics`, `PQC`, `FHE`,
  `Cryptography`, or `Hardware Security`.
- `tags` are 2 to 4 paper-specific lowercase hyphenated keywords (not the topic name).
- For FHE papers, also add sub-section tags so they appear under the FHE page filters:
  add `tfhe` if the paper is about TFHE (torus FHE, CGGI, programmable bootstrapping);
  add `fhe-fpga` if it is an FPGA implementation or FPGA acceleration of any FHE scheme;
  add both if it is a TFHE implementation on FPGA.
- `description` is a one-sentence SHORT summary (shown on the card).
- The body is the LONGER summary, 4 to 6 sentences (shown in the popup).
- `byline` and `link` as in the template.
- Stagger the `date` minutes (08:01, 08:02, ...) so ordering is stable.
Do not create a single combined digest post; one file per paper only.

## 5. Publish
```
git add _posts/
git commit -m "Research Tracker papers, <today's date>"
git push origin main
```
The GitHub Actions workflow builds and deploys automatically on push. Do not
build Jekyll yourself. After pushing, confirm with `git log -1 --oneline`, then
report: the number of papers per topic, the new post filenames, and the commit
hash. If the push fails, retry once; if it still fails, print the exact error.
