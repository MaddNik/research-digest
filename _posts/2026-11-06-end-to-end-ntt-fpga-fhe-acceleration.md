---
title: "End-to-End NTT on FPGA for FHE Acceleration"
date: 2026-11-06 08:17:00 +0200
categories: [FHE]
tags: [ntt, fpga-acceleration, lattigo, fhe-fpga]
link: https://arxiv.org/abs/2611.03325
byline: "Mohamed Allam et al. (arXiv:2611.03325, Nov 2 2026)"
description: "A fully unrolled FPGA NTT kernel spanning three dies of an AMD Alveo V80 speeds up end-to-end FHE key switching and bootstrapping by up to 2.2 times."
---

In FHE-based deep learning inference, roughly 63 percent of CPU time goes to the number theoretic transform and its inverse, which reduce polynomial multiplication complexity from O(N squared) to O(N log N). Prior FPGA accelerators either speed up entire FHE schemes at the cost of being tied to specific parameters, or accelerate only the NTT with interconnects that grow with parallelism and complicate routing on multi-die FPGAs; end-to-end NTT acceleration inside a full FHE pipeline had not previously been explored. This paper designs a fully unrolled, delay-commutator streaming NTT and inverse-NTT kernel and floorplans it across the three dies of an AMD Alveo V80 FPGA. At 400 megahertz, the kernel transforms a polynomial of 65,536 coefficients every 5.12 microseconds, the highest throughput reported among FPGA designs at this size, and is up to 22 times faster than a CPU per transform when offloaded end to end. Integrated into the Lattigo FHE library with 128-bit secure parameters, it accelerates core FHE operations such as key switching and bootstrapping by 1.8 to 2.2 times, and neural network inference by 1.8 to 2.1 times.
