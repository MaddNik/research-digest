---
title: "Fully-Succinct Multi-Key FHE and Rate-1 Simulatable Threshold Decryption from LWE"
date: 2026-08-21 08:16:00 +0200
categories: [FHE]
tags: [multi-key-fhe, threshold-decryption, lwe, succinct-ciphertexts]
link: https://eprint.iacr.org/2026/1683
byline: "Abtin Afshar et al. (IACR ePrint 2026/1683, Aug 13 2026)"
description: "The first multi-key fully homomorphic encryption scheme with ciphertext, public-key, and secret-key sizes that do not grow with the number of participating users."
---

The paper constructs a leveled multi-key FHE (MKFHE) scheme, secure under the standard Learning with Errors assumption, in which ciphertext size, public key size, and secret key size are all independent of the number of users, N. The authors state that every prior MKFHE construction required ciphertext size to grow at least linearly with the number of users, a limitation that had persisted for more than a decade, and their result is presented as the first evidence that constant-ciphertext-size MKFHE is achievable from standard assumptions. They also give a single-round distributed decryption protocol for multi-key ciphertexts that is simultaneously rate one, meaning each user's partial decryption share is the same size as the plaintext, and simulatable, meaning an honest user's partial decryption can be simulated. The authors say no prior MKFHE scheme from standard assumptions achieved both properties together. They argue this construction is useful for building multi-party computation protocols with asymptotically optimal communication complexity.
