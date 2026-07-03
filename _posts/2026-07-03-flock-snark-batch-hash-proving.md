---
title: "Flock: Fast Proving for Batch Boolean Computations"
date: 2026-07-03 08:19:00 +0200
categories: [Cryptography]
tags: [snark, zero-knowledge, hash-proving, proof-systems]
link: https://eprint.iacr.org/2026/1329
byline: "Bünz et al. (IACR ePrint 2026/1329, Sun 28 Jun 2026)"
description: "Flock is a new hash-based SNARK that proves huge batches of standard hash evaluations such as SHA-256, Keccak, and BLAKE3 dramatically faster than prior systems."
---

Flock addresses a common SNARK bottleneck: proving large batches of standard cryptographic hash function evaluations. It proves batches of the same R1CS circuit together with input and output relations between them, and can handle hash-chains and Merkle path openings, with the paper noting it could in principle extend to hash-based signature verification. The construction combines new optimizations to the lincheck and zerocheck protocols with an optimized implementation. On a single core of an M4 Max processor the authors report proving 82,000 BLAKE3 compression function evaluations, 42,000 SHA-256 compressions, and 30,000 Keccak permutations per second, with overhead less than 250 times native execution. On ten cores, throughput exceeds 660,000 BLAKE3 compressions per second, and for SHA-256 the paper reports Flock is more than 9 times faster than Binius64, the prior state of the art.
