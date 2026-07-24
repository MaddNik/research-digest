---
title: "Power Reveals Timing Conceals - Side-Channel Attacks and Hiding Countermeasures for HQC's Fixed-Weight Vector Sampling"
date: 2026-07-24 08:09:00 +0200
categories: [PQC]
tags: [hqc, side-channel-attack, fixed-weight-sampling, countermeasures]
link: https://eprint.iacr.org/2026/1462
byline: "Dina Hesse et al. (IACR ePrint 2026/1462, Jul 17 2026)"
description: "Power side-channel attacks against the fixed-weight vector sampling step of the code-based scheme HQC recover the secret key with a 100 percent success rate, and the paper evaluates hiding countermeasures needed to stop them."
---

This paper targets the fixed-weight vector sampling procedure used in HQC, a code-based post-quantum encryption scheme. The authors present two practical attacks: a power-based distinguisher that recovers the key with a 100 percent success rate using 900,000 distinguisher calls, and a separate single-trace attack effective even against masked implementations. They then evaluate hiding countermeasures, including dummy operations, bitslicing, and shuffling, to see whether these mitigate the leakage. The paper concludes that hiding alone is insufficient and that a combination of masking and hiding is required to effectively protect real implementations of HQC's sampling step.
