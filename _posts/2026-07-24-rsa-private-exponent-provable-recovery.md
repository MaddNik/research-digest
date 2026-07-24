---
title: "Provable Recovery of RSA Private Exponents below N^(11/42-epsilon)"
date: 2026-07-24 08:23:00 +0200
categories: [Cryptography]
tags: [rsa-cryptanalysis, small-private-exponent, wiener-attack, provable-security]
link: https://eprint.iacr.org/2026/1478
byline: "Yiming Gao and Honggang Hu (IACR ePrint 2026/1478, Jul 20 2026)"
description: "A fully provable RSA private key recovery attack that pushes the exponent bound past the classical Wiener 1 over 4 threshold without relying on heuristic assumptions."
---

The paper revisits small private exponent attacks on RSA, an area historically anchored by Wiener's bound of d less than N to the power 1 over 4. The authors show that for balanced RSA moduli, the private exponent d can be recovered when d is at most N to the power 11 over 42 minus epsilon. Unlike many prior improvements in this line of research, their method is fully provable rather than relying on heuristic lattice reduction assumptions. The result is presented as the first fully provable improvement beyond Wiener's classical exponent bound.
