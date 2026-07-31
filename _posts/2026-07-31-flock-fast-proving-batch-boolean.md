---
title: "Flock: Fast Proving for Batch Boolean Computations"
date: 2026-07-31 08:19:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, snark, hash-based-proofs]
link: https://arxiv.org/abs/2607.27491
byline: "Benedikt Bunz et al. (arXiv:2607.27491, Jul 29 2026)"
description: "Flock is a new hash-based SNARK optimized for proving large batches of standard cryptographic hash evaluations such as SHA-256, Keccak, and BLAKE3."
---

Flock targets a common SNARK bottleneck, proving many repeated hash-function evaluations, by proving batches of the same R1CS circuit together with input and output relations between instances, enabling applications like hash-chains and Merkle path openings. It combines new optimizations to the lincheck and zerocheck protocols with an implementation the authors describe as co-designed with coding agents. On a single core of an M4 Max processor it reaches 82 thousand BLAKE3 compression-function evaluations, 42 thousand SHA-256 compressions, and 30 thousand Keccak permutations per second, with less than 250 times overhead versus native execution. On ten cores throughput exceeds 660 thousand BLAKE3 compressions per second. The authors report more than 9 times faster SHA-256 proving than Binius64, the prior state of the art, and more than 500 times faster than the fastest elliptic-curve-based SNARK they measured against.
