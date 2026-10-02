---
title: "On the Power of Slicing and Dicing: Linear Garbling Beyond Two-Input Gates"
date: 2026-10-02 08:27:00 +0200
categories: [Cryptography]
tags: [garbled-circuits, secure-computation, free-xor, communication-complexity]
link: https://eprint.iacr.org/2026/2200
byline: "Tianren Liu and Luojian Wei (IACR ePrint 2026/2200, Sep 27 2026)"
description: "Extending Rosulek and Roy's slicing-and-dicing garbling technique to gates with three, four, and arbitrary fan-in yields new communication-cost bounds for garbled circuits."
---

Communication is a central efficiency bottleneck in garbled circuits, and Rosulek and Roy's slicing and dicing technique from CRYPTO 2021 gave a garbling scheme where XOR gates need no communication at all and each two-input AND gate costs only 1.5 lambda plus 5 bits, with lambda the security parameter. The authors investigate how far these techniques extend to gates with larger fan-in, developing a linear-algebraic framework that yields both concrete constructions and asymptotic bounds. For three- and four-input gates they obtain constructions with communication costs of 7 lambda over 3 plus 35 bits and 15 lambda over 4 plus a constant, respectively, and for arbitrary fan-in n they give a construction for any single-output gate with communication bounded by 22 times 2 to the n power times lambda over n plus 2 to the n power bits. The constructions remain compatible with free-XOR and keep all hash queries within each gate nonadaptive, and the authors prove security in the random-oracle model under a circular correlation robustness condition for any number of slices. Experiments applying the three-input construction to real control circuits find communication savings over the best two-input circuit baselines the authors collected.
