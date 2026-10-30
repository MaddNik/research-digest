---
title: "Faster Matrix Multiplication Leads to Faster Lattice Sieving"
date: 2026-10-30 08:14:00 +0200
categories: [PQC]
tags: [lattice-sieving, matrix-multiplication, svp, cryptanalysis]
link: https://eprint.iacr.org/2026/2622
byline: "Yiming Gao and Honggang Hu (IACR ePrint 2026/2622, Oct 24 2026)"
description: "Building on a recent improved bound on the matrix multiplication exponent, this paper shows that heuristic lattice sieving can be sped up below the standard (3/2 to the n/2) running time whenever fast matrix multiplication is available."
---

Let omega denote the matrix multiplication exponent; a recent OpenAI result showed that omega is at most 9/4. This paper shows that, for any fixed positive number eta, if omega is at most 9/4 minus eta then there exists a positive constant delta depending on eta such that heuristic lattice sieving can be improved to (3/2 minus delta) to the (n/2+o(n)) running time under the spherical heuristic used in the BDGL sieving analysis. The authors show that with currently known matrix multiplication algorithms their method already yields subquadratic search time within BDGL buckets, directly linking progress in fast matrix multiplication to concrete speedups in the best known algorithms for solving the shortest vector problem that underlies lattice-based cryptography's security estimates.
