---
title: "On Memory Effects in PWXL variants"
date: 2026-08-28 08:16:00 +0200
categories: [PQC]
tags: [uov, multivariate-cryptography, nist-pqc, cryptanalysis]
link: https://eprint.iacr.org/2026/1819
byline: "Jintai Ding et al. (IACR ePrint 2026/1819, Aug 27 2026)"
description: "An analysis of memory effects in Wiedemann-based XL attacks concludes that UOV's original NIST parameter sets remain sufficiently secure at security levels Ip, Is, and III."
---

The authors estimate the intrinsic undercounting that occurs in the free-memory-access, Macaulay-coefficient-on-demand RAM model when it is applied to the Parallelized Wiedemann-based XL algorithm as used in the Ran Wedge attack and the Furue-Ikematsu intersection attack against UOV, under optimistic but feasible-sounding assumptions about the attacker. They argue that accounting for these memory effects shows UOV is secure enough at NIST security levels Ip, Is, and III without needing the parameter changes some had suggested. As an additional option, if NIST considers the original parameters insufficiently convincing, the authors offer alternative perturbations that hold the number of equations m, and hence the compressed public key size, fixed while spending only on the vinegar variable count: uov-Ip# (256,116,44), uov-III# (256,186,72), and uov-V# (256,250,96).
