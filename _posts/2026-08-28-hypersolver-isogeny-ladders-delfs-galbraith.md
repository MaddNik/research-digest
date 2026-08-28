---
title: "HyperSolver: Asymptotically and Concretely Accelerating the Delfs–Galbraith Attack using Isogeny Ladders"
date: 2026-08-28 08:09:00 +0200
categories: [PQC]
tags: [isogeny-based-cryptography, sqisign, cryptanalysis, gpu-implementation]
link: https://eprint.iacr.org/2026/1823
byline: "Lorenz Panny et al. (IACR ePrint 2026/1823, Aug 27 2026)"
description: "HyperSolver presents a new memoryless Delfs-Galbraith variant that asymptotically and concretely accelerates attacks on the supersingular endomorphism-ring problem underlying isogeny-based schemes such as SQIsign."
---

This paper presents a new variant of the memoryless Delfs-Galbraith algorithm for finding an isogeny path from a given supersingular elliptic curve to a curve with known endomorphism ring, a problem that underlies the security of isogeny-based cryptography including SQIsign. For arbitrary characteristics the algorithm asymptotically outperforms the previous best Delfs-Galbraith variant by a logarithmic factor, and the authors also compute concrete finite-field-operation cost estimates showing lower expected cost than all previous variants. As part of the analysis, they provide a novel study of the probability of encountering distinguished subgraphs in an expander graph under different graph-exploration strategies, a subtlety they say had gone unnoticed. The authors implement the algorithm with the asymptotic bottleneck attacked on GPUs, reporting that 100-bit instances can be solved in under 100 GPU hours, compared with the current 114-bit ECDLP cryptanalytic record achieved with significantly more hardware and time. The paper is set to appear at Asiacrypt 2026.
