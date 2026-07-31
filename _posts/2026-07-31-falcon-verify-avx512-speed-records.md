---
title: "Falcon Verify on AVX-512: Speed Records"
date: 2026-07-31 08:07:00 +0200
categories: [PQC]
tags: [falcon, avx-512, signature-verification, hardware-optimization]
link: https://eprint.iacr.org/2026/1539
byline: "David Rubin et al. (IACR ePrint 2026/1539, Jul 27 2026)"
description: "An optimized AVX-512 implementation of Falcon signature verification sets new speed records on AMD Zen5 hardware."
---

The authors rewrite Falcon's number-theoretic transform using a 32-bit Barrett-style representation instead of the standard 16-bit Montgomery approach, combined with Shoup-Harvey precomputed multipliers. This achieves Falcon-512 verification in 3.6 microseconds on AMD Zen5, a 2.6 times improvement over prior optimized implementations. They further identify hash-to-point computation as the remaining bottleneck and propose a non-standard variant swapping SHAKE256 for KTP256, a parallel-squeeze extendable output function derived from KangarooTwelve, cutting verification time to 2.2 microseconds, a 4.2 times speedup over baseline. The work targets Falcon, one of NIST's standardized post-quantum signature schemes.
