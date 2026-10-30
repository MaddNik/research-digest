---
title: "Faster complete formulas and their application to curves with efficient endomorphisms"
date: 2026-10-30 08:26:00 +0200
categories: [Cryptography]
tags: [elliptic-curve-cryptography, scalar-multiplication, glv-endomorphisms, secp256k1]
link: https://eprint.iacr.org/2026/2667
byline: "Diego F. Aranha and Paulo L. Barreto (IACR ePrint 2026/2667, Oct 28 2026)"
description: "A new complete elliptic curve point addition formula using a 3D cross product reduces the cost from 12 to 11 multiplications, the first such improvement in 10 years, yielding a 5.2 percent speedup in libsecp256k1 and up to 14 percent faster pairing exponentiation."
---

This paper revisits scalar multiplication on prime curves of the form y squared equals x cubed plus b, a family that includes secp256k1, BN, and BLS curves. By applying a 15-year-old technique in a new way, the authors improve the best known complete point addition from 12 to 11 multiplications, or 10 for mixed coordinates, the first improvement of this kind in 10 years, since its final stage reduces to a 3D cross product needing only 5 multiplications. Implementing the new formulas in the libsecp256k1 library yields a 5.2 percent improvement in constant-time fixed-base scalar multiplication, and the authors also propose a complete tripling formula with the same cost as incomplete tripling in Jacobian coordinates, combined into an exception-free width-3 tau-NAF method that is about 14 percent faster than exception-free GLV-based scalar multiplication at 256 bits in an operation-count model. A constant-time implementation in the RELIC library confirms the model on BLS12-381, BLS24-509, and BLS48-575, with the tau-NAF method 9 to 13 percent faster than GLV with the same complete formulas in the first pairing group, and an imaginary version of Toom-Cook developed for the target group's extension field arithmetic gives a further 4 to 11 percent improvement in exponentiation there.
