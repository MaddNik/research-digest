---
title: "Solving the Shortest Vector Problem in 2^(0.7314n+o(n)) Time via Discrete Gaussian Sampling on Superlattices"
date: 2026-08-07 08:05:00 +0200
categories: [PQC]
tags: [lattice, svp, cryptanalysis]
link: https://eprint.iacr.org/2026/1587
byline: "Yiming Gao, Yansong Feng, and Honggang Hu (IACR ePrint 2026/1587, Aug 3 2026)"
description: "A new classical randomized algorithm solves the exact shortest vector problem on full-rank lattices in time 2 to the power 0.7314n, improving on prior classical and quantum time bounds."
---

This paper presents a classical randomized algorithm for solving the exact Euclidean shortest vector problem (SVP) on full-rank lattices. The method constructs a random prime-index superlattice containing the original lattice, applies discrete Gaussian sampling over that superlattice, and then scans the sampled vectors to identify the shortest nonzero vector that also lies in the original lattice. According to the abstract, this approach achieves a running time of 2 to the power of approximately 0.73134 times n, plus a lower-order term, using space of 2 to the power of n over 2, plus a lower-order term. The authors state this improves upon prior classical and quantum time bounds for exact SVP solving. Since SVP hardness underlies the security estimates of lattice-based post-quantum schemes, algorithmic improvements of this kind are directly relevant to parameter selection and long-term security margins for those schemes.
