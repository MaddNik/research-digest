---
title: "Modulus Operandi: Round-Optimal Modulus Conversion for MPC and Threshold FHE"
date: 2026-10-16 08:18:00 +0200
categories: [FHE]
tags: [threshold-fhe, modulus-conversion, secure-multiparty-computation, round-complexity]
link: https://eprint.iacr.org/2026/2450
byline: "Ivan Damgard et al. (IACR ePrint 2026/2450, Oct 12 2026)"
description: "New modulus conversion protocols for secure multiparty computation achieve a single communication round for threshold decryption of lattice-based ciphertexts, down from two or three rounds in prior work."
---

In secure multiparty computation, modulus conversion turns a sharing of a value modulo one modulus into a sharing of the same value modulo another, without leaking anything about the value, and it is a key step in threshold decryption for lattice-based cryptosystems where a sharing modulo the ciphertext modulus must move to the plaintext modulus before opening. The most efficient prior protocols needed two rounds for a prime target modulus, three rounds for arbitrary moduli, and one round only when all moduli were powers of two. The authors construct three new protocols in the preprocessing model: one that takes a single round for arbitrary moduli using just one opening, a variant that replaces most secure multiplications in preprocessing with checked private inputs to cut cost when the number of parties is small, and a third that avoids a bound on the input value altogether at the cost of two rounds. To support the two-round protocol they also build the first one-round comparison protocol for a bitwise-shared value against a public threshold with polynomial-size preprocessing, plus constant-round protocols without preprocessing for symmetric functions and comparisons modulo powers of arbitrary primes. Finally, the authors prove that a single round is optimal for non-interactive modulus conversion, showing that unless the target modulus divides the source modulus, every non-interactive conversion has a non-negligible failure probability.
