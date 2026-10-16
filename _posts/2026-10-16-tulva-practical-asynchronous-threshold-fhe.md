---
title: "Tulva: Practical Asynchronous Threshold FHE"
date: 2026-10-16 08:16:00 +0200
categories: [FHE]
tags: [threshold-fhe, asynchronous-decryption, privacy-preserving-evm, lwe]
link: https://eprint.iacr.org/2026/2485
byline: "Valerio Cini et al. (IACR ePrint 2026/2485, Oct 14 2026, IEEE S&P 2027)"
description: "Tulva adds an asynchronous threshold decryption mechanism to essentially any base fully homomorphic encryption scheme, letting any subset of parties decrypt without needing to be online at the same time."
---

Fully homomorphic encryption lets a single secret key present a single point of failure, and threshold FHE addresses this by distributing the key across K parties so that any threshold t of them can cooperate to decrypt. Tulva targets the asynchronous setting, where a ciphertext can be decrypted by collecting decryption shares from any t parties who never need to coordinate or be online simultaneously, which matters for applications such as privacy-preserving Ethereum Virtual Machines and quorum-based decryption of long-lived private data. The scheme is compatible with virtually any base FHE scheme and leaves ciphertexts unchanged apart from an appended random tag, supports a wide range of threshold profiles and ring degrees of 256 or more, and achieves security against partial decryption queries on challenge ciphertexts based on the standard LWE assumption. The authors provide an open-source implementation and report that, for a 16-out-of-512 threshold with a publicly preprocessed ciphertext, computing the secret-dependent partial decryption and combining shares takes only 3.7 milliseconds and 0.5 milliseconds respectively on commodity hardware. Compared with a state-of-the-art synchronous scheme presented at CCS 2025, Tulva replaces an interactive randomness preparation step with a public, ciphertext-dependent preprocessing step, removes interaction from the online phase, and supports 32 times more total users at similar decryption time.
