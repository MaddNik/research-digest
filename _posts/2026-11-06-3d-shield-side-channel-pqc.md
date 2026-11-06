---
title: "Side-Channel Attack Prevention for Post Quantum Cryptography Algorithms: A 3D-Shield Approach"
date: 2026-11-06 08:33:00 +0200
categories: [Hardware Security]
tags: [3d-integration, post-quantum-cryptography, side-channel-defense, ntt]
link: https://arxiv.org/abs/2611.01144
byline: "Carl Benda et al. (arXiv:2611.01144, Oct 31 2026)"
description: "A 3D integration approach called 3D-Shield proposes stacking decoy-key hardware over NTT chips to physically shield post-quantum cryptography side-channel targets."
---

Despite their resistance to quantum attacks in theory, practical implementations of all four standardized NIST post-quantum algorithms, ML-KEM, ML-DSA, FN-DSA, and SLH-DSA, remain vulnerable to side-channel attacks in practice. This paper proposes 3D-Shield, a defense based on three-dimensional chip integration that uses stacked hardware layers to physically shield the underlying cryptographic activity, introducing decoy keys and physical shielding through die stacking around dedicated number theoretic transform chips. The approach is designed to complement existing countermeasures such as masking and shuffling rather than replace them, specifically targeting side-channel leakage from the NTT butterfly operation that underlies ML-KEM and ML-DSA arithmetic. The authors outline the construction of the 3D-Shield approach and validate its effectiveness against a generic attack that targets intermediate computations inside an NTT butterfly.
