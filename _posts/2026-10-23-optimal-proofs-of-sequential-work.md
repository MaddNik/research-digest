---
title: "Optimal Proofs of Sequential Work"
date: 2026-10-23 08:22:00 +0200
categories: [Cryptography]
tags: [proofs-of-sequential-work, timed-cryptography, lower-bounds]
link: https://eprint.iacr.org/2026/2569
byline: "Krzysztof Pietrzak and Leonid Reyzin (IACR ePrint 2026/2569, Oct 20 2026)"
description: "A new proof of sequential work with maximum node indegree two matches newly proved communication lower bounds up to constant factors, cutting the honest prover's total hash-input complexity from O(T log T) to O(T)."
---

A proof of sequential work (PoSW) lets a verifier become convinced that a prover performed T sequential computation steps, with (delta, lambda)-soundness meaning a malicious prover making at most (1-delta)T sequential steps can produce a valid proof only with probability 2 to the power minus lambda, even using massive parallelism. PoSW are, alongside time-lock puzzles and verifiable delay functions, a central primitive in timed cryptography, and unlike those other primitives can be built from hash functions alone with a security proof in the random oracle model. Existing constructions rely on graph labeling, where the prover sequentially computes labels over a graph of T nodes; the efficient Cohen-Pietrzak construction from 2018 requires transmitting O((lambda log T)/delta) hash outputs over a graph with average indegree O(log T), giving O(T log T) total hash inputs for labeling. This paper first proves a matching lower bound, showing any efficient graph-labeling-based PoSW with (delta, lambda)-soundness requires the prover to send Omega((lambda log T)/delta) labels, via a reduction to a cut-depth game bounded using a refinement of Valiant's depth-reduction argument, and then presents a new PoSW construction with maximum indegree two that matches these bounds up to constant factors, reducing the honest prover's total hash-input complexity from O(T log T) to O(T) while retaining the same asymptotic communication and verifier hash-input complexity.
