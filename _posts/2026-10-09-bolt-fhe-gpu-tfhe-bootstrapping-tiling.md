---
title: "BOLT-FHE: An Efficient Unified Framework for GPU-based TFHE Bootstrapping via On-Chip Local Tiling Strategies"
date: 2026-10-09 08:17:00 +0200
categories: [FHE]
tags: [tfhe, gpu-acceleration, bootstrapping]
link: https://eprint.iacr.org/2026/2356
byline: "Yanren Chen et al. (IACR ePrint 2026/2356, Oct 5 2026, TCHES 2026)"
description: "BOLT-FHE is a GPU bootstrapping framework for TFHE that fuses the blind rotation and external product chain into a single MegaKernel, reaching over 40,000 bootstrappings per second on a commodity GPU."
---

Bootstrapping is the main performance bottleneck in bitwise fully homomorphic encryption, and this paper presents BOLT-FHE, a GPU bootstrapping framework emphasizing block-local execution, on-chip tiling, and a unified MegaKernel that supports both gadget decomposition and modulus raising, including optional support for common-mask-assumption packing. The design keeps the accumulator update chain within a single thread block and fuses NTT, inverse NTT, external products, and accumulator updates using a fixed execution template, with two compile-time parameters controlling multi-warp cooperation and per-thread register footprint. On an NVIDIA RTX 4090, BOLT-FHE reaches 40,166 bootstrappings per second at 128-bit security. Compared to the prior state-of-the-art GPU implementation VeloFHE, BOLT-FHE achieves 1.85 to 2.92 times speedups with gadget decomposition, and for modulus raising it improves by 2.38 to 2.42 times without packing and by 3.17 to 3.31 times with the best packing configuration.
