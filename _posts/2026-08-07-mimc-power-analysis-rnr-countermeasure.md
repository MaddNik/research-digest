---
title: "Power Analysis and Countermeasures on the MiMC Block Cipher"
date: 2026-08-07 08:28:00 +0200
categories: [Hardware Security]
tags: [side-channel, power-analysis, masking]
link: https://eprint.iacr.org/2026/1562
byline: "Elena Andreeva et al. (IACR ePrint 2026/1562, Jul 30 2026)"
description: "The paper presents profiled and unprofiled power analysis attacks on the MiMC arithmetization-oriented block cipher and compares masking against a redundant number representation countermeasure."
---

MiMC is an arithmetization-oriented block cipher used in zero-knowledge, fully homomorphic encryption, and multi-party computation protocols, and the authors examine its side-channel security on ARM Cortex-M4 and x86 platforms. An unprofiled linear-regression attack reduces the key-guessing space to about 2 to the 30th power candidates using roughly 32000 power measurements, while a profiled attack achieves full key recovery with as few as 100 measurements. To defend against this, the authors compare classical ISW masking with a redundant number representation adapted to large prime fields, finding that about 64 bits of redundancy is enough to make differential power analysis attacks impractical. The redundant number representation approach adds only about 50 percent performance overhead on both platforms, compared to about 8.3 times overhead for masking on Cortex-M4 and about 81 times on x86-64. The results are supported by leakage assessment over 10 million traces and by SASCA-based quantitative analysis.
