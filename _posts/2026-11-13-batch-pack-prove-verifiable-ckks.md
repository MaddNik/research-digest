---
title: "Batch, Pack, and Prove: More Efficient Verifiable Computation for CKKS"
date: 2026-11-13 08:21:00 +0200
categories: [FHE]
tags: [ckks, verifiable-computation, polynomial-commitments]
link: https://arxiv.org/abs/2611.16922
byline: "Ignacio Cascudo et al. (arXiv:2611.16922, Nov 12 2026, ASIACRYPT 2026)"
description: "New batching and packing techniques remove the scalability bottlenecks of prior succinct arguments for verifying CKKS homomorphic computations, producing proofs that are orders of magnitude smaller and faster."
---

Ensuring the integrity of encrypted computations is an important challenge in homomorphic encryption, and while verifiable computation can address this in theory, making it practical has proven far from trivial. Building on prior succinct arguments that prove arithmetic circuits and range checks over the relevant polynomial ring for CKKS ciphertexts, the authors identify three scalability bottlenecks in that earlier work: large polynomial commitment proof sizes, a linear overhead in range proofs, and no explicit method for sublinear verification. This paper removes all three bottlenecks with a more efficient arithmetization of CKKS computations, a new polynomial commitment called BatchFold that supports batched evaluations and achieves shorter proofs, a packing technique that eliminates the need to commit to massive polynomials and removes the linear overhead in range proofs, and SparsePack, an efficient protocol for proving evaluations of sparse, circuit-dependent polynomials that leverages both packing and batched evaluations. Evaluated on a generic neural network architecture, the techniques achieve proofs that are several orders of magnitude smaller and faster than prior approaches. The full version accompanies a paper accepted at ASIACRYPT 2026.
