---
title: "Incomplete Ciphertext Comparison in ML-KEM: From an IND-CCA2 Break to Key Recovery"
date: 2026-08-21 08:25:00 +0200
categories: [Hardware Security]
tags: [ml-kem, fujisaki-okamoto, key-recovery, implementation-flaw]
link: https://eprint.iacr.org/2026/1682
byline: "Bhabani Sankar Das (IACR ePrint 2026/1682, Aug 13 2026)"
description: "An attack on wolfSSL's ML-KEM implementation shows that an incomplete Fujisaki-Okamoto ciphertext comparison leaks decryption noise and enables near-complete secret-key recovery."
---

The paper reports that wolfSSL's ML-KEM decapsulation compares fewer than all ciphertext bytes during the Fujisaki-Okamoto re-encryption check, and that the skipped bytes carry the compressed tail of the decryption noise, which is an exact linear function of the secret key. By varying the unchecked bytes and observing decapsulation behavior, an attacker can measure this noise coordinate by coordinate and recover the key via ordinary least squares. Against the shipped binaries, the attack recovers about 98.0 percent of the 2048 secret coefficients of ML-KEM-1024 using 400 ciphertexts on an AVX2 backend and 98.5 percent using 600 ciphertexts on NEON, with full recovery reaching roughly 1300 ciphertexts against a reference implementation.
