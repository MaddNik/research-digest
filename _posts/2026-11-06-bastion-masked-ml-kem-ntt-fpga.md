---
title: "BASTION: Lock-Step, Staggered and Sequential Share Schedules for a First-Order Masked ML-KEM NTT on FPGA"
date: 2026-11-06 08:32:00 +0200
categories: [Hardware Security]
tags: [ml-kem, masking, fpga, side-channel-analysis]
link: https://eprint.iacr.org/2026/2765
byline: "Marcos Lázaro Díaz (IACR ePrint 2026/2765, Nov 4 2026)"
description: "BASTION compares three share-scheduling strategies for a masked ML-KEM NTT core on FPGA, finding that all resist first-order leakage but differ sharply in second-order leakage and hardware cost."
---

The number theoretic transform is the arithmetic core of ML-KEM and a frequent side-channel target in hardware; because the transform is linear, first-order masking can be applied share by share without fresh randomness, but it leaves open the question of exactly when each share should be processed. This paper implements three share-processing schedules, lock-step, staggered, and sequential, on one first-order masked NTT core for ML-KEM on an Artix-7 FPGA, measuring their hardware cost and pre-silicon leakage under a single synthesis flow and against an iso-architectural unmasked control. The lock-step core costs 1.56 times the lookup tables, 2.33 times the slices, and twice the DSP blocks of the unmasked control at an unchanged cycle count but a reduced clock frequency of 196.1 instead of 227.3 megahertz, while the sequential core needs only 9 more lookup tables than the control but twice the cycles. On a whole-design leakage model calibrated with injected flaws detected within 750 traces, none of the three schedules leaks at first order across five pairs of 100,000-trace runs, but at second order they differ sharply: the lock-step core leaks in single samples, the sequential core leaks only at a specific, publicly predictable pair of samples, and the staggered core leaks in both ways at nearly every delay tested. A check on the routed netlist confirms that the lock-step and staggered cores share no cells across their share domains, isolating synthesis-level sharing as a separate risk; silicon validation is left to future work.
