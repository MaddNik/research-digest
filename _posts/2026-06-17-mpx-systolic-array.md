---
title: "MPX: A Unified Systolic Array for Matrix and Polynomial Multiplication"
date: 2026-06-17 08:22:00 +0200
categories: [FHE]
tags: [hardware-acceleration]
link: https://arxiv.org/abs/2606.16394
byline: "George Alexakis et al. (arXiv:2606.16394, Jun 15 2026)"
description: "A dual-mode systolic array that supports both matrix multiplication and direct polynomial multiplication for FHE and post-quantum cryptography on a single hardware fabric."
---

Polynomial multiplication is a fundamental kernel in fully homomorphic encryption
and post-quantum cryptography, and is commonly accelerated through Number Theoretic
Transforms. This work designs MPX, a dual-mode systolic array that supports both
matrix multiplication and direct polynomial multiplication within the same hardware
fabric, motivated by the observation that the wavefront dataflow of systolic arrays
naturally aligns with the accumulation pattern of polynomial multiplication. The
authors report that adding this dual-mode capability requires only about 20 percent
additional area with negligible power overhead during matrix operations. In
polynomial-multiplication mode, they report more than 1.2 times lower latency
compared to running Number Theoretic Transform based polynomial multiplication on
systolic matrix engines. By unifying the two operation modes, MPX reuses a single
hardware substrate across the matrix-heavy and polynomial-heavy workloads common to
encrypted and post-quantum computation.
