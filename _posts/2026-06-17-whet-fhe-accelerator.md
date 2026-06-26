---
title: "WHET: Welding Homomorphic Encryption to Accelerator Architectures"
date: 2026-06-17 08:19:00 +0200
categories: [FHE]
tags: [fhe, hardware-acceleration]
link: https://arxiv.org/abs/2606.11541
byline: "Jongmin Kim et al. (arXiv:2606.11541, Jun 10 2026)"
description: "Memory-centric, architecture-aware optimizations that align FHE constructions with accelerator hardware and report the first sub-millisecond CKKS bootstrapping."
---

This work identifies that conventional fully homomorphic encryption constructions
generate excessive working sets and heavy off-chip memory traffic when run on
accelerators. The authors introduce memory-centric, architecture-aware
optimizations including fine-grained coefficient-to-slot transformation, plaintext
compression, and intermediate modulus raising to reduce the on-chip data footprint
by minimizing temporary ciphertexts and plaintext loads. They also propose
architectural refinements such as specialized buffers and functional-unit
extensions. The reported results are 1.38 to 8.74 times per-area performance
improvements over state-of-the-art accelerators. The authors also claim the
first-ever sub-millisecond CKKS bootstrapping.
