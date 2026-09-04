---
title: "Pushing Forward Multi-Secret-Key Homomorphic Encryption for Private Average Aggregation"
date: 2026-09-04 08:18:00 +0200
categories: [FHE]
tags: [multiparty-he, federated-learning, rlwe, secure-aggregation]
link: https://arxiv.org/abs/2609.01945
byline: "Miguel Morona-Minguez et al. (arXiv:2609.01945, Sep 1 2026)"
description: "New multi-secret-key RLWE homomorphic encryption protocols for private federated-learning aggregation avoid a collective public key and cancel ciphertext noise explicitly, removing the need for large smudging noise during collaborative decryption."
---

Homomorphic encryption fits the client-to-aggregator communication pattern of federated learning well, but single-key deployments require strong non-collusion assumptions, while multiparty homomorphic encryption removes that limitation at the cost of needing large-variance smudging noise during collaborative decryption under recent attacks on restricted decryption access, which increases ciphertext size and implementation complexity. This paper proposes lightweight multi-secret-key protocols for private average aggregation based on RLWE homomorphic encryption that depart from the usual multiparty blueprint by avoiding generation of a collective public key, letting each client instead encrypt its update under its own secret key while keeping the resulting ciphertexts compatible with homomorphic aggregation and collaborative decryption. By explicitly tracking and cancelling ciphertext noise during decryption, the protocol removes the need for large security-parameter-dependent smudging noise. The construction is instantiated in both exact BFV-based and approximate CKKS-based variants, proven secure in the semi-honest model against an adversary corrupting the aggregator and up to L minus 1 clients, and shown to substantially reduce ciphertext expansion and online cost relative to state-of-the-art multiparty-homomorphic-encryption-based aggregation while preserving practical performance.
