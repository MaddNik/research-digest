---
title: "Area-Efficient Hardware Architecture of the Post-Quantum HQC Cryptosystem with Side-Channel Protection"
date: 2026-10-09 08:32:00 +0200
categories: [Hardware Security]
tags: [hqc, side-channel-countermeasure, fpga]
link: https://eprint.iacr.org/2026/2359
byline: "Kamal Raj et al. (IACR ePrint 2026/2359, Oct 5 2026)"
description: "A constant-time HQC hardware design reuses idle KECCAK logic to scramble secret-dependent power during decoding, suppressing side-channel leakage at less than 0.5 percent area overhead."
---

HQC is the post-quantum key-encapsulation mechanism recently selected by NIST for standardization as an alternative KEM candidate, but prior studies show its physical implementations remain vulnerable to power-based side-channel attacks, and the usual masking and shuffling countermeasures add significant hardware resources and performance overhead. The authors present a resource-efficient, constant-time hardware architecture for HQC that uses a novel idle-hardware reuse strategy as a side-channel countermeasure, intentionally reusing the existing KECCAK hardware to generate dynamic power during decoding and scramble secret-dependent power correlations, adding less than 0.5 percent area overhead for the countermeasure logic. The fully parameterized design supports all three NIST security categories, HQC-128, HQC-192, and HQC-256, and a prototype on an Artix-7 FPGA reaches a maximum clock frequency of 139 megahertz while using 11,489 LUTs, 6,785 flip-flops, and 4 DSPs. Functional correctness is verified with NIST known-answer tests across key generation, encapsulation, and decapsulation, and test vector leakage assessment confirms significant suppression of side-channel leakage.
