---
title: "Sub-Cubic Homomorphic Matrix Multiplication via Self-Dual Normal Bases"
date: 2026-08-14 08:18:00 +0200
categories: [FHE]
tags: [homomorphic-matrix-multiplication, bgv, strassen-algorithm]
link: https://eprint.iacr.org/2026/1592
byline: "Efe Izbudak et al. (IACR ePrint 2026/1592, Aug 6 2026)"
description: "Routing Strassen-style matrix multiplication through cyclotomic ring embeddings with self-dual normal bases halves the homomorphic trace depth needed under BGV, evaluating 32x32 matrix multiplication in 141.3 milliseconds."
---

The authors analyze bilinear embeddings of matrix algebras into commutative cyclotomic rings using the Cohn-Umans method, showing that single-multiplication bilinear monomial embeddings need a ring degree that grows roughly as N cubed for an N by N matrix. They circumvent this by routing Strassen tensor rank decompositions through orthogonal Chinese Remainder Theorem ideals, bringing the asymptotic complexity down to roughly N to the power of log base 2 of 7, Strassen's exponent. By embedding the inner tensor into the maximal real subfield and satisfying a parity constraint, they guarantee existence of a self-dual normal basis, cutting the number of required basis generators to one and halving the homomorphic trace depth needed. They further extend the construction to arbitrarily large matrices via a multi-ciphertext block-Strassen decomposition that defers the trace operator to post-recombination, eliminating homomorphic basis-switching entirely. Multi-threaded benchmarks over the BGV scheme evaluate 32 by 32 matrix multiplication in 141.3 milliseconds at security level lambda equals 148 using a single ciphertext-ciphertext multiplication, a 2.49 times speedup over multi-threaded baselines.
