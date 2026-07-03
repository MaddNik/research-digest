---
title: "Generalized Batched Decomposition Key-Switching for CKKS"
date: 2026-07-03 08:16:00 +0200
categories: [FHE]
tags: [ckks, key-switching, noise-analysis, bootstrapping-optimization]
link: https://eprint.iacr.org/2026/1340
byline: "Peña et al. (IACR ePrint 2026/1340, Mon 29 Jun 2026)"
description: "A generalized batched key-switching decomposition for CKKS cuts noise growth and redundant computation, with new noise analysis for a widely used bootstrapping algorithm."
---

Lattice-based homomorphic encryption schemes accumulate noise in ciphertexts as computation proceeds, and the key-switching procedure used to re-encrypt a ciphertext under a new secret key is a major contributor to that noise growth. The authors generalize the RNS-based decomposition technique used in CKKS key-switching to an arbitrary number of input polynomials and secret keys, enabling multiple relinearizations and rotations to be performed in batch. This allows the modulus-lowering and decomposition steps to be hoisted, restricting noise growth and eliminating redundant computation. The paper proves security and correctness for all proposed algorithms and derives explicit noise bounds, illustrating the impact on applications such as private deep neural network inference. It also provides what the authors describe as the first noise analysis of the double-hoisted baby-step giant-step matrix-vector multiplication algorithm used in state-of-the-art CKKS bootstrapping circuits, and identifies a further optimization for automorphism applications during the giant steps of that algorithm.
