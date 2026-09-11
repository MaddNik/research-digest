---
title: "FPGA Acceleration of Fully Homomorphic Encryption with Adaptive Key Switching"
date: 2026-09-11 08:17:00 +0200
categories: [FHE]
tags: [fhe-fpga, key-switching, hardware-acceleration, bootstrapping]
link: https://arxiv.org/abs/2609.09423
byline: "Zhihan Xu et al. (arXiv:2609.09423, Sep 8 2026)"
description: "An adaptive FPGA-based FHE accelerator that dynamically switches between two key-switching methods achieves up to 3.31 times faster bootstrapping than prior state-of-the-art FPGA accelerators."
---

Key-switching is a major performance bottleneck in fully homomorphic encryption (FHE), and a recent method called KLSS reduces some of its operational complexity at the cost of requiring higher computational precision than the traditional Hybrid Key Switching (HKS) method, making their relative speed highly dependent on hardware parallelism, security parameters, and on-chip memory. The authors propose a memory-efficient KLSS datapath that avoids off-chip ciphertext transfers, build a performance model comparing KLSS and HKS overheads, and use it to design an adaptive FPGA-based FHE accelerator that dynamically selects between the two methods during computation. Implemented on an Alveo U280 FPGA and evaluated across multiple FHE benchmarks, the adaptive accelerator achieves a 1.84 to 3.31 times speedup in bootstrapping latency and a 1.66 to 2.52 times speedup in secure image classification compared to state-of-the-art FPGA accelerators.
