---
title: "Efficient NTRU+ Implementations on Cortex-M"
date: 2026-10-23 08:08:00 +0200
categories: [PQC]
tags: [ntru, lattice-cryptography, cortex-m, number-theoretic-transform]
link: https://eprint.iacr.org/2026/2568
byline: "Subeen Cho et al. (IACR ePrint 2026/2568, Oct 20 2026)"
description: "Two new Cortex-M implementations of the NTRU+ lattice KEM, one speed-optimized and one memory-optimized, cut execution time by up to 52.43 percent and peak stack usage by up to 82.60 percent relative to the official C implementation."
---

Most embedded implementations of lattice-based key encapsulation mechanisms (KEMs) rely on 2-way number-theoretic transforms (NTTs) over power-of-two cyclotomic rings, while schemes built on 3-way NTTs combining radix-3 and radix-2 layers remain scarcely studied on microcontrollers. This work presents efficient implementations of NTRU+, a KEM built on 3-way NTTs, on Arm Cortex-M0+, M3, M4, and M7, configuring layer fusion, modular arithmetic, and instruction scheduling for the 3-way NTT on each core and parameter set. The authors introduce omega-folded front layers that compute the first two layers of the forward NTT on ternary inputs without modular reduction, and they present both a speed-optimized implementation that keeps operands as full polynomial arrays and a memory-optimized implementation that reuses a single polynomial workspace. On physical boards, the speed-optimized implementation reduces execution time by up to 52.43 percent compared with the official optimized C implementation, while the memory-optimized implementation cuts peak stack usage by up to 82.60 percent while still running faster than the reference in every KEM operation. A controlled NTT-replacement experiment and per-technique comparisons further show that the same optimization can have different effects depending on the instruction set and pipeline of each core.
