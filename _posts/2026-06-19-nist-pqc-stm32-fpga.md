---
title: "Comparative Performance Analysis of NIST PQC Standards: From STM32 Software Limitations to FPGA-SoC Acceleration"
date: 2026-06-19 08:07:00 +0200
categories: [PQC]
tags: [post-quantum, hardware-acceleration, embedded-systems]
link: https://arxiv.org/abs/2606.15744
byline: "Mustafa Akif Yildirim et al. (arXiv:2606.15744, Jun 14 2026)"
description: "Shows that NIST signature schemes are impractical in pure software on a Cortex-M4 microcontroller and need FPGA hardware acceleration to run at millisecond speeds."
---

This implementation study evaluates NIST-standardized post-quantum signature schemes on
resource-constrained embedded hardware. The authors report that SPHINCS+ is practically
unusable in a software-only environment due to impractical execution times, and that a
standard Dilithium implementation could not run on an STM32F407G microcontroller because
of memory and timing constraints. They then move to a hybrid hardware and software design
on a Xilinx Zynq-7000 ZedBoard, using an FPGA-based Number Theoretic Transform accelerator.
With that acceleration, key generation and signature generation reach millisecond-level
performance. The conclusion is that quantum-resistant embedded cryptography requires
dedicated hardware acceleration rather than pure software. The paper appeared at the
International Innovation, Science, and Technology Conference (InnoSciTech 2026), pages 36
to 40.
