---
title: "An improved algorithm to solve the isogeny problem in dimension 2 with precomputation"
date: 2026-11-13 08:15:00 +0200
categories: [PQC]
tags: [isogeny-cryptography, cryptanalysis, abelian-surfaces]
link: https://eprint.iacr.org/2026/2808
byline: "Maria Corte-Real Santos (IACR ePrint 2026/2808, Nov 6 2026)"
description: "A new unconditional algorithm solves the superspecial isogeny problem in dimension 2 faster than the Costello-Smith algorithm after a one-time precomputation that depends only on the prime p."
---

The author gives a new algorithm for the superspecial isogeny problem in dimension 2. After a one-time precomputation depending only on the prime p, which succeeds with overwhelming probability, each individual instance is solved in expected time and memory on the order of p to the power of 3 over 4. This result is unconditional and relies on no heuristics. Including the cost of the precomputation, a single instance is solved in time on the order of p to the power of 19 over 23, improving on the order of p of the Costello-Smith algorithm, and the improvement holds even using the same memory as the rigorous version of that algorithm. The key ingredient is an algorithm that computes the equations of certain Humbert surfaces modulo p for a growing range of parameters, giving a membership test for optimally split surfaces that is evaluated in batches using fast multipoint evaluation, which speeds up the main bottleneck of the Costello-Smith algorithm: finding an isogeny from a superspecial principally polarized abelian surface to a product of supersingular elliptic curves.
