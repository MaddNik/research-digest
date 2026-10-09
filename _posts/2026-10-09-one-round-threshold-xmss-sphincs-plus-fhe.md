---
title: "One-Round Threshold XMSS and SPHINCS+ from Fully Homomorphic Encryption"
date: 2026-10-09 08:22:00 +0200
categories: [FHE]
tags: [threshold-signatures, hash-based-signatures, ckks]
link: https://eprint.iacr.org/2026/2360
byline: "Jung Hee Cheon et al. (IACR ePrint 2026/2360, Oct 5 2026)"
description: "The first one-round threshold protocol for XMSS and SPHINCS+ evaluates signing homomorphically under threshold FHE, producing signatures that unmodified RFC 8391 or FIPS 205 verifiers accept."
---

Hash-based signatures such as XMSS and SPHINCS+ are well established in post-quantum cryptography, but thresholdizing them has been difficult because their lack of algebraic structure rules out the shortcuts available for classical signatures like ECDSA, Schnorr, RSA, or BLS, leaving costly general-purpose MPC as the main option. This paper constructs and implements the first one-round threshold protocol for XMSS and SPHINCS+, sharing the secret key among signing parties while evaluating the signing algorithm homomorphically under a threshold fully homomorphic encryption scheme, so that any t-of-n parties can jointly derive a signature via threshold decryption that is accepted by an unmodified RFC 8391 or FIPS 205 verifier. The authors develop efficient homomorphic SHAKE evaluation over discrete CKKS for varying batch sizes, and handle the parallel hash computations and data-dependent selections in XMSS and SPHINCS+ signing through batching and homomorphic lookup. Their implementation amortizes SHAKE256/256 evaluation to 3.4 milliseconds per hash, completes online threshold XMSS signing in 0.69 seconds, and shows that threshold SPHINCS+ has roughly two orders of magnitude higher signing latency but over an order of magnitude lower setup latency than XMSS.
