---
title: "Keyber: Recovering the Signal by Amplifying the Noise in ML-KEM"
date: 2026-11-06 08:29:00 +0200
categories: [Hardware Security]
tags: [ml-kem, fault-attack, statistical-ineffective-fault-attack, key-generation]
link: https://eprint.iacr.org/2026/2766
byline: "Vipin Kumar et al. (IACR ePrint 2026/2766, Nov 4 2026)"
description: "Keyber is the first statistical ineffective fault attack on ML-KEM key generation, recovering the full secret key from a single fault using up to 30,000 decapsulation-failure inequalities."
---

ML-KEM, standardized as FIPS 203, is being deployed to resist adversaries with quantum computers, but fault attacks against it have so far focused only on decapsulation, leaving its key generation step largely unexamined. This paper presents Keyber, the first statistical ineffective fault attack on ML-KEM key generation, which needs only a single fault that adds a known value to the error vector during key generation, leaving the public matrix seed intact so every subsequent decapsulation carries a known induced error. The adversary encapsulates locally, keeps only ciphertexts whose induced error peaks at exactly one coefficient, and attributes decapsulation failures to that coefficient, with each useful query yielding one linear inequality on the secret key and requiring no further faults. The authors observe that roughly 0.2 to 27 percent of encapsulations are usable depending on the ML-KEM parameter set, with the full secret key recoverable using up to 30,000 inequalities across all security levels, and they demonstrate the attack end to end on ML-KEM-512 running on an ARM Cortex-M4 using a single over-clock fault. Because key generation happens only once per key's lifetime, a single successful fault during that one-time operation compromises the key permanently, showing that ML-KEM implementations must harden key generation as well as decapsulation.
