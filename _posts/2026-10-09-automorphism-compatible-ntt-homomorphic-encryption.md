---
title: "Automorphism-Compatible NTT and its Application to Homomorphic Encryption"
date: 2026-10-09 08:23:00 +0200
categories: [FHE]
tags: [ckks, bgv, bfv, ntt]
link: https://eprint.iacr.org/2026/2328
byline: "Charanjit S. Jutla, Nathan Manohar, and Guy Moshkowich (IACR ePrint 2026/2328, Oct 4 2026)"
description: "New in-place NTT butterfly algorithms output results in an automorphism-compatible order, letting Galois automorphisms on CKKS and BGV/BFV ciphertexts be applied with a simple shift instead of an arbitrary permutation."
---

For N a power of 2, the negacyclic number-theoretic transform (NTT) maps a degree N minus 1 polynomial to its evaluations at the N primitive 2N-th roots of unity, and standard in-place butterfly algorithms such as Cooley-Tukey and Gentleman-Sande compute it in O(N log N) time but output evaluations in a fixed standard order. The authors give in-place butterfly algorithms for the negacyclic NTT and its inverse that instead output evaluations in an automorphism-compatible order, using the same structure as the standard algorithms but with different precomputed twiddle factors. These automorphism-compatible algorithms apply directly to the packed fully homomorphic encryption schemes CKKS and BGV/BFV, where the negacyclic NTT is a major component of ciphertext arithmetic. Using this approach, Galois automorphisms can be applied to ciphertexts stored in double-CRT format with a simple cyclic shift or adjacent-pair swap of the stored data, in contrast to currently used butterfly algorithms that require an arbitrary-looking permutation, and the authors note this removes the need for a dedicated automorphism functional unit in FHE hardware accelerators.
