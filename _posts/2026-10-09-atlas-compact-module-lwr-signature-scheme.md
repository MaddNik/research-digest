---
title: "ATLAS: A Compact Module-LWR Signature Scheme"
date: 2026-10-09 08:12:00 +0200
categories: [PQC]
tags: [module-lwr, fiat-shamir-with-aborts, lattice-signatures]
link: https://eprint.iacr.org/2026/2323
byline: "Karthick Srivatsan et al. (IACR ePrint 2026/2323, Oct 3 2026)"
description: "ATLAS is a new Fiat-Shamir-with-aborts lattice signature scheme based on Module Learning with Rounding that removes the explicit noise term used by Dilithium and HAETAE."
---

ATLAS is a lattice-based digital signature scheme built on the Fiat-Shamir with aborts paradigm, with security based on the hardness of the Module Learning with Rounding (MLWR) problem. Unlike Dilithium's construction or HAETAE's bimodal instantiation, ATLAS derives its public key through deterministic rounding, eliminating the error term and the explicit noise sampling it requires, which reduces key-generation cost and secret-key storage while keeping the scheme structurally close to Dilithium's well-studied design. ATLAS targets 128, 256, and 512-bit classical security levels, including what the authors describe as the first MLWR-based signature parameter set at the 512-bit level, and adopts power-of-two moduli that replace modular reduction with bitwise operations and remove rejection sampling from key parts of the scheme. Since power-of-two moduli preclude conventional NTT-based multiplication, the authors design a hierarchical Toom-Cook and Karatsuba decomposition accelerated with AVX2 vectorization, and the scheme supports both SHAKE and KDF-SM3 as interchangeable symmetric back-ends.
