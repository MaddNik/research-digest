---
title: "Multilevel Amortized Gaussian Elimination in Information-Set Decoding: Applications to HQC and PCG"
date: 2026-07-31 08:10:00 +0200
categories: [PQC]
tags: [code-based, hqc, information-set-decoding, cryptanalysis]
link: https://eprint.iacr.org/2026/1498
byline: "Kevin Carrier et al. (IACR ePrint 2026/1498, Jul 22 2026)"
description: "Refined information-set decoding techniques shave several bits off the estimated security of HQC and related pseudorandom correlation generators."
---

The paper revisits the Reduce-and-Prange technique of Kim and Lee for information-set decoding in the sublinear regime and applies a branching-process analysis for improved accuracy. The authors introduce MAGE-Stern, which extends partial pivot reuse to Stern's algorithm, yielding roughly a 3-bit improvement in time complexity against HQC while reducing memory usage by about 12 bits. They report that the standardized HQC Category I parameter set, targeted at 128-bit security, now appears to sit at approximately 140 bits, which is about 3 bits below its original 143-bit NIST security target estimate. When combined with projective decoding and applied to pseudorandom correlation generator parameters, the techniques yield up to 6-bit improvements over earlier attacks.
