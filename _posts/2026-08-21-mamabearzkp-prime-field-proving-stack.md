---
title: "MamaBearZKP: A Holistic Co-design of Prime Fields and Proving Stacks for High-Throughput ZKP on Modern CPUs"
date: 2026-08-21 08:22:00 +0200
categories: [Cryptography]
tags: [zkp-engineering, prime-fields, hyperplonk, cpu-vectorization]
link: https://eprint.iacr.org/2026/1698
byline: "Jipeng Zhang et al. (IACR ePrint 2026/1698, Aug 15 2026)"
description: "A co-designed prime field and CPU-vectorized proving stack aimed at large speedups for zero-knowledge proof generation."
---

The paper targets computational bottlenecks in modern zero-knowledge proving systems by jointly designing the underlying prime field arithmetic together with the hardware execution strategy, rather than optimizing each in isolation. The core of the approach is a custom 49-bit prime field paired with AVX-512IFMA vectorized instructions for CPU acceleration. The authors report single-threaded speedups of up to 42x, 33x, 15x, 21x, and 21x for ZeroCheck, ProductCheck, DeepFold Commit, DeepFold Open, and end-to-end proof generation respectively, compared to existing baselines, with multi-threaded speedups reaching up to 64x. They attribute the gains to treating field arithmetic, protocol structure, and low-level hardware primitives as a single unified optimization target, applied to the HyperPlonk and DeepFold proving systems.
