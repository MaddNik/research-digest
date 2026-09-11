---
title: "PHAT: PHotonic Accelerator for TFHE"
date: 2026-09-11 08:14:00 +0200
categories: [FHE]
tags: [tfhe, photonic-accelerator, bootstrapping, phase-change-memory]
link: https://arxiv.org/abs/2609.11613
byline: "Guowei Yang et al. (arXiv:2609.11613, Sep 10 2026)"
description: "PHAT is an electro-photonic accelerator that uses optically-addressed phase-change memory to speed up the FFT operations in TFHE bootstrapping, achieving up to 5.10 times speedup over a state-of-the-art ASIC."
---

Fully homomorphic encryption over the torus (TFHE) supports arbitrary operations but suffers from high computation and communication overhead, particularly in the fast Fourier transform (FFT) operations required during bootstrapping, and conventional electronic accelerators struggle with throughput due to technology scaling limits and the memory-wall problem. The authors propose PHAT, a photonic accelerator for TFHE that uses optically-addressed phase-change memory (OPCM) based processing-in-memory to deliver high computation and communication throughput for FFT operations. To handle the challenges of mapping FFT to OPCM, including high-precision analog computation and the latency and energy cost of programming OPCM cells, they introduce an electro-photonic accelerator architecture with OPCM-based FFT units, a twiddle-stationary dataflow tailored for OPCM, and a scheduling mechanism that maximizes FFT unit utilization. Across four real-world TFHE workloads, PHAT delivers 2.14 to 5.10 times speedup over a state-of-the-art ASIC accelerator.
