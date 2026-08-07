---
title: "Slipway: Accessing Finite Subspace Trails in Poseidon"
date: 2026-08-07 08:19:00 +0200
categories: [Cryptography]
tags: [cryptanalysis, algebraic-attack, zk-friendly-primitive]
link: https://eprint.iacr.org/2026/1579
byline: "Giuseppe Vitto (IACR ePrint 2026/1579, Aug 2 2026)"
description: "An algebraic cryptanalysis technique reaches previously inaccessible low-degree finite subspace trails inside the Poseidon permutation used in proof systems, sharply reducing its effective algebraic degree for a chosen instance."
---

Poseidon is an algebraic permutation widely used inside zero-knowledge proof systems, built from full and partial rounds of power-map S-boxes and MDS linear diffusion layers. The paper studies finite subspace trails, directions in the state space along which certain partial-round S-boxes add no algebraic degree, and addresses the open question of how a constrained input family can reach such a trail without first passing through full rounds that would normally raise its degree. By jointly constructing a constrained input family and a round-constant-dependent MDS matrix, the author shows the initial full rounds can act as a controlled reparametrization rather than a source of degree growth, a phenomenon called full-round absorption. For the KoalaBear Poseidon instance with parameters t equals 16, alpha equals 3, RF equals 8, RP equals 20, this yields output polynomials of exact degree 3 to the 10th power instead of the expected 3 to the 28th power, producing a complete CICO-2 solution for the full-round permutation using matrices that still satisfy Poseidon's own MDS design checks. The construction is generalized to CICO-k with corresponding trail-dimension and matrix-image bounds.
