---
title: "Twisted Towers: A Faster and Fully Costed SexTNFS Attack"
date: 2026-11-13 08:27:00 +0200
categories: [Cryptography]
tags: [discrete-logarithm, number-field-sieve, pairing-based-cryptography, bls12-381]
link: https://eprint.iacr.org/2026/2831
byline: "Gautam Botrel (IACR ePrint 2026/2831, Nov 8 2026)"
description: "A fully instruction-costed redesign of the Special exTNFS attack on BLS12-381's target group yields a small estimated cost improvement over the published attack design, without changing the practical security of the curve."
---

The author studies the Special exTNFS attack on discrete logarithms in the target group of the BLS12-381 pairing-friendly curve, giving a design in which every step, including relation collection, cofactorization, filtering, linear algebra, the Block Wiedemann generator, and individual logarithms, is priced in one instruction-level cost model, with success probability of at least 0.39. The design rests on an explicit twisted tower construction built from an involution and a unit on the sextic base field, which acts as a cube of the Frobenius map and lets relations and ideals come in orbits of four, reducing the linear system and requiring only ten Schirokauer maps, with a norm-2 element of the base field enabling a coset sieve. The author also observes that prior yield estimates over the relevant coefficient cubes counted unit multiples as distinct relations, when in fact only about 1 in 7 of the smoothness-weighted cube points give distinct relations for the valid polynomial pair closest to the published BLS12-381 design. Under stated heuristics, the ledger comes to about 2 to the power of 115.72 dense field-multiplication equivalents, roughly 2 to the power of 130 processor instructions, with the new design estimated to cost about 0.8 bit less than a fundamental-domain version of the published design, though the comparison ranges from 0.57 bit in its favor to 0.19 bit against depending on the cost model used. The author stresses that nothing was run at full size and that the practical security of BLS12-381 is unchanged.
