---
title: "Exploring Fault Injection Attacks on HQC and BIKE Beyond Fujisaki-Okamoto Verification"
date: 2026-10-16 08:29:00 +0200
categories: [Hardware Security]
tags: [fault-injection, hqc, bike, code-based-kem]
link: https://eprint.iacr.org/2026/2492
byline: "Thales B. Paiva et al. (IACR ePrint 2026/2492, Oct 15 2026)"
description: "New laser fault injection attacks target instructions inside HQC and BIKE decapsulation outside the Fujisaki-Okamoto transform, achieving full key recovery with valid ciphertexts and experimentally validated on an STM32H7 microcontroller."
---

Fault injection attacks on post-quantum code-based key encapsulation mechanisms have mostly focused on faults that target the Fujisaki-Okamoto transform, but this work presents new fault injection attacks against BIKE and HQC that instead target less obvious instructions elsewhere in the decapsulation process. The proposed attacks achieve full key recovery using only valid ciphertexts under NIST Level 1 parameters, requiring 17,392 decapsulation queries for HQC and roughly 3 million for BIKE. The authors also introduce a general methodology for identifying effective fault locations by analyzing decoder behavior under perturbed conditions, broadening the known attack surface for these schemes beyond the Fujisaki-Okamoto-centric analyses common in prior work. The attacks are experimentally validated on an STM32H7 microcontroller using laser fault injection, demonstrating high repeatability and providing a foundation for more efficient fault attack analyses on code-based KEMs going forward.
