---
title: "Subexponential Algorithms for LWE via Rejection Sampling on Superlattices"
date: 2026-10-30 08:11:00 +0200
categories: [PQC]
tags: [lwe, lattice-cryptanalysis, rejection-sampling, subexponential-algorithms]
link: https://eprint.iacr.org/2026/2640
byline: "Ligeng Fan et al. (IACR ePrint 2026/2640, Oct 26 2026)"
description: "Two rejection-sampling refinements to the superlattice framework yield provably subexponential classical algorithms for search-LWE, resolving an open obstacle identified in prior work on extending superlattice techniques beyond short integer solution problems."
---

Recent superlattice algorithms improved the provable complexity of lattice problems, but extending the framework from the short integer solution problem to learning with errors (LWE) hit a key obstacle identified by Ducas, Engelberts, and Loyer, and a related gap existed in Kirchner and Fouque's claimed subexponential running time for LWE with few samples. This paper develops two refinements based on rejection sampling to close that gap. The first uses rejection sampling to cancel a shift-dependent normalization factor arising when sampling from a shifted, scaled integer lattice, giving a provably subexponential classical search-LWE algorithm for prime modulus between n squared and 2n squared and constant Gaussian error width, using only 4n samples and running in time and space exp(O(n divided by ln ln n)). The second applies rejection sampling to the difference of two Gaussian lattice samples drawn from random auxiliary superlattices, yielding an algorithm with time and space 2 to the (1/2+o(1))n/ln R for appropriate parameter regimes, which the authors show is provably subexponential for polynomially bounded error width and any fixed ratio of samples to dimension greater than 1, unlike prior primal, dual, or BKW-based bounds in this regime.
