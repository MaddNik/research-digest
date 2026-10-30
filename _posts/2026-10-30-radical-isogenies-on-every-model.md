---
title: "Radical isogenies on every model"
date: 2026-10-30 08:10:00 +0200
categories: [PQC]
tags: [isogeny-based-cryptography, radical-isogenies, csidh, elliptic-curve-models]
link: https://eprint.iacr.org/2026/2661
byline: "Thomas Decru (IACR ePrint 2026/2661, Oct 27 2026)"
description: "A model-independent derivation of radical isogeny formulas gives explicit, inversion-free chain-of-isogeny computations of every odd degree directly on short Weierstrass, Montgomery, twisted Edwards, and several other common elliptic curve models."
---

Radical isogeny formulas compute a cyclic chain of N-isogenies using one Nth root per step without sampling torsion points, but for general N they were previously known only in Tate normal form. This paper gives radical steps of every odd degree N directly on short Weierstrass, Montgomery, twisted Edwards, Huff, extended Jacobi quartic, twisted Hessian, Legendre, and Jacobi intersection curves, on Kummer lines, and on all curves with a rational point of order 2, using a model-independent approach that recovers the codomain without taking additional square roots. The work lowers the cost of a radical isogeny step in Tate normal form from 12.5N to 10N multiplications plus one exponentiation, with short Weierstrass curves close behind at 10N+35 multiplications, while Montgomery and twisted Edwards curves cost 10.5N+O(1) multiplications but are cheapest, at 2N multiplications, for pushing a point through a step when transporting torsion points along chains with N of 19 or higher. All algorithms given are inversion-free with exact operation counts, extending the practical toolkit for isogeny-based schemes such as CSIDH.
