---
title: "FN-DSA on Arm Cortex-M55: Revisiting a Floating-Point Lattice Signature with Native FP64 and Helium"
date: 2026-10-23 08:09:00 +0200
categories: [PQC]
tags: [fn-dsa, falcon, cortex-m55, lattice-signatures]
link: https://eprint.iacr.org/2026/2559
byline: "Seung-Won Lee et al. (IACR ePrint 2026/2559, Oct 20 2026)"
description: "The first FN-DSA implementation on Arm Cortex-M55 that reproduces the reference known-answer tests exactly while running up to 1.93 times faster, by exploiting the core's native double-precision FPU and Helium vector extension."
---

FN-DSA has the shortest signatures among NIST's post-quantum signature standards, but its reference binary64 floating-point arithmetic is normally emulated with integer instructions on microcontrollers, making signing slow. Prior speedups either change the arithmetic or sampling order, so their signatures no longer match the reference known-answer tests, or rely on double-precision SIMD instructions that microcontrollers typically lack. The authors exploit the fact that the Arm Cortex-M55 has both a double-precision floating-point unit and the M-Profile Vector Extension (MVE, also called Helium), presenting the first FN-DSA implementation that reproduces the reference known-answer tests exactly, runs in constant time, and is still faster than the reference. They vectorize the NTTs with layer merging and the fixed-point FFT of key generation using split-word Q32 arithmetic on the MVE, and use bit-exact FP64 arithmetic on the FPU for the FFT, LDL decomposition, split, merge, and sampler of signing, alongside an exponent-normalized division trick and vectorized Keccak bit interleaving. Key generation, signing, and verification become up to 1.23, 1.93, and 1.30 times faster than the reference on the same core respectively, with batch verification of four signatures up to 1.75 times faster.
