---
title: "Software-Pipelining The Number Theoretic Transform on Neural Processing Units: A Loop-Fission Methodology"
date: 2026-10-16 08:17:00 +0200
categories: [FHE]
tags: [ntt, npu-acceleration, barrett-reduction, loop-fission]
link: https://eprint.iacr.org/2026/2474
byline: "Henri Vermeersch et al. (IACR ePrint 2026/2474, Oct 14 2026, TCHES 2027)"
description: "A loop-fission methodology for AI-accelerator neural processing units yields the first efficient number theoretic transform implementations on NPUs, speeding up the core operation behind lattice-based PQC and FHE."
---

Lattice-based post-quantum cryptography and fully homomorphic encryption rely heavily on the number theoretic transform for efficient polynomial multiplication, and while GPUs and FPGAs have been widely explored for NTT acceleration, neural processing units, a fast-growing class of AI accelerators, had remained largely unexplored for cryptographic workloads. This work develops a methodology for accelerating the NTT on NPUs using AMD's AI Engine architecture as a representative platform, built around manual loop fission that splits large, complex loops into smaller primitives to enable efficient software pipelining and avoid memory stalls or register spilling. Applying this methodology the authors build efficient Barrett reduction primitives and three high-throughput, low-latency NTT implementations at radix 2, radix 4, and radix 8, achieving speedups of 8.27 to 13.2 times in throughput and 2.44 to 10.3 times in latency per AI Engine tile compared with prior work on AMD's first-generation AI Engine. The implementations support arbitrary NTT-friendly moduli and polynomial degrees up to 4096 for 14-bit moduli and 2048 for 30-bit moduli, and the paper discusses how the techniques port to other NPU architectures and which architectural features matter most for NTT acceleration. The work is published in TCHES 2027.
