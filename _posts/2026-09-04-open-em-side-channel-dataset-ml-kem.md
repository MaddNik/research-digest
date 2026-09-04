---
title: "Open EM Side-Channel Dataset for ML-KEM (Kyber) Implementations"
date: 2026-09-04 08:26:00 +0200
categories: [Hardware Security]
tags: [ml-kem, electromagnetic-side-channel, masking, open-dataset]
link: https://eprint.iacr.org/2026/1851
byline: "Alain Alyosha Magazin et al. (IACR ePrint 2026/1851, Sep 1 2026)"
description: "Ledger releases an open dataset of 200,000 electromagnetic traces per implementation for three ML-KEM (Kyber) decapsulation implementations on an STM32F407, including share-wise traces of a first-order masked variant."
---

The authors present an open dataset of electromagnetic traces captured during the decapsulation operation of ML-KEM (Kyber), the key encapsulation mechanism standardized by NIST in FIPS 203, with each trace windowed on a single pair-pointwise polynomial multiplication in which the decapsulation key is one operand, a recurring target of published side-channel key-recovery attacks. The dataset covers three widely used implementations, the CRYSTALS reference implementation, the Cortex-M4-optimized pqm4 implementation, and the first-order masked mkm4 implementation, with 200,000 traces per implementation captured on an STM32F407 Cortex-M4 microcontroller using a near-field electromagnetic probe. For the masked implementation the authors release traces of both shares, enabling first-order leakage assessment and share-wise analysis rather than attacks limited to unprotected code. Compared with previously published datasets of the same operation, which offered only power measurements of the unprotected reference implementation, this dataset adds an electromagnetic modality and covers both optimized and masked code, and it is distributed as chunked NumPy arrays with associated sensitive variables so researchers without measurement equipment can reproduce and extend side-channel analyses of ML-KEM.
