---
title: "A Single-Trace Side-Channel Attack on the KpqC Digital Signature Scheme AIMer v3"
date: 2026-11-13 08:32:00 +0200
categories: [Hardware Security]
tags: [side-channel, aimer, mpc-in-the-head, power-analysis]
link: https://eprint.iacr.org/2026/2859
byline: "Jinnuo Li et al. (IACR ePrint 2026/2859, Nov 10 2026)"
description: "A deep-learning-based single-trace power analysis attack recovers the full secret key of AIMer v3, a finalist in the Korean post-quantum cryptography competition, from a single signature with 100 percent success."
---

The Korean Post-Quantum Cryptography competition selected AIMer, a post-quantum digital signature scheme based on the MPC-in-the-Head paradigm, as one of its final algorithms in 2025, but the authors note that detailed side-channel analysis of AIMer remains limited, particularly for its latest version, AIMer v3. This paper presents, to the authors' knowledge, the first side-channel attack on AIMer v3, demonstrating a single-trace power analysis attack using deep learning that exploits power leakage from bits of the secret preimage during the computation of AIM3's input affine layer. Using a ChipWhisperer-HuskyPlus setup, the authors recover the full secret key from a single signature on an ARM Cortex-M4 processor with a success rate of 100 percent. They further evaluate the attack's performance under different noise levels and propose potential countermeasures.
