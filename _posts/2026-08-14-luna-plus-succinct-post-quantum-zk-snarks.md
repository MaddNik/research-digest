---
title: "LUNA+: More Succinct Post-Quantum ZK-SNARKs from Computational Privacy"
date: 2026-08-14 08:11:00 +0200
categories: [PQC]
tags: [zk-snark, designated-verifier, mlwe, succinctness]
link: https://eprint.iacr.org/2026/1639
byline: "Yuki Kume et al. (IACR ePrint 2026/1639, Aug 12 2026)"
description: "LUNA+ replaces the statistical privacy foundation of the LUNA lattice-based designated-verifier zk-SNARK with a computational one, shrinking proof and setup sizes."
---

The original LUNA scheme is a designated-verifier lattice-based zero-knowledge argument achieving quasi-optimal asymptotic proof length, but its practical parameters were limited by a statistical privacy analysis based on a Leftover Hash Lemma with Leakage, which forces large smudging noise and correspondingly large lattice dimension, modulus, and proof and common-reference-string sizes. LUNA+ replaces this with a computational privacy analysis, showing that the circuit privacy of LUNA's re-randomization step can instead rest on the hardness of a Matrix Hint-Module Learning With Errors problem. The authors also introduce a new underlying problem, Coset Error Knapsack MH-MLWE, in which the MLWE error is drawn from a coset of a lattice. The result is meaningfully improved concrete succinctness over the original LUNA construction.
