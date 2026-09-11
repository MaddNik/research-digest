---
title: "Coral: General and Efficient Framework for Homomorphic Evaluation of Symmetric Ciphers"
date: 2026-09-11 08:15:00 +0200
categories: [FHE]
tags: [tfhe, transciphering, symmetric-ciphers, aes]
link: https://eprint.iacr.org/2026/1917
byline: "Jikang Bai et al. (IACR ePrint 2026/1917, Sep 8 2026)"
description: "Coral is a general TFHE-based transciphering framework that decomposes symmetric cipher decryption into four reusable computational modules, speeding up homomorphic evaluation of Trivium, AES, ChaCha20, and ZUC."
---

Fully homomorphic encryption (FHE) allows computation on encrypted data, but encrypting data under FHE is costly for clients and produces large ciphertexts, a problem transciphering addresses by letting clients upload symmetric ciphertexts that the server converts into FHE ciphertexts by homomorphically evaluating symmetric decryption. The authors note that transciphering itself can become a bottleneck, and that a general framework for efficiently supporting structurally different symmetric ciphers has been missing. They present Coral, a transciphering framework built on TFHE that decomposes decryption circuits at operation boundaries into four recurring computational modules, namely linear Boolean operations, sparse low-degree Boolean functions, modular additions, and small-domain substitutions, with compatible ciphertext interfaces that can be reused and composed across ciphers. Instantiating Coral for Trivium, AES, ChaCha20, and ZUC, the authors report speedups of up to 4.055 times for ZUC under single-threaded execution and up to 5.517 times for ChaCha20 under fully parallel execution compared to corresponding baselines.
