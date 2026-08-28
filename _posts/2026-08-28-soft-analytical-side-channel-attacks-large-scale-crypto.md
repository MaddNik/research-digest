---
title: "Efficient Soft Analytical Side-Channel Attacks on Large-Scale Cryptographic Computations"
date: 2026-08-28 08:30:00 +0200
categories: [Hardware Security]
tags: [side-channel-attack, belief-propagation, ml-dsa, masked-implementations]
link: https://eprint.iacr.org/2026/1811
byline: "Yiteng Sun et al. (IACR ePrint 2026/1811, Aug 27 2026)"
description: "GRWP-SASCA makes soft analytical side-channel attacks practical on large-scale cryptographic computations such as the ML-DSA number theoretic transform by regionalizing and pruning the underlying factor graph."
---

Soft Analytical Side-Channel Attacks combine leakage-derived priors from multiple intermediate variables with belief propagation, but applying them to large-scale cryptographic computations produces factor graphs whose memory and computational cost become prohibitive, with standard SASCA requiring roughly 122 gigabytes of memory even for a 6-layer sub-component of the ML-DSA number theoretic transform. The authors propose Greedy Region-Wise Pruning SASCA, which replaces global belief propagation with a sequence of localized inference steps over incrementally merged regions, reducing search space via greedy pruning of redundant structures and low-confidence candidates. For unprotected ML-DSA, GRWP-SASCA reduces memory overhead for message propagation by up to a factor of 151 and achieves an estimated speedup of about 68 times compared to standard SASCA, and for d-order masked ML-DSA with multiple traces it achieves memory reductions and speedups that scale favorably with the masking order. Real-device experiments on an ARM Cortex-M4 platform recover the secret from an unprotected implementation within about 15 minutes using a single trace with peak memory usage of about 0.9 gigabytes, and recover a first-order masked ML-DSA secret within 3.2 hours using 8 traces with peak memory usage of about 8.1 gigabytes.
