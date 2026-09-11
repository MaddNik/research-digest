---
title: "Dynasaurs: Efficient Universal Dynamic zkSNARKs from Sparse Linear Arguments"
date: 2026-09-11 08:23:00 +0200
categories: [Cryptography]
tags: [zksnarks, sparse-arguments, plonk, r1cs]
link: https://eprint.iacr.org/2026/1892
byline: "Marti Batista et al. (IACR ePrint 2026/1892, Sep 4 2026)"
description: "Dynasaurs builds universal dynamic zkSNARKs that update a proof in time proportional to how much the witness changes, using at most 20 group elements and 23 pairings, over six times fewer than the prior state of the art."
---

Dynamic zkSNARKs extend standard zkSNARKs with an update algorithm that adapts a proof to a new statement in time sublinear in circuit size when only a few witness positions change, but existing universal constructions require sending over 130 group elements and more than 180 pairings. The authors build a sparse zkSNARK for linear relations from a fully witness-dependent argument together with a rational encoding of the constraint matrices, addressing a witness-independent bottleneck in the standard approach to proving general linear relations. They then develop a compiler that turns any sparse argument for a linear relation into a dynamic one while preserving zero-knowledge. Instantiated for Plonk and R1CS-lite, their techniques produce universal dynamic zkSNARKs with at most 20 group elements per proof and 23 verifier pairings, more than 6.5 and 7.8 times fewer than the state of the art, along with asymptotically faster updates.
