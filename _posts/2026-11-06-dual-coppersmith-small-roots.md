---
title: "Dual Coppersmith: Finding Small Roots Without Multivariate Polynomial Systems"
date: 2026-11-06 08:27:00 +0200
categories: [Cryptography]
tags: [coppersmith-method, lattice-reduction, small-roots, public-key-cryptanalysis]
link: https://eprint.iacr.org/2026/2740
byline: "Taehun Kang et al. (IACR ePrint 2026/2740, Nov 3 2026)"
description: "Dual Coppersmith replaces the algebraic root-recovery stage of Coppersmith's method with geometric recovery from a lattice, avoiding the exponential worst case of solving auxiliary polynomial systems."
---

The multivariate Coppersmith algorithm is a central tool for finding small hidden roots of modular polynomial equations in public-key cryptanalysis, normally working in two stages: a lattice-reduction stage that builds auxiliary integer equations satisfied by the hidden root, and a root-recovery stage that solves them, which can take exponential time even when the first stage succeeds. This paper introduces Dual Coppersmith, which replaces the algebraic root-recovery stage with geometric recovery from a modular orthogonal lattice by embedding the hidden root as a short lattice vector; the authors prove that the LLL lattice-reduction algorithm recovers the vector's direction whenever a sufficient gap separates it from other independent lattice vectors, after which the root is read off directly from coordinate ratios. To analyze this gap, they propose a heuristic model for the lattice's second successive minimum, examining both the full lattice and a structured sublattice, and show that under this model Dual Coppersmith matches the standard Coppersmith product-size bound without ever solving an auxiliary polynomial system. Experiments on the approximate common divisor problem and the Herrmann-May problem support the model's predictions and show root recovery in higher-dimensional instances where a Grobner-basis baseline times out.
