---
title: "Efficient (Functional) Bootstrapping for CKKS over the Conjugate-Invariant Ring"
date: 2026-10-30 08:19:00 +0200
categories: [FHE]
tags: [ckks, bootstrapping, conjugate-invariant-ring, functional-bootstrapping]
link: https://eprint.iacr.org/2026/2618
byline: "Jiaming Liu et al. (IACR ePrint 2026/2618, Oct 23 2026)"
description: "A real FFT algorithm over the conjugate-invariant ring enables native bootstrapping for conjugate-invariant CKKS, achieving up to 12.86 times faster single-ciphertext bootstrapping and up to 1.68 times higher functional bootstrapping throughput than prior methods."
---

Conjugate-invariant CKKS halves the RLWE dimension needed to store real-valued data relative to standard CKKS, but it cannot be bootstrapped directly in its native ring because the linear transformations used in bootstrapping require storing complex values, so existing methods convert ciphertexts to standard CKKS, bootstrap there, and convert back at extra cost. This paper's first contribution is a real FFT algorithm over the conjugate-invariant ring that enables native bootstrapping without that conversion. The second contribution addresses functional bootstrapping over this ring, adapting a real-valued interpolant with radial correction and developing a single-cosine Hermite interpolation method that uses just one real ciphertext, while showing that existing complex-valued interpolation methods can still be run using two real ciphertexts to simulate complex arithmetic. Implemented in Lattigo, the native bootstrapping achieves a 1.14 to 12.86 times speedup in single-ciphertext bootstrapping depending on baseline and linear-transformation depth, and the functional bootstrapping methods achieve 1.16 to 1.68 times higher throughput than state-of-the-art methods over standard CKKS.
