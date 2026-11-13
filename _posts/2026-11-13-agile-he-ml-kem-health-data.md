---
title: "An Agile Homomorphic Encryption and ML-KEM Scheme for Privacy-Preserving Health Data Processing"
date: 2026-11-13 08:22:00 +0200
categories: [FHE]
tags: [bgv, ml-kem, crypto-agility, embedded-systems]
link: https://eprint.iacr.org/2026/2832
byline: "Daniel Resende, Nadia El Mrabet, Ulrich Kuhne (IACR ePrint 2026/2832, Nov 8 2026, LightSec 2026)"
description: "A proof-of-concept combines ML-KEM with the BGV homomorphic encryption scheme into an agile cryptographic scheme feasible for encrypted health data processing on embedded devices."
---

Storing and processing health data raises serious privacy concerns, so the data must be encrypted, and fully homomorphic encryption, which allows computation on encrypted data, is a promising technology for this setting even though FHE algorithms remain complex despite recent efficiency gains. The authors note that the security of several prominent FHE schemes rests on variants of the Learning With Errors problem, which is also the basis of ML-KEM, the new post-quantum standard for asymmetric encryption. Building on this shared foundation, they propose an agile cryptographic scheme that combines ML-KEM and the BGV homomorphic encryption scheme, targeting efficient implementation in an embedded use case. The paper describes the parameter selection for the proposed scheme and demonstrates its feasibility with a proof-of-concept implementation, published at LightSec 2026.
