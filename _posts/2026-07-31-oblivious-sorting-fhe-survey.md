---
title: "Oblivious Sorting under Fully Homomorphic Encryption: A Comprehensive Survey and Performance Analysis"
date: 2026-07-31 08:18:00 +0200
categories: [FHE]
tags: [tfhe, oblivious-sorting, benchmarking, survey]
link: https://eprint.iacr.org/2026/1495
byline: "Omar Ahmed et al. (IACR ePrint 2026/1495, Jul 21 2026)"
description: "A systematic survey and benchmark of eighteen oblivious sorting algorithms across three major FHE schemes finds TFHE the most efficient for sorting."
---

The paper addresses the challenge of adapting sorting routines, which normally rely on data-dependent branching, to the FHE setting where such branching is not directly possible. The authors introduce a new metric, FHE-Effort, to measure the efficiency of homomorphic sorting circuits, and benchmark eighteen algorithms across three major FHE schemes using a unified codebase. Their results indicate that TFHE is currently the most efficient scheme for sorting applications among those tested. They further find that sorting networks such as Odd-Even Merge and Bitonic Sort offer the best algorithmic architectures for this task.
