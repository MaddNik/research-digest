---
title: "Sub-Cubic Homomorphic Matrix Multiplication via Self-Dual Normal Bases"
date: 2026-08-07 08:24:00 +0200
categories: [FHE]
tags: [bgv, matrix-multiplication, cyclotomic-rings]
link: https://eprint.iacr.org/2026/1592
byline: "Efe Izbudak et al. (IACR ePrint 2026/1592, Aug 3 2026)"
description: "A new algebraic embedding technique brings sub-cubic complexity to homomorphic matrix multiplication under the BGV scheme, with a 2.49 times speedup demonstrated for 32 by 32 matrices."
---

The paper studies how to embed matrix algebra operations into commutative cyclotomic rings so that matrix multiplication can be evaluated homomorphically with lower complexity. The authors show that a single-multiplication bilinear embedding of this kind normally needs a ring degree on the order of N cubed, which is too costly in practice. To get around this, they route Strassen's matrix-multiplication tensor decomposition through orthogonal ideals defined via the Chinese Remainder Theorem, and they embed the resulting tensor into a maximal real subfield so that a self-dual normal basis exists, cutting the number of basis generators needed down to one. This combination brings the asymptotic multiplication count down toward N to the power of log base two of seven, approximately N to the 2.807 power, for arbitrary matrix sizes. Using an implementation over the BGV scheme, the authors report a 2.49 times speedup over a baseline for 32 by 32 matrix multiplication at a security level of lambda equals 148, completing in about 141.3 milliseconds.
