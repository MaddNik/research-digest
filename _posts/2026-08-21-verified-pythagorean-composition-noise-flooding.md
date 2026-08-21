---
title: "Verified Pythagorean Composition for Adaptive Cryptographic Games: Noise Flooding in Homomorphic Encryption"
date: 2026-08-21 08:17:00 +0200
categories: [FHE]
tags: [noise-flooding, formal-verification, ckks, security-proofs]
link: https://eprint.iacr.org/2026/1671
byline: "Yi Lee et al. (IACR ePrint 2026/1671, Aug 13 2026)"
description: "A machine-checked security proof, formalized in Rocq and SSProve, tightens the composition bound for the noise-flooding defense used in approximate CKKS-style homomorphic encryption."
---

Noise flooding is a standard countermeasure against decryption attacks on approximate homomorphic encryption, but the authors note its security proof is unusually sensitive to how repeated adaptive decryption queries are composed: a naive hybrid argument loses security linearly in the number of queries, q. They present a proof technique that instead accumulates conditional Kullback-Leibler divergence costs across queries and converts to statistical distance only once, yielding a bound whose loss grows with the square root of q rather than linearly. This argument is formally verified using the Rocq proof assistant together with the SSProve framework: for any fully homomorphic encryption scheme that is approximately correct and IND-CPA secure, they formalize a reduction for adaptive adversaries making q queries and prove the resulting security bound. The technical core is a new relational program logic over SSProve semantics, described as having a Pythagorean judgment that composes conditional KL budgets without an intermediate conversion to statistical distance, plus a verified trace compiler that lifts a local oracle rule to arbitrary adaptive programs. The paper is about formal verification of a security proof technique rather than a new encryption scheme or implementation.
