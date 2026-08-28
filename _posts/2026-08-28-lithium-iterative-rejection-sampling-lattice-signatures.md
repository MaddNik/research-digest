---
title: "Lithium: Making Iterative Rejection Sampling Practical for Compact Lattice Signatures"
date: 2026-08-28 08:13:00 +0200
categories: [PQC]
tags: [lattice-based-signatures, rejection-sampling, avx-512, post-quantum-implementation]
link: https://eprint.iacr.org/2026/1790
byline: "Jipeng Zhang et al. (IACR ePrint 2026/1790, Aug 24 2026)"
description: "Lithium turns Gaertner's theoretical iterative rejection sampling design into a concrete, implementation-ready lattice signature scheme that is both smaller and faster than ML-DSA."
---

ML-DSA offers a practical Fiat-Shamir lattice-signature baseline, but its signature sizes remain large enough to make bandwidth and storage first-order costs, and Gaertner's iterative rejection sampling construction from CRYPTO 2025 showed this design family could be made much more compact, though it was unclear whether the theoretical design could be turned into a practical scheme without an impractical signer. The authors present Lithium, which co-designs its parameters, discrete Gaussian sampler, ApproxExp evaluation, iterative rejection sampling, and rANS encoder so that compactness does not come at the cost of signer efficiency. They provide algorithmic and vectorized optimizations along with a portable reference implementation and vectorized AVX2 and AVX-512 implementations, with Lithium-120 targeting a security level close to ML-DSA-44. Experiments show their fastest implementation signs faster than ML-DSA-44, at 166,000 versus 191,000 cycles, while producing signatures about half the size at 1,187 bytes versus 2,420 bytes, and Lithium-120 is more compact and signs about 7.5 times faster than HAETAE-120.
