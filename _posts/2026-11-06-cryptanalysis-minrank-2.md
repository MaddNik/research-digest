---
title: "Cryptanalysis of MinRank 2.0"
date: 2026-11-06 08:11:00 +0200
categories: [PQC]
tags: [minrank, multivariate-cryptography, cryptanalysis, mayo]
link: https://eprint.iacr.org/2026/2733
byline: "Nicolas Aragon et al. (IACR ePrint 2026/2733, Nov 3 2026)"
description: "A revisited attack on the MinRank problem underlying several NIST post-quantum candidates solves a 25-year-old open challenge and corrects prior complexity estimates."
---

MinRank is an NP-complete problem underlying several post-quantum schemes, including the NIST second-round signature candidate Mirath and the multivariate signature candidates UOV, MAYO, QR-UOV, and SNOVA. This paper revisits combinatorial and algebraic attacks on MinRank, improving the kernel-search attack by sharing its linear algebra computation across guesses, lowering its cost by 3 to 6 bits on Mirath parameters and the Courtois MinRank challenges. Using the improved attack, the authors solve Courtois challenge D, open since 2001, an instance over the binary field with 19 by 19 matrices, 81 unknowns, and target rank 10, requiring about 11,434 CPU days and an estimated bit-operation count of 2 to the 61st power. On the algebraic side, they show that the Kipnis-Shamir attack's complexity is less understood than previously believed, since existing estimates rely on a generic Hilbert series that does not correctly predict the rank of the relevant Macaulay matrices, leading to corrected complexity estimates that are 1 to 24 bits higher than the best other attack on every Mirath parameter set. They also extend the Support-Minors and Minors modeling approaches with field equations, substantially lowering complexity estimates over small fields.
