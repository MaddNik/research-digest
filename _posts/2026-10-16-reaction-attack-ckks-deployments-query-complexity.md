---
title: "Reaction Attack on CKKS Deployments with Asymptotically Optimal Query Complexity"
date: 2026-10-16 08:15:00 +0200
categories: [FHE]
tags: [ckks, reaction-attack, key-recovery, lattigo]
link: https://eprint.iacr.org/2026/2490
byline: "Song Bian et al. (IACR ePrint 2026/2490, Oct 15 2026, accepted to IEEE S&P 2027)"
description: "A protocol-level reaction attack recovers the full secret key of CKKS deployments that combine public coefficient-to-slot keys with a client's one-bit validity response, using a number of queries close to the information-theoretic minimum."
---

The authors study a protocol-level reaction leakage in CKKS deployments where public coefficient-to-slot evaluation keys are combined with a client's one-bit validity response to a decryption attempt. In this setting a malicious evaluator can recover a ternary secret key using a number of reaction queries that is asymptotically optimal in terms of the secret key's entropy, by shifting a public encryption key to produce a ciphertext whose plaintext depends on the secret key and then using the public coefficient-to-slot layer to make validity depend strictly on whether a targeted secret coefficient matches a guessed value. The attack does not break the underlying RLWE or CKKS IND-CPA security; instead it exploits the interaction between client-side validity reactions and public homomorphic linear transformations, and each query is independently randomized so malicious ciphertexts look distinct and evade naive detection. The authors implemented the full end-to-end attack in Lattigo version 6.2.0 and recovered the complete secret key across four standard CKKS parameter sets, using O(N) queries for uniform ternary secrets, within a factor of less than 2 of the oracle-only entropy lower bound, with a tailored variant reducing queries further for sparse ternary secrets. The paper is accepted to the 2027 IEEE Symposium on Security and Privacy.
