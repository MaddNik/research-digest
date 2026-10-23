---
title: "SLEEK: Sparse Quasi-Cyclic Codes with Closed-Form DFR Key Encapsulation"
date: 2026-10-23 08:13:00 +0200
categories: [PQC]
tags: [code-based-cryptography, qc-mdpc, key-encapsulation, decoding-failure-rate]
link: https://eprint.iacr.org/2026/2512
byline: "Alessandro Annechini et al. (IACR ePrint 2026/2512, Oct 16 2026)"
description: "SLEEK is a new QC-MDPC-based key encapsulation mechanism with a closed-form decoding-failure-rate estimate that produces ciphertexts 4.9 times smaller than NIST's HQC standard for long-term keys, at a 47 percent runtime cost."
---

Bandwidth, execution time, and decoding failures remain important challenges for code-based key encapsulation mechanisms (KEMs). The authors introduce SLEEK, a KEM based on Quasi-Cyclic Moderate-Density Parity-Check (QC-MDPC) codes that uses a parallel bit-flipping decoder with three iterations and a closed-form estimate of the decoding-failure rate, enabling parameter selection with analytically bounded failure probability and compatibility with standard IND-CCA transformations. Two variants are designed: SLEEK-LT targets IND-CCA security for long-term keys and supports QC-MDPC codes of different rates to trade off public-key and ciphertext size, while SLEEK-E targets IND-CPA security for ephemeral keys with forward secrecy using a novel QC key structure whose security is shown equivalent to the original QC-MDPC construction while reducing key-generation cost. The authors provide parameter sets for 128-, 192-, and 256-bit security plus an 80-bit configuration for constrained embedded platforms, and an optimized AVX2 implementation shows that SLEEK-LT ciphertexts are 4.9 times smaller than NIST-standard HQC at the cost of a 47 percent runtime increase, while being 1.3 to 2.7 times faster than BIKE. SLEEK-E improves execution time by 1.6 times over HQC with 2.1 times less bandwidth usage, and is 5.3 times faster than Lean-BIKE while substantially reducing the impact of decoding failures on reliability.
