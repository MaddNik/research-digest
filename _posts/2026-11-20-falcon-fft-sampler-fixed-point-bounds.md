---
title: "Bounds of Falcon's Fast Fourier Sampler with Fixed-Point Arithmetic"
date: 2026-11-20 08:07:00 +0200
categories: [PQC]
tags: [falcon, fn-dsa, lattice-signatures, formal-verification]
link: https://eprint.iacr.org/2026/2902
byline: "Vincent Hwang (IACR ePrint 2026/2902, Nov 15 2026)"
description: "A formally verified Renyi divergence analysis bounds the security loss of Falcon's fixed-point fast Fourier sampler compared to its real-arithmetic specification."
---

Falcon was selected by NIST for standardization as FN-DSA in the forthcoming FIPS 206, and its signature generation relies on a fast Fourier sampler defined over the complex numbers. This report bounds the Renyi divergence between that sampler in real arithmetic and its fixed-point implementation on the tail-cut event, where every sample stays within a fixed number of standard deviations of its center. For a reference bit security of 128 at degree 512 and 256 at degree 1024 over 2 to the 64 signatures, the bound keeps 126.28 and 248.78 bits of security at the plain center, and slightly more at the fractional center, for every key that key generation accepts. The author proposes four changes to the fixed-point implementation, including rejecting rather than saturating a candidate at a saturated shift and adding three new checks on the key generation tree, and shows that two of these changes are load-bearing for the proof. The bounds rest on machine-checked proofs in CryptoLine and Lean over compiled aarch64 code, and the report notes that the compiler turned constant-time C into key-dependent branches on one tested build, leaving a branchless assembly reference as future work.
