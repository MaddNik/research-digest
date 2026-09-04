---
title: "Order-Four Symmetry in BGV Bootstrapping: Faster Digit Extraction for Large Primes"
date: 2026-09-04 08:14:00 +0200
categories: [FHE]
tags: [bgv, bootstrapping, digit-extraction, helib]
link: https://eprint.iacr.org/2026/1847
byline: "Zhenyu Xiong et al. (IACR ePrint 2026/1847, Aug 31 2026)"
description: "An order-four character filter on the digit-extraction polynomial and a Galois-structured mixed-radix butterfly for linear transforms together speed up BGV thin bootstrapping by 1.27 times for large-prime plaintext moduli."
---

Bootstrapping is the computational bottleneck of BGV and BFV fully homomorphic encryption, and it scales particularly poorly with large plaintext primes across its two dominant stages, digit extraction and linear transforms. This paper introduces two algebraic optimizations addressing both stages: for digit extraction, choosing an auxiliary radix A with A squared congruent to minus 1 modulo the plaintext prime induces an order-four character filter that eliminates most monomials from the canonical digit-extraction polynomial, reducing non-scalar multiplications from O(square root of d) to O(square root of d over r). For linear transforms, the authors give the first concrete instantiation of a Galois-structured mixed-radix butterfly decomposition for non-power-of-two cyclotomics, reducing the automorphism count from O(square root of D) to O(log D). On a standard NTT-friendly large-prime parameter set with plaintext modulus 65537 and 32768 slots, a single-threaded HElib implementation achieves a 1.85 times digit-extraction speedup and a 1.27 times total thin-bootstrapping speedup over the prior state of the art, with the untouched pipeline stages changing by at most one percent. Across nineteen parameter sets, the digit-extraction speedup ranges from 1.72 to 2.13 times, and the work is a minor revision of a paper accepted at Asiacrypt 2026.
