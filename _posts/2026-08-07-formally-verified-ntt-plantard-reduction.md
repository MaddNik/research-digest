---
title: "Code Generation of Faster Formally Verified NTT with Plantard Reduction"
date: 2026-08-07 08:06:00 +0200
categories: [PQC]
tags: [ml-kem, implementation, formal-verification]
link: https://eprint.iacr.org/2026/1624
byline: "Donnie Y. Xu et al. (IACR ePrint 2026/1624, Aug 6 2026)"
description: "A code generator produces formally verified implementations of the ML-KEM Number-Theoretic Transform using Plantard arithmetic, yielding 1.5 to 2.5 times performance gains over existing baselines."
---

This paper presents a formally verified implementation of the Number-Theoretic Transform (NTT) used in ML-KEM, the NIST-standardized lattice key encapsulation mechanism, based on Plantard modular reduction arithmetic. The implementation is produced through a code generator equipped with a static bound analyzer, and the authors provide generated implementations in both C and the Jasmin language, with the correctness of the arithmetic formally verified using the EasyCrypt proof assistant. The authors report that the generated implementations achieve performance improvements ranging from 1.5 times to 2.5 times over existing baseline implementations, with the exact gain depending on the specific operation and scheme being targeted. The work connects formal verification tooling directly to practical performance engineering for a component central to deployed post-quantum key exchange.
