---
title: "Top Gun: Degree Annihilation Attacks on Poseidon"
date: 2026-06-17 08:24:00 +0200
categories: [Cryptography]
tags: [cryptanalysis, zero-knowledge, hash-functions, algebraic-attacks]
link: https://eprint.iacr.org/2026/1254
byline: "Antonio Sanso et al. (IACR ePrint 2026/1254, Jun 14 2026)"
description: "A new algebraic-cryptanalysis framework that lowers the effective degree of Poseidon's polynomial systems by forcing dominant degree terms to vanish."
---

Poseidon is one of the most widely deployed arithmetization-oriented permutations
and is central to many zero-knowledge proof systems, so the difficulty of
controlling polynomial degree growth has been a key barrier to algebraic attacks.
This work introduces degree annihilation, which, unlike round-skipping techniques
that remove rounds from the algebraic model, instead imposes algebraic constraints
that force dominant degree contributions of existing rounds to vanish, yielding
polynomial systems of substantially lower effective degree. The authors present a
simple bivariate form that combines naturally with classical round-skipping, where
the gain depends on how the annihilated contribution propagates through the
remaining nonlinear layers; when this multiplicity matches one S-box layer, the
effect equals skipping an additional nonlinear layer. They then generalize to
multivariate settings, using systems of control equations to annihilate successive
partial-round degree contributions, solved via elimination, resultants, and Groebner
basis techniques. As a proof of concept they apply the framework to reduced-round
Poseidon instances. The recommended full-round parameter sets remain intact.
