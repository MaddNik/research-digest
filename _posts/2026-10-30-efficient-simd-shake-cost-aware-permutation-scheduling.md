---
title: "Efficient SIMD SHAKE through Cost-Aware Permutation Scheduling"
date: 2026-10-30 08:15:00 +0200
categories: [PQC]
tags: [ml-kem, haetae, shake, simd-implementation]
link: https://eprint.iacr.org/2026/2666
byline: "Hang Zhang et al. (IACR ePrint 2026/2666, Oct 28 2026)"
description: "A cost-aware scheduling method for SIMD Keccak permutations across multiple SHAKE streams speeds up ML-KEM by up to 1.44 times and HAETAE by up to 1.28 times on Apple M5, Cortex-A72, and Intel processors."
---

Lattice-based cryptography relies heavily on SHAKE to expand seeds into byte strings for matrix generation and sampling, and SIMD implementations of Keccak can process multiple hash streams in parallel, but differing stream lengths and input dependencies often prevent full SIMD utilization. This paper presents a cost-aware method for scheduling Keccak permutations across hash streams within a single execution of a cryptographic algorithm, grouping ready streams and dividing long streams into segments that can be regrouped, guided by a model of permutation calls, state movement, initialization, and input preparation costs. Evaluated on ML-KEM and HAETAE across an Apple M5, a Cortex-A72, and an Intel Core i5-11500 using Keccak kernels processing two, four, or eight streams per call, the scheduling method speeds up ML-KEM encapsulation by up to 1.31 times and decapsulation by up to 1.44 times, while HAETAE signing speeds up by up to 1.28 times and verification by up to 1.26 times.
