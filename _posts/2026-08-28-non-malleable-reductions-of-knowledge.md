---
title: "Non-Malleable Reductions of Knowledge"
date: 2026-08-28 08:22:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, simulation-extractability, lattice-based-proofs, fiat-shamir]
link: https://eprint.iacr.org/2026/1822
byline: "Antonio Faonio and Lili Tong (IACR ePrint 2026/1822, Aug 27 2026)"
description: "A modular framework for non-malleable reductions of knowledge identifies when composing Fiat-Shamir proof systems preserves simulation extractability, and applies it to give the first non-malleability analysis of LaBRADOR."
---

Non-malleability for non-interactive zero-knowledge proofs requires that, given a proof for one statement, it is infeasible to derive a valid proof for a related statement without knowing a corresponding witness. The authors introduce a modular framework for analyzing non-malleable reductions of knowledge, which transform the task of proving knowledge for a source relation into proving knowledge for a simpler or more structured target relation, and identify settings in which composing two such reductions, particularly two obtained via the Fiat-Shamir transform, preserves simulation extractability and therefore non-malleability. Their framework isolates concrete properties required from each component, including new forms of zero knowledge that are easier to verify than full simulation extractability. They illustrate the approach on LaBRADOR, a lattice-based proof system for R1CS from CRYPTO 2023, providing the first simulation-extractability analysis of the scheme and, since LaBRADOR itself is not zero knowledge, designing a zero-knowledge variant that preserves its practical efficiency and sublinear proof size. The paper is published at Asiacrypt 2026.
