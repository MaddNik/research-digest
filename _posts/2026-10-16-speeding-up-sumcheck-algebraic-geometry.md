---
title: "Speeding up Sumcheck using Algebraic Geometry"
date: 2026-10-16 08:22:00 +0200
categories: [Cryptography]
tags: [sumcheck-protocol, algebraic-geometry-codes, zero-knowledge-proofs, binary-fields]
link: https://eprint.iacr.org/2026/2494
byline: "Rahul Dalal et al. (IACR ePrint 2026/2494, Oct 15 2026)"
description: "A new binary-preserving multiplication code built from a genus-95 curve over the binary field shrinks the most expensive round of the sumcheck protocol by more than three times for proof systems over binary fields."
---

The sumcheck protocol is a ubiquitous component of modern proof systems for proving the sum of evaluations of a low-degree multivariate polynomial, and while it has been generalized in theory to any multiplication code, practical systems still use polynomials, which costs proof systems over binary fields targeting Boolean circuits because the Reed-Solomon product of two binary messages is no longer binary. The authors present a new concrete multiplication code based on algebraic geometry that is binary-preserving, meaning the product of two encoded binary messages stays binary, constructing an explicit code over the field with 2 to the power 128 elements that carries 64-bit messages to binary product messages of length 222, with relative distance greater than 1 minus 2 to the power negative 119. The part of the product message the prover actually sends in sumcheck shrinks by more than three times compared with Reed-Solomon as used in practice, and the code is derived from a genus-95 curve over the binary field with 64 rational points, built as an Artin-Schreier cover of a genus-4 curve. The authors implemented the resulting protocol, called the AG skip, inside the Flock proof system, and for 2 to the power 32 constraints it speeds up the skip round by 2.36 times and the whole zerocheck, the prover's most expensive component, by 1.65 times.
