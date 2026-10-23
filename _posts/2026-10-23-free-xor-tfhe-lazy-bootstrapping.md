---
title: "Free-XOR TFHE via Lazy Bootstrapping"
date: 2026-10-23 08:20:00 +0200
categories: [FHE]
tags: [tfhe, gate-bootstrapping, blind-rotation]
link: https://arxiv.org/abs/2610.29983
byline: "Ali Ajorian and Osman Biçer (arXiv:2610.29983, Oct 21 2026)"
description: "A new TFHE-style gate bootstrapping framework evaluates all 8 symmetric binary Boolean gates with only two blind rotations while still supporting free-XOR evaluation, simplifying a prior free-XOR construction."
---

Gate bootstrapping is central to FHEW-like fully homomorphic encryption schemes such as TFHE, letting Boolean gates be evaluated while simultaneously reducing ciphertext noise, but its cost is typically dominated by an expensive blind rotation. A prior construction achieved free-XOR evaluation, where XOR gates are computed by simply adding the two input ciphertexts, and used two lightweight blind rotations for AND gates to obtain a functionally complete gate set. The authors propose a similar gate bootstrapping framework that also supports free evaluation of XOR gates, but extends support to all 8 symmetric binary Boolean gates, meaning gates whose output is identical for inputs (0,1) and (1,0), using two blind rotations. The construction is presented as substantially simpler than the prior free-XOR scheme both conceptually and in terms of implementation, while broadening the set of gates that benefit from the free-XOR trick in TFHE-style homomorphic circuit evaluation.
