---
title: "From Round Skipping to S-Box Skipping: Attacking Poseidon's Partial Layer via Subspace Restriction"
date: 2026-08-21 08:19:00 +0200
categories: [Cryptography]
tags: [poseidon, cryptanalysis, zk-friendly-hash, algebraic-attacks]
link: https://eprint.iacr.org/2026/1692
byline: "Amit Singh Bhati et al. (IACR ePrint 2026/1692, Aug 15 2026)"
description: "A new subspace-restriction technique breaks deep into the partial rounds of the Poseidon hash permutation used in zero-knowledge proof systems."
---

The authors introduce a generalized S-box skipping technique that processes an initial full round plus a run of partial rounds without increasing the polynomial degree of the underlying system. By restricting the solution space in a way that is independent of the specific round constants and MDS matrix, they linearize the internal state transitions, turning an otherwise intractable polynomial system into a tractable parameterized ideal. Using this, they build a probability-1 distinguisher spanning multiple rounds and report experimental solutions to the CICO-1 problem over 28 of 31 rounds and CICO-2 over 25 of 31 rounds, evaluated on Ethereum's KoalaBear field parameters (t equals 24, alpha equals 3). The authors state the method depends only on the parameters t and k, so the results apply to the general Poseidon structure regardless of the choice of round constants, MDS matrix, S-box exponent alpha, or field size p.
