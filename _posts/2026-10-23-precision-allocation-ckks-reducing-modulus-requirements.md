---
title: "A New Approach to Reducing Modulus Requirements in Homomorphic Computation: Precision Allocation in CKKS"
date: 2026-10-23 08:15:00 +0200
categories: [FHE]
tags: [ckks, modulus-management, precision-allocation]
link: https://eprint.iacr.org/2026/2562
byline: "Zhaoyang Liang et al. (IACR ePrint 2026/2562, Oct 20 2026)"
description: "A new CKKS construction lets average rather than maximum precision requirements govern the ciphertext modulus budget, reducing the initial modulus bit length by 67 percent for a test case of six successive squarings over 256 messages."
---

Reducing the ciphertext modulus needed for a given output precision under RLWE security constraints is a central challenge for homomorphic computation, and existing approaches to CKKS generally size the modulus budget according to the single highest precision requirement among packed values. This work instead allows average rather than maximum precision requirements to govern the modulus budget, achieving savings in the baseline cost by allocating arbitrary output precision among independent packed values under decryption correctness constraints, and quantifying the modulus savings that arise from differences in precision requirements across those values. The construction preserves the standard CKKS ciphertext format, maintaining compatibility with existing optimizations, and inherits CKKS's IND-CPA security without additional cryptographic assumptions. With a 64-bit average precision requirement, the authors transfer 75 bits of precision without reducing evaluation depth and up to 735 bits while preserving correct initial recovery, raising the precision allocated to target values as high as 2,269 bits; for six successive squarings of 256 messages targeting 224-bit precision, the implementation reduces the initial modulus bit length by 67 percent compared with standard CKKS, enabling a fourfold reduction in ring dimension.
