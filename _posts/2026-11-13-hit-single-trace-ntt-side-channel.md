---
title: "HIT: Single-Pass Inference for Single-Trace NTT Side-Channel Attacks"
date: 2026-11-13 08:31:00 +0200
categories: [Hardware Security]
tags: [side-channel, ml-kem, ml-dsa, ntt]
link: https://eprint.iacr.org/2026/2865
byline: "Yihan Nie et al. (IACR ePrint 2026/2865, Nov 11 2026)"
description: "A new hierarchical inference tree replaces loopy belief propagation for single-trace NTT side-channel attacks, running over 900 times faster than prior methods and enabling the first single-trace analytical attack on the ML-DSA NTT."
---

In physical implementations of the post-quantum standards ML-KEM and ML-DSA, the Number-Theoretic Transform processes secret polynomials directly and is a primary target for single-trace side-channel key recovery, but existing Soft Analytical Side-Channel Attacks apply loopy belief propagation over cyclic factor graphs that fails under high noise and becomes infeasible for ML-DSA because the per-step update cost grows with the square of the modulus. The authors present the Hierarchical Inference Tree, or HIT, a framework built on the insight that small secret inputs deterministically fix all NTT intermediate values across the recursive butterfly network. Instead of loopy belief propagation, HIT merges and prunes candidate inputs from leaves to root in a single pass over an acyclic binary tree, eliminating belief oscillation, guaranteeing constant runtime, and decoupling complexity from the modulus size. On ML-KEM-768, HIT runs more than 900 times faster than state-of-the-art SASCA and more than doubles noise tolerance, and it also enables the first single-trace analytical attack on the ML-DSA NTT, recovering each polynomial in under one second. On physical ARM Cortex-M4 targets, HIT achieves over 98 percent polynomial recovery across both standards using only 20 to 80 profiling traces.
