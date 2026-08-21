---
title: "Silent Threshold Encryption from Lattices"
date: 2026-08-21 08:08:00 +0200
categories: [PQC]
tags: [threshold-encryption, lattice-based, functional-encryption, decomposed-lwe]
link: https://eprint.iacr.org/2026/1716
byline: "Jeffrey Champion et al. (IACR ePrint 2026/1716, Aug 17 2026)"
description: "A lattice-based silent threshold encryption scheme with ciphertext size that grows sublinearly in the number of decryption participants."
---

This paper constructs silent threshold encryption, a setting where a group public key is derived deterministically from individual members' public keys without any interactive setup. The main goal is a scheme whose ciphertext size grows sublinearly, or even independently, of the decryption quorum size N, using the decomposed learning with errors (LWE) assumption in the random oracle model. The authors report ciphertext size on the order of quasi-linear in the threshold T plus a term polynomial in the security parameter and log N, giving meaningful succinctness whenever T is bounded by N to a constant power less than one. The construction also extends to general monotone policy families via succinct secret sharing. The core technical tool is a bounded-collusion registered functional encryption scheme with succinct ciphertexts for depth-d Boolean circuits. The authors present this as an improvement over prior silent threshold encryption approaches that relied on bilinear maps or heavyweight primitives such as indistinguishability obfuscation.
