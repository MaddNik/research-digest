---
title: "Correlation Power Analysis on SHA-2-Based SLH-DSA"
date: 2026-11-06 08:31:00 +0200
categories: [Hardware Security]
tags: [slh-dsa, correlation-power-analysis, hash-based-signatures, side-channel]
link: https://eprint.iacr.org/2026/2753
byline: "Jinwook Chang et al. (IACR ePrint 2026/2753, Nov 4 2026)"
description: "Non-profiled correlation power analysis recovers secret portions of the address-based pseudorandom function in all six SHA-2 parameter sets of the SLH-DSA hash-based signature scheme."
---

SLH-DSA repeatedly processes a fixed secret seed together with varying public addresses through its address-based pseudorandom function, making that function a natural side-channel target. This paper presents non-profiled correlation power analysis against all six SHA-2 parameter sets of SLH-DSA, using separate recovery paths through the SHA-256 compression rounds and the message-schedule expansion, and accounting for the specific input layout in which a 22-byte compressed address precedes the secret seed. For the 256-bit parameter sets, a two-stage joint procedure recovers two 16-bit secret portions. Evaluated on an STM32F303 Cortex-M4 implementation using 30 secret seeds and 5,000 power traces per seed per condition, the compression-round attack achieves 100 percent success under both tested addressing schemes, and message-schedule recovery also reaches 100 percent for the 128-bit and 192-bit parameter sets; for the two 256-bit variants, joint recovery reaches 100 percent while recovery of individual message words ranges from 66.7 to 80 percent. The results show that side-channel protection for SLH-DSA implementations must cover both the compression rounds and the message-schedule expansion, not just one or the other.
