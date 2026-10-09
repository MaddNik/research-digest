---
title: "Provable Subexponential Algorithms for NIST Third-Round Lattice Families"
date: 2026-10-09 08:09:00 +0200
categories: [PQC]
tags: [lattice-cryptanalysis, kyber, dilithium, falcon]
link: https://eprint.iacr.org/2026/2386
byline: "Yiming Gao, Xuyuan Han, and Honggang Hu (IACR ePrint 2026/2386, Oct 6 2026)"
description: "A provable classical subexponential algorithm recovers the short secret of several NIST third-round lattice families, including Kyber/ML-KEM, FrodoKEM, SABER, NTRU, and Dilithium/ML-DSA, under growing parameters."
---

The authors give provable classical subexponential algorithms for secret recovery in growing parameter families associated with NIST third-round lattice candidates, covering Kyber/ML-KEM, FrodoKEM, SABER, NTRU LPRime, and Dilithium/ML-DSA, with polynomial moduli and polylogarithmic coefficient scales yielding recovery of the short secret component in expected time and space of about 2 to the power of n over ln ln n. The construction builds on the Wagner-style Gaussian sampling framework of Ducas, Engelberts, and Loyer and on a low-error decision-LWE algorithm, exploiting an exact gap in the squared Euclidean norm of a comparison vector so that one Gaussian list suffices to identify every secret coordinate by binary search. For quotient relations of NTRU type they develop an affine slice search that restricts candidate pairs to lattice slices and recovers an equivalent signing key in similar subexponential time, also applying to cyclic NTRU-HPS/HRSS. Importantly, the authors state that despite the subexponential complexity, their results do not establish any reduction in the concrete security of the currently specified NIST parameter sets.
