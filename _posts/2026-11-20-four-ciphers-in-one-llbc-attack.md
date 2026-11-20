---
title: "Four Ciphers in One: Full-Round Attacks on the Reference Implementation of LLBC"
date: 2026-11-20 08:21:00 +0200
categories: [Cryptography]
tags: [block-ciphers, cryptanalysis, lightweight-cryptography, reference-implementation]
link: https://eprint.iacr.org/2026/2896
byline: "Sei Kofuku, Yasutaka Igarashi (IACR ePrint 2026/2896, Nov 15 2026)"
description: "A reference implementation of the LLBC lightweight block cipher uses wrong rotation amounts that split it into four independent 32-bit ciphers, enabling full key recovery on all 20 rounds."
---

LLBC is a 128-bit low-latency block cipher for IoT applications, proposed in the IEEE Internet of Things Journal in 2025, whose designers released a reference implementation in C and Verilog that produced the proposal's own test vectors. The authors show this reference implementation differs from the peer-reviewed specification in eight points, most importantly using round-function rotation amounts of 32 and 16 instead of the specified 3 and 19. They prove that an LLBC-type cipher with rotation amounts b1 and b2 is a product of independent sub-ciphers whenever the greatest common divisor of 64, b1, and b2 is a multiple of 4, and splits entirely when that value is a multiple of 8, which is exactly what happens in the reference implementation: it splits into four 32-bit ciphers that never mix. Exploiting this split, the authors give a probability-one distinguisher from two chosen plaintexts, decrypt any ciphertext with 2 to the 32 chosen plaintexts, and recover the master key from three known plaintexts with about 2 to the 80 encryptions, a factor of 2 to the 48 below exhaustive search, completing the full 20-round decryption attack in 175.5 seconds on a single PC. They recommend that designers independently verify released reference code against test vectors generated separately from the specification.
