---
title: "DKG Is All You Need"
date: 2026-10-02 08:31:00 +0200
categories: [Cryptography]
tags: [threshold-encryption, distributed-key-generation, batched-decryption, transparent-setup]
link: https://eprint.iacr.org/2026/2205
byline: "Guru-Vamsi Policharla (IACR ePrint 2026/2205, Sep 30 2026)"
description: "A batched threshold encryption scheme needs nothing beyond a plain distributed key generation step for setup, with public parameters independent of the batch size."
---

The author constructs the first batched threshold encryption scheme with a transparent setup where the public parameters are independent of the batch size, so batches of arbitrary size can be decrypted without fixing a bound in advance, with security proved under a constant-size assumption, the decisional bilinear square Diffie-Hellman assumption. Setup is nothing more than a distributed key generation protocol to sample secret shares of a random value. Ciphertexts consist of two elements in the group G1, one in G2, and the encrypted message, plus a non-interactive zero-knowledge proof for chosen-ciphertext security built from a sigma protocol over two field elements; partial decryptions are a single G1 element computed with one scalar multiplication, and decrypting a batch of B ciphertexts costs O(B) pairings and O(B times log squared B) group operations. In the ramp setting, where there is a gap between the reconstruction threshold t and the corruption threshold f as in consensus protocols with n at least 3f plus 1, the author also gives a pairing-free batched threshold encryption scheme from the DDH assumption whose partial decryptions are 2B over (t minus f) group elements, and reduces the aggregation cost of the pairing-based scheme to O(B times log squared of B over (t minus f)) group operations.
