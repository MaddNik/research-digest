---
title: "Exposing SIMD Parallelism in SQIsign: An AVX-512 Implementation"
date: 2026-08-21 08:12:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-based, avx-512, simd-optimization]
link: https://eprint.iacr.org/2026/1713
byline: "Weize Wang et al. (IACR ePrint 2026/1713, Aug 17 2026)"
description: "An AVX-512IFMA implementation that restructures SQIsign's computational dependencies to gain vectorized speedups, including a 3.18x faster verification."
---

This paper looks at how to extract vectorization opportunities from isogeny-based post-quantum schemes, focusing on SQIsign. Rather than only optimizing field multiplication in isolation, the authors reorganize the computational dependency graphs of higher-level operations to expose SIMD parallelism more broadly. Using an AVX-512IFMA implementation, they report end-to-end speedups of 1.76x for key generation, 1.71x for signing, and 3.18x for verification at NIST security level I. They also apply the same approach to the CORAL scheme, reporting speedups of 1.28x to 1.40x for key generation and 1.92x to 2.46x for shared-key computation across the parameter sets tested.
