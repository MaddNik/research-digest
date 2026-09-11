---
title: "Cryptanalysis of Deep Neural Cryptography: Second Round Key Recovery on the Unprotected Implementation and a Floating-Point Attack on the Protected Implementation of AES"
date: 2026-09-11 08:25:00 +0200
categories: [Cryptography]
tags: [aes, neural-network-implementation, floating-point-attack, key-recovery]
link: https://eprint.iacr.org/2026/1919
byline: "Sisung Kim et al. (IACR ePrint 2026/1919, Sep 8 2026)"
description: "New attacks extend key recovery against neural-network implementations of AES to a second round key on the unprotected version, and break the proposed provably secure protected version using a floating-point rounding flaw."
---

At Eurocrypt 2026, Gerault et al. introduced natural deep neural network implementations of block ciphers, ReLU networks that agree exactly with the cipher on binary inputs but extend it continuously to real-valued inputs, and showed this extension exposes the first round key, proposing a generic Secure Blackbox Transformation to make such implementations provably secure. The authors revisit both sides of this result. On the attack side, they refine the absorption property of the natural S-box and combine it with a chosen-plaintext collision test to recover the second round key of AES-256 in about 2 to the 39 queries, going beyond the first-round-key attacks known previously. On the defense side, they show that the Secure Blackbox Transformation's security guarantee, proven over the reals, does not carry over to finite precision, giving a floating-point attack that recovers the first round key of the protected AES-128 implementation in 128 chosen queries by exploiting an input value the defense fails to round to a bit, a weakness they confirm in bfloat16, float16, float32, and float64. They propose a clamp placed before the rounding step that blocks the attack while leaving the cipher and the exact-real security guarantee unchanged, though a full finite-precision security guarantee remains open.
