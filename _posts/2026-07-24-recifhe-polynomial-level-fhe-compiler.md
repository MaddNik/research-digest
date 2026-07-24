---
title: "Ciphertext- and Polynomial-Level Optimization for Fully Homomorphic Encryption"
date: 2026-07-24 08:17:00 +0200
categories: [FHE]
tags: [fhe-compiler, polynomial-optimization, redundancy-elimination]
link: https://arxiv.org/abs/2607.15750
byline: "Seongho Kim et al. (arXiv:2607.15750, Jul 17 2026)"
description: "The paper introduces Recifhe, an FHE compiler that optimizes across both ciphertext-level and polynomial-level representations instead of only the coarse-grained ciphertext level used by prior compilers."
---

Recent FHE compilers optimize FHE programs mainly at the coarse-grained ciphertext level, which the authors argue misses optimization opportunities available at the finer-grained polynomial level. The paper presents Recifhe, a system that converts non-FHE programs into FHE programs while applying optimizations across both levels and eliminating redundant polynomial computations. By unifying ciphertext-level and polynomial-level optimization in one pipeline, the compiler avoids the missed cross-level opportunities of prior single-level approaches. The authors report a 1.25 times speedup over optimization that operates at the ciphertext level only. The work targets compiler and toolchain support for FHE rather than a new cryptographic scheme.
