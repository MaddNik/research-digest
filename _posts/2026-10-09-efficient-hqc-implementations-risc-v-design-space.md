---
title: "Efficient HQC Implementations on RISC-V: A Cross-Layer Design Space Exploration"
date: 2026-10-09 08:15:00 +0200
categories: [PQC]
tags: [hqc, risc-v, fpga, hardware-software-codesign]
link: https://arxiv.org/abs/2610.06058
byline: "Maximilian Schoffel et al. (arXiv:2610.06058, Oct 5 2026)"
description: "A comprehensive exploration of RISC-V-based HQC implementations characterizes nearly 30,000 architectural configurations and finds Pareto-optimal designs that beat the prior state of the art on both resource use and latency."
---

RISC-V-based hardware and software co-design has become an established way to implement post-quantum cryptography on embedded devices, offering the flexibility needed for crypto-agility, but prior RISC-V implementations of the HQC key-encapsulation mechanism have explored only a small part of this design space. The authors present what they describe as the most comprehensive exploration of RISC-V-based HQC to date, built around a new parametrizable architecture framework that characterizes 29,920 distinct architectural configurations across all three HQC security levels on FPGA. The Pareto-optimal configurations from this exploration outperform the prior state-of-the-art RISC-V-based HQC implementation, ranging from 4.8 times lower LUT utilization at 17 percent lower latency, up to 69.6 times lower latency at 30 percent lower LUT utilization. These configurations also require up to 10.6 times fewer block RAMs, giving implementers a much richer set of efficient operating points to choose from.
