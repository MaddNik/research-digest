---
title: "A Bleichenbacher bit-by-bit oracle attack from partial message knowledge"
date: 2026-11-20 08:23:00 +0200
categories: [Cryptography]
tags: [bleichenbacher-attack, rsa, pkcs1, padding-oracle]
link: https://eprint.iacr.org/2026/2901
byline: "Juan Carlos Garcia Escartin (IACR ePrint 2026/2901, Nov 15 2026)"
description: "Knowing just the three least significant bytes of an RSA message lets an attacker with a padding oracle decrypt the full message bit by bit."
---

Oracle attacks illustrate why cryptographic standards must be implemented correctly in code, and the Bleichenbacher attack on RSA with PKCS#1 v1.5 padding remains a notable example decades after it was first described. This paper shows that an attacker who knows a few least significant bytes of an RSA message can exploit a server's oracle side channel to decrypt the full message bit by bit. The author considers two oracles testable with chosen ciphertexts, one revealing whether the decrypted message starts with the bytes 00 02 and another revealing whether the decrypted message is fully PKCS compliant. For an attacker who knows the three least significant bytes, the first oracle yields an attack where a single oracle call reveals the next least significant bit, and the second requires only a small constant number of oracle calls with high probability. The attack splits the message bits into a known and an unknown section and chooses transformations that keep the unknown part, except for the last unknown bit, orders of magnitude below the integer from the known part, so the resulting string's padding validity reveals the unknown bit. The same method is adapted to extract a few least significant bytes of a message at increased cost, mainly from finding a second validly padded message from the original captured ciphertext.
