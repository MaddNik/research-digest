---
title: "Multi-Diagonal Truncated Differentials and Ciphertext-Only Attacks on Reduced-Round AES"
date: 2026-08-14 08:26:00 +0200
categories: [Cryptography]
tags: [aes, truncated-differentials, ciphertext-only-attack]
link: https://eprint.iacr.org/2026/1637
byline: "Orhun Kara and Can Balikci (IACR ePrint 2026/1637, Aug 8 2026)"
description: "A new analytical framework for truncated differential probabilities yields the first ciphertext-only distinguishing attack on 5-round AES and a matching key-recovery attack on 6-round AES."
---

The authors develop a new analytical framework for computing truncated differential probabilities in AES that goes beyond prior integral-cryptanalysis techniques restricted to a single active diagonal. Their framework handles configurations with one active diagonal in the plaintext and arbitrary passive inverse diagonals in the ciphertext, as well as the complementary setting, which had not previously been addressed analytically rather than through statistical sampling. Using this, they build the first ciphertext-only distinguishing attack on 5-round AES and extend it to a key-recovery attack on 6-round AES under specific plaintext conditions. They validate the results through multiple independent verification methods and present the underlying methodology as broadly applicable to other AES-like block ciphers.
