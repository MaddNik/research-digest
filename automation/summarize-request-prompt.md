You are running non-interactively (headless) in /home/nik/research-digest, which
is authenticated to push to GitHub. Style rules: no em dashes, no emojis, recreate
all mathematics as proper LaTeX, put all code/pseudocode in code blocks.

Task: produce ONE summary for a single source using the summarize-anything skill,
then exit. Do NOT commit or push anything yourself.

- Source URL: ${SRC}
- Requested level: ${LEVEL}
- Site category (one of Photonics, PQC, FHE, Cryptography, Hardware Security, Other): ${CAT}

Steps:
1. Invoke the summarize-anything skill on the Source URL above at level ${LEVEL}.
   Follow its SKILL.md formatting rules (LaTeX equations, code blocks, the mandatory
   Algorithms appendix, completeness, publisher and source_url fields).
2. Storage: summaries live under ~/research-material/<topical-category>/<slug>-<date>/.
   Choose the <topical-category> folder by TOPIC, not by the site category. Map the
   site category to a topical kebab-case folder, reusing an existing one only if the
   source clearly belongs there:
   - FHE -> an existing fhe* / tfhe* folder if it clearly fits, else a new descriptive folder.
   - Photonics -> a photonics-* folder.
   - PQC or Cryptography -> a pqc-* or crypto-* folder.
   - Hardware Security -> a hardware-security-* folder.
   Per the skill rules, in headless mode, if the best-fitting existing folder already
   holds other material, create a NEW dedicated folder rather than merging into it.
3. Ground the summary only in the source; verify the title, authors, and venue. Set
   source_url in content.json to the canonical Source URL so the publisher links it.
4. Do NOT commit or push. When finished, exit. The Stop hook publishes and pushes
   automatically.
5. Report the saved path and the chosen category folder.
