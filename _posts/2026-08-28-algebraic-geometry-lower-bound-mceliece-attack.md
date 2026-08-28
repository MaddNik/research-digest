---
title: "An Algebraic-Geometry Lower Bound against the ePrint:2026/1747 McEliece Key-Recovery Attack"
date: 2026-08-28 08:11:00 +0200
categories: [PQC]
tags: [classic-mceliece, code-based-cryptography, key-recovery-attack, nist-pqc]
link: https://eprint.iacr.org/2026/1810
byline: "Daniel Apon (IACR ePrint 2026/1810, Aug 26 2026)"
description: "An algebraic-geometric analysis identifies a structural dependency among held-position equations that undermines a recent holdout key-recovery attack on Classic McEliece."
---

This note responds to a recent proposal by Vedenev to turn a hold-out distinguisher for the Goppa-McEliece public key into a full key-recovery attack by reconstructing the hidden generalized Reed-Solomon representation from held support positions. The author shows experimentally that Vedenev's assumption of independent linear equations across held positions fails in a waterfall pattern, where additional held positions sharply drop in value just before the count needed for a successful attack. Identifying an algebraic-geometric reason for this dependence, the author proves that for a binary Goppa polynomial of degree t, the number of held positions required at the critical step must exceed 2t+3 under a stated nondegeneracy condition. For the NIST Category 5 parameter set mceliece8192128, this bound implies the required held-position count exceeds 259, pushing Vedenev's proposed key-recovery algorithm's cost above 2 to the 1500th power bit operations.
