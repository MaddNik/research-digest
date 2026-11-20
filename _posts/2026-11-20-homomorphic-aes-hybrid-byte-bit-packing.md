---
title: "Revisiting homomorphic AES evaluation with Hybrid Byte-Bit Packing"
date: 2026-11-20 08:17:00 +0200
categories: [FHE]
tags: [bgv, transciphering, aes, helib]
link: https://eprint.iacr.org/2026/2885
byline: "Lu Zhang et al. (IACR ePrint 2026/2885, Nov 13 2026)"
description: "A hybrid byte-bit packing strategy for BGV-based homomorphic AES transciphering avoids extra key-switching in the linear layers, speeding up per-block latency by up to 11.7 times."
---

Homomorphic AES evaluation is a standard benchmark for practical fully homomorphic encryption systems. Existing BGV-based AES transciphering schemes typically use byte-oriented slot representations that suit the algebraic structure of the multiplicative inversion in SubBytes, but evaluating the affine transformation and subsequent linear layers in that representation requires extra automorphisms and key-switching operations. The authors propose a hybrid byte-bit packing strategy in which, after the multiplicative inversion, an unpacking step converts the slot packing from byte-oriented to bit-oriented, so the SubBytes affine transformation and the rest of the AES linear transformations can be unified and evaluated over GF(2) using only homomorphic additions, avoiding the key-switching that packed byte-oriented evaluation of these linear components would otherwise need. A hoisting technique further speeds up the unpacking step by 2.5 times compared to a non-hoisted implementation. Implemented in HElib at parameters meeting at least 128-bit security, the approach achieves per-block latency speedups of 2.6 and 11.7 times without bootstrapping, and 2.1 and 3.3 times with bootstrapping, on a local machine and a 64-thread server respectively, compared with a reproduced BGV-based AES baseline under the same settings.
