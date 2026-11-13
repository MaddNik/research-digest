---
title: "Homomorphism in Expectation: Leveled Homomorphic Encryption with Range-Relative Correctness"
date: 2026-11-13 08:18:00 +0200
categories: [FHE]
tags: [leveled-fhe, encoding, arithmetic-circuits]
link: https://eprint.iacr.org/2026/2854
byline: "Zeyu Liu et al. (IACR ePrint 2026/2854, Nov 10 2026)"
description: "The authors show that encrypted addition alone suffices for both addition and multiplication in deep real-valued homomorphic computation, building leveled homomorphic encryption from any additively homomorphic scheme over the integers modulo 2."
---

Lattice-based schemes have dominated the development of homomorphic encryption for deep computation, but this work introduces Homomorphism in Expectation, a construction showing that encrypted addition suffices for both addition and multiplication in deep real-valued computation. Given any additively homomorphic encryption scheme over the integers modulo 2, the authors construct range-relatively correct leveled homomorphic encryption for arithmetic circuits of arbitrary polynomial depth, where for a chosen depth bound and input bound the scheme supports inputs in a symmetric range and outputs bounded by the circuit's maximum output magnitude over that range, with decryption returning an answer within a bounded error except with some small failure probability. The construction begins by encoding real-valued inputs as encrypted bitstreams, which allows multiplication through encrypted bit addition, but the direct approach incurs costs exponential in circuit depth and is limited to logarithmic depth with non-compact ciphertexts. The authors overcome this with new encoding and circuit evaluation techniques that eliminate the exponential overhead, enabling compact homomorphic arithmetic at arbitrary polynomial depth from additive encryption alone.
