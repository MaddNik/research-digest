---
title: "Arion: Arithmetization-Oriented Hashing for Zero-Knowledge Proof Systems"
date: 2026-09-04 08:23:00 +0200
categories: [Cryptography]
tags: [arithmetization-oriented-hashing, zero-knowledge, groebner-basis, plonk]
link: https://eprint.iacr.org/2026/1842
byline: "Luca Campa et al. (IACR ePrint 2026/1842, Aug 31 2026, published in TOSC 2026)"
description: "Arion is a new arithmetization-oriented hash function whose security analysis is grounded in the quotient ring dimension of the underlying algebraic ideal, and which is frequently the fastest design in the Plonk setting among compared hash functions."
---

The authors propose Arion, an arithmetization-oriented hash function built from a new permutation, Arion-pi, over a prime field, based on a recently introduced algebraic framework called the generalized triangular polynomial system for constructing cryptographic permutations from polynomials over finite fields. Arion is defined in both a standard Sponge construction and a feed-forward truncation mode, with secure parameter sets specified for prime fields commonly used in zero-knowledge applications, including the scalar fields of BLS12-381 and BN254. The security analysis relies heavily on algebraic techniques such as interpolation, polynomial system solving, Groebner basis computations, and resultants, and the authors say Arion is the first hash function whose security analysis is explicitly grounded in the algebraic invariant of the underlying ideal, the quotient ring dimension, determining this dimension for the CICO problem induced by both hashing modes for any threshold t. Benchmarked across R1CS, Plonk, and AIR arithmetization frameworks against Poseidon, Poseidon2, Anemoi, Griffin, and Rescue, Arion is frequently the best-performing design in the Plonk setting, remains competitive in R1CS and AIR, and is the only high-degree power-map-based construction that matches Poseidon and Poseidon2 on native evaluation performance. The work was published by the IACR in TOSC 2026.
