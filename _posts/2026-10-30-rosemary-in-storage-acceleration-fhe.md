---
title: "Rosemary: Efficient and Adaptable In-Storage Acceleration for Fully Homomorphic Encryption"
date: 2026-10-30 08:21:00 +0200
categories: [FHE]
tags: [fhe-accelerator, in-storage-processing, i-o-bottleneck, hardware-acceleration]
link: https://arxiv.org/abs/2610.38262
byline: "Xuan Wang et al. (arXiv:2610.38262, Oct 28 2026)"
description: "Rosemary moves FHE computation inside NAND flash solid-state drives to address the storage input/output bottleneck that consumes 71 to 85 percent of execution time in large-scale FHE workloads, achieving a 185.7 times geometric-mean speedup over CPU and GPU baselines."
---

The authors observe that state-of-the-art FHE systems spend 71 to 85 percent of their execution time moving data between storage and compute units rather than performing useful computation, a bottleneck that prior FHE accelerators largely overlook because they focus on small benchmarks that fit in main memory. Rosemary addresses this with a heterogeneous acceleration system built around a novel in-storage processing architecture combined with compiler-level and algorithmic optimizations. Its components include an adaptable, hardware-aware FHE engine placed inside a NAND flash-based solid-state drive for efficient and cost-effective in-storage FHE processing, a throughput-data-aware program allocator that partitions FHE workloads into heterogeneous programs, and a compiler-level ciphertext-aware optimizer that exploits FHE kernels suited to low-cost in-storage execution. Across a diverse set of FHE workloads including encrypted deep learning inference and cloud database queries, Rosemary achieves geometric-mean speedups of 185.7 times over state-of-the-art CPU and GPU implementations and 3.7 times over prior FHE accelerators, while improving energy efficiency by up to 3.9 times and energy-delay-area-product by up to 16.5 times.
