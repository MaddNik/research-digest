---
title: "Flying, Not Floating: Precise Fixed-Point Falcon on Embedded Processors"
date: 2026-10-16 08:09:00 +0200
categories: [PQC]
tags: [falcon, fn-dsa, fixed-point-arithmetic, cortex-m4]
link: https://eprint.iacr.org/2026/2431
byline: "Stef Halmans et al. (IACR ePrint 2026/2431, Oct 9 2026)"
description: "Researchers present the first fixed-point Falcon signer for microcontrollers, cutting signing cycles while keeping the numerical precision that the FN-DSA standard requires."
---

The Falcon digital signature scheme, currently under standardization as FN-DSA, needs real-number arithmetic during signing, and its security depends on how precise that arithmetic is. Building on prior work that showed Falcon-512 can sign using 64.64 fixed-point arithmetic on 64-bit hosts, this paper presents the first fixed-point FN-DSA signer for microcontrollers, implemented in constant-time Cortex-M4 assembly with 32.64 arithmetic for both Falcon-512 and Falcon-1024. New techniques keep reciprocals, inverse square roots, and small constants wide and round only once at the point of use, restoring precision that a naive fixed-point implementation would lose. The resulting signer needs around 45 percent fewer cycles than double-precision emulation, and its measured precision supports about 2 to the power 99.7 and 2 to the power 96.7 signing queries per key for Falcon-512 and Falcon-1024 respectively, comfortably above the 2 to the power 64 target and well beyond double precision's roughly 2 to the power 61.5 and 2 to the power 58.7. The twelve-byte words do raise signing RAM usage, and the authors also derive key generation acceptance bounds and give recommendations for the fixed-point FN-DSA variant that NIST is planning.
