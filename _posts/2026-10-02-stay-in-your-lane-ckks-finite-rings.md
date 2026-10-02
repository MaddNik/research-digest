---
title: "Stay in Your Lane: Fast Arithmetic over Large Finite Rings with CKKS"
date: 2026-10-02 08:18:00 +0200
categories: [FHE]
tags: [ckks, finite-rings, bootstrapping, polynomial-lanes]
link: https://eprint.iacr.org/2026/2190
byline: "Hyeongmin Choe, Robin Köstler, and Tim Seuré (IACR ePrint 2026/2190, Sep 26 2026)"
description: "By decomposing CKKS's polynomial ring into native lanes, a new bootstrapping method runs arithmetic over large finite rings and fields in under 4.5 seconds with far less overhead than prior encodings."
---

Recent CKKS-based constructions support homomorphic arithmetic modulo powers of two and more general moduli, and the authors explore a complementary tradeoff where using polynomial rings native to CKKS simplifies arithmetic and ciphertext refreshing but restricts the usable message spaces. Building on Kim's interpretation of GBFV ciphertexts as CKKS ciphertexts, they decompose the ring into N over n polynomial lanes, where each lane represents a message in a ring defined by a polynomial coprime to the cyclotomic polynomial, covering message spaces that include specific 128, 256, 512, and 1024-bit prime fields and extension fields such as F sub 5 to the 16th, F sub 17 to the 4th, and F sub 37 to the 32nd power. Unlike the triangle encoding used by Gao and Zheng's construction, these lanes occur at intermediate stages of the conventional CoeffToSlot and SlotToCoeff transformations, so the method avoids extra encoding-specific linear maps and performs arithmetic and refreshing entirely within CKKS-native polynomial rings. At a ring dimension of 2 to the 16th power, the arithmetic bootstrapping takes less than 4.5 seconds in every tested configuration, with little variation across the ring parameters, and arithmetic modulo 2 to the n power plus 1 is 2.2 to 3.8 times faster than Gao and Zheng's modulo 2 to the n power arithmetic for small n, with an estimated 26 times speedup at larger ring sizes where the comparison construction's memory use becomes prohibitive.
