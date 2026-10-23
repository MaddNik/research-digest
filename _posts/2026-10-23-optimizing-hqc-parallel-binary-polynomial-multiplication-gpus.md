---
title: "Optimizing HQC with Enhanced Parallel Binary Polynomial Multiplication on GPUs"
date: 2026-10-23 08:11:00 +0200
categories: [PQC]
tags: [hqc, gpu-acceleration, code-based-cryptography, tensor-cores]
link: https://eprint.iacr.org/2026/2538
byline: "DongCheon Kim et al. (IACR ePrint 2026/2538, Oct 20 2026, TCHES 2027)"
description: "A GPU implementation of the HQC code-based KEM using a parallelized Frobenius additive FFT and INT1 tensor cores reaches 3,828 thousand polynomial multiplications per second and up to 2.03 times higher end-to-end throughput than the prior best GPU implementation."
---

Graphics processing units are widely used as accelerators to handle key-establishment requests in bulk, requiring GPU implementations to sustain high throughput while keeping each request within its latency bound. This work presents a high-performance, end-to-end GPU implementation of Hamming Quasi-Cyclic (HQC), a code-based key encapsulation mechanism, targeting its dominant cost of binary polynomial multiplication over the Galois field GF(2). The authors propose a parallelization of the Frobenius additive fast Fourier transform and a mapping of the cyclic product, viewed as a Toeplitz matrix-vector product, onto one-bit integer tensor cores, plus a GPU-resident computation strategy and warp-level parallelization for hashing, Reed-Muller/Reed-Solomon coding, and fixed-weight sampling. Varying the mapping of KEM instances to GPU threads yields five variants spanning the throughput-latency trade-off; on an RTX 4090, the coarse-grained variant maximizes batch throughput, with the multiplier reaching 3,828 thousand polynomial multiplications per second, about 2.9 times the prior GPU HQC implementation HIGH, and the full KEM achieving 1.56, 1.55, and 2.03 times higher end-to-end throughput than HIGH for key generation, encapsulation, and decapsulation respectively. A tensor-core-based variant achieves single-shot latency as low as 254 microseconds, and all five variants are further evaluated on an RTX 3090 and an embedded Jetson AGX Orin to confirm cross-platform portability.
