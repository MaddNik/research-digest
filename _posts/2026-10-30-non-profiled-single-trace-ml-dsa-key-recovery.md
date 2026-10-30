---
title: "Non-profiled Single-Trace ML-DSA Secret Key Recovery by Horizontal Distribution Analysis"
date: 2026-10-30 08:35:00 +0200
categories: [Hardware Security]
tags: [ml-dsa, single-trace-attack, side-channel-analysis, horizontal-attack]
link: https://eprint.iacr.org/2026/2643
byline: "Linus Backlund and Elena Dubrova (IACR ePrint 2026/2643, Oct 26 2026)"
description: "A non-profiled horizontal side-channel attack compares observed trace distributions against expected Hamming weight leakage using a Gaussian mixture model, recovering the full ML-DSA-65 secret key from a single trace in 99 percent of attempts on an ARM Cortex-M4."
---

Single-trace side-channel attacks on cryptographic implementations have mostly relied on profiled methods that assume the attacker has a clone device and implementation knowledge to build a leakage model before attacking, but this paper shows that a much weaker, non-profiling adversary can still mount powerful single-trace attacks. The method compares the observed sample distribution against the expected Hamming weight leakage distribution using a Gaussian mixture model as a distinguisher, and its horizontal nature lets the attacker obtain multiple observations per execution by partitioning and stacking a single trace. The authors show how to select optimal trace preprocessing parameters and configure the measurement setup to lower the noise floor, enabling exploitation of weak leakage, and they prove that imperfect classifications can be efficiently corrected using information-set decoding algorithms. Evaluated on an optimized ML-DSA-65 implementation on ARM Cortex-M4 targeting the secret key unpacking procedure, the method recovers the full secret key from a single trace in 99 percent of attacks with an enumeration budget of 2 to the 70 operations.
