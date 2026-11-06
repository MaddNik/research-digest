---
title: "SpreadMAYO: Unlocking Greater Parallelism for Faster MAYO Signatures on GPUs"
date: 2026-11-06 08:12:00 +0200
categories: [PQC]
tags: [mayo, multivariate-cryptography, gpu-acceleration, post-quantum-signatures]
link: https://eprint.iacr.org/2026/2705
byline: "Zhuoyu Xie et al. (IACR ePrint 2026/2705, Oct 31 2026)"
description: "SpreadMAYO restructures MAYO's GPU implementation to expose finer-grained parallelism, speeding up signing by up to 6.93 times over the prior GPU baseline."
---

MAYO is a multivariate signature scheme and a Round 3 candidate in NIST's additional post-quantum signature standardization process, valued for its compact keys and signatures. Prior GPU implementations of MAYO under-exploit parallelism within each operation, since equation-slice partitioning serializes independent matrix work and signing requires frequent thread synchronization during linear-system construction and elimination. This paper presents SpreadMAYO, a GPU implementation that distributes matrix contractions across rows, output positions, and 64-bit limbs, packing sixteen GF(16) coefficients per limb and processing them with native 32-bit operations instead of lookup tables. For signing, threads privately accumulate columns with deferred polynomial reduction, transpose packed columns using warp shuffles, and eliminate rows below each pivot in parallel; the authors also fuse AES-based key expansion with matrix computation to cut global-memory traffic. On an NVIDIA RTX 4090, SpreadMAYO outperforms the Round 3 adapted GPU baseline by 2.33 to 3.71 times in key generation, 4.40 to 6.93 times in signing, and 3.42 to 5.13 times in verification, reaching up to 10.75 times in repeated-key server signing.
