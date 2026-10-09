---
title: "Faster Provable Lattice Sieving with Spherical Codes"
date: 2026-10-09 08:16:00 +0200
categories: [PQC]
tags: [lattice-sieving, shortest-vector-problem, provable-security]
link: https://eprint.iacr.org/2026/2388
byline: "Divesh Aggarwal, Aditya Morolia, and Noah Stephens-Davidowitz (IACR ePrint 2026/2388, Oct 7 2026)"
description: "A new sieving algorithm with proven correctness for the approximate shortest vector problem closes much of the gap between the fastest proven and the fastest heuristic lattice-sieving running times."
---

The paper studies mu-SVP, the problem of finding a mu-approximate shortest non-zero vector in a lattice for constant approximation factors mu greater than 1, where prior to this work there was a large gap between the fastest algorithms with proven correctness and the fastest heuristic algorithms that work well in practice but lack proofs. The authors construct a sieving algorithm that combines the faster nearest-neighbor subroutines used in the fastest heuristic sieving algorithms with the perturbation argument used in algorithms with proven correctness, yielding a proven algorithm whose running time depends on the maximal size of certain spherical codes. Under a reasonable assumption about that maximal size, the algorithm's running time is roughly 2 to the power of 0.3066 times n for large constant mu, close to the best heuristic running time of about 2 to the power of 0.2925 times n, and much faster than the previous best proven algorithm at roughly 2 to the power of 0.802 times n. Using only the best proven upper bound on spherical code size, which the authors note is likely quite loose, they still obtain a proven running time of roughly 2 to the power of 0.6078 times n, substantially better than prior proven results though slower than a very recent concurrent algorithm that also handles mu equal to 1.
