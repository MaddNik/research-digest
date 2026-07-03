---
title: "Resultants Meet Resultant: Improving CICO-1 and CICO-2 Attacks on ZK-Friendly Permutations"
date: 2026-07-03 08:22:00 +0200
categories: [Cryptography]
tags: [cryptanalysis, zk-friendly-permutations, arithmetization, cico-attacks]
link: https://eprint.iacr.org/2026/1281
byline: "Bak et al. (IACR ePrint 2026/1281, Mon 29 Jun 2026)"
description: "A new cryptanalytic framework using bivariate resultants improves both CICO-1 and CICO-2 attacks against arithmetization-oriented ZK-friendly permutations."
---

Arithmetization-oriented permutations, designed to be efficient inside zero-knowledge proof systems, are commonly evaluated for security via the CICO-k problem. The best prior CICO-1 attack against permutations built from alpha-inversions used resultants starting from a single input variable, achieving a known time and memory complexity. This paper generalizes the approach to two input variables and extends the temporary-variable-elimination technique to that setting, yielding a new CICO-2 attack framework and a new Start-From-The-Middle CICO-1 attack framework. Both new attacks rely on fast bivariate resultants for the final system-solving step, and using near-linear-complexity resultant algorithms the authors achieve complexity almost linear in the ideal degree for CICO-1, and almost linear in alpha to the power n times the ideal degree for CICO-2, representing the first theoretical improvement of this kind. The authors note that an efficient implementation of the underlying resultant algorithms remains an open challenge.
