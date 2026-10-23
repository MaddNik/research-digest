---
title: "Power Analysis on SQIsign via Ideal Reconstruction from Quaternion Leakages"
date: 2026-10-23 08:30:00 +0200
categories: [Hardware Security]
tags: [sqisign, power-analysis, isogeny-cryptography, side-channel-attack]
link: https://eprint.iacr.org/2026/2508
byline: "Won Kim et al. (IACR ePrint 2026/2508, Oct 17 2026)"
description: "The first side-channel analysis of Round-3 SQIsign identifies five vulnerabilities in its signing procedure, with polynomial-time key-recovery algorithms and a demonstrated power analysis attack extracting the needed leakage from the SQIsign source code."
---

SQIsign is an isogeny-based signature scheme and a Round-3 candidate in NIST's additional post-quantum digital signature standardization, for which NIST considers side-channel resistance an important evaluation factor, yet side-channel analysis of SQIsign has remained very limited, with prior studies targeting only the substantially different Round-1 version or relying on toy parameters and assumed, undemonstrated leakage. This work identifies five side-channel vulnerabilities in the signing procedure of Round-3 SQIsign and provides polynomial-time algebraic algorithms that recover the secret key from the corresponding leaked intermediate values, along with algorithms for reconstructing the complete secret key even when the leakage reveals only partial bits of an algebraic value. The authors further perform a power analysis attack on the SQIsign source code, successfully extracting the necessary leakage, or its partial information, for each of the five identified vulnerabilities, establishing concrete, implementation-level side-channel risks for the current version of SQIsign.
