---
title: "Discrete Gaussian Sampling Meets BDGL Decoding: Solving the Shortest Vector Problem in $2^{0.5596n+o(n)}$ Time"
date: 2026-09-04 08:08:00 +0200
categories: [PQC]
tags: [shortest-vector-problem, lattice-cryptanalysis, discrete-gaussian-sampling, sieving]
link: https://eprint.iacr.org/2026/1844
byline: "Yiming Gao et al. (IACR ePrint 2026/1844, Aug 31 2026)"
description: "A new randomized classical algorithm combines random-superlattice discrete Gaussian sampling with a BDGL product-code decoding layer to solve the exact shortest vector problem in 2 to the 0.5596n time."
---

The Aggarwal-Dadush-Regev-Stephens-Davidowitz algorithm solves the shortest vector problem in lattices in 2 to the n time using discrete Gaussian sampling, and a later variant by Gao, Feng, and Hu made this sampler available at the shortest-vector scale for a 2 to the 0.7314n time algorithm, while the separate BDGL sieve uses spherical product codes to run in 2 to the 0.2925n time under a random-list heuristic. This paper combines the random-superlattice discrete Gaussian sampling framework with a single BDGL product-code decoding layer, splitting the sampler output into two lists and using a Gaussian midpoint identity to turn the search for a fixed shortest vector into a birthday-style event that the product-code decoder can locate directly rather than by enumerating all pairwise differences. The analysis makes no random-list assumption, and by replacing a centered quotient line with a random affine translate that targets a rarer midpoint shell, the authors obtain a randomized classical algorithm for the shortest vector problem running in 2 to the 0.5596n time using 2 to the n over 2 space. Faster classical shortest-vector algorithms feed directly into concrete security estimates for lattice-based post-quantum schemes.
