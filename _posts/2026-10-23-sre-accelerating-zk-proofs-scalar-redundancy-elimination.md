---
title: "SRE: Accelerating Zero-Knowledge Proofs via Scalar Redundancy Elimination in Multi-Scalar Multiplication"
date: 2026-10-23 08:27:00 +0200
categories: [Cryptography]
tags: [zero-knowledge-proofs, multi-scalar-multiplication, msm-acceleration]
link: https://arxiv.org/abs/2610.27452
byline: "Jonathan Ku et al. (arXiv:2610.27452, Oct 20 2026)"
description: "A new Scalar Redundancy Elimination technique reduces the number of point-addition operations in Pippenger's bucket method for multi-scalar multiplication by 25 percent, giving a 30 percent runtime speedup and 10 to 20 percent faster zero-knowledge proof systems."
---

Multi-scalar multiplication (MSM) is a fundamental elliptic-curve cryptography operation that underlies cryptographic primitives such as polynomial commitments and zero-knowledge proofs, where it often becomes the runtime bottleneck, and the current state-of-the-art algorithm, Pippenger's bucket method, is itself bottlenecked by its point-merging step. The authors target this bottleneck with a new Scalar Redundancy Elimination (SRE) algorithm, offering a vanilla array-based approach, a list-based greedy approach, and a list-based exhaustive approach, all incorporating an early-stopping technique, which can be integrated into a modified MSM algorithm built on Pippenger's bucket method depending on the use case. The proposed MSM algorithm enhanced with SRE incurs less than 3 percent additional search time while reducing the number of operations by 25 percent, leading to a 30 percent speedup in runtime compared with the standard Pippenger's bucket method. This translates into a 10 to 20 percent runtime reduction across various zero-knowledge proof systems that rely heavily on MSM.
