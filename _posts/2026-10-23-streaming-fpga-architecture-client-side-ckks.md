---
title: "A Combined Streaming FPGA Architecture for Client-Side CKKS Encoding and Encryption"
date: 2026-10-23 08:21:00 +0200
categories: [FHE]
tags: [ckks, fpga-acceleration, client-side-encryption, fhe-fpga]
link: https://arxiv.org/abs/2610.27204
byline: "Joseph Kurina et al. (arXiv:2610.27204, Oct 19 2026, FPT 2026)"
description: "A streaming FPGA accelerator that shares hardware between CKKS floating-point encoding and modular encryption delivers 5,143 complete ciphertexts per second, about 45 times more than a CPU-based SEAL-Embedded worker on the same workstation."
---

Before a client can let a service process encrypted data under homomorphic encryption, it must first encode and encrypt its own inputs, and sharing hardware between the floating-point encoding transform and the modular encryption transform can reduce chip area but requires those roles to execute at different times. The authors present a streaming FPGA architecture for CKKS encoding and encryption that computes the shared floating-point encoding transform once and then performs the integer transforms for six residue moduli in parallel, with dedicated transform pipelines exchanging intermediate results on chip rather than through off-chip memory. DSP Builder generates the transform RTL, and the Altera HLS IP Gen compiler compiles the surrounding SYCL pipeline into an accelerator functional unit integrated with DMA and control logic. At polynomial degree N equal to 8192, the Altera Agilex 7 implementation delivers 5,143 complete ciphertexts per second at 471 megahertz, compared with 113 ciphertexts per second from a single SEAL-Embedded CPU worker on the same workstation using all 4,096 slots for real-valued inputs; the measurements cover the full path from prepared-input computation through complete ciphertext construction, including FPGA submission and output delivery.
