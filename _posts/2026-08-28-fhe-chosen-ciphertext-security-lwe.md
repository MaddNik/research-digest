---
title: "Fully Homomorphic Encryption with Chosen-Ciphertext Security from LWE"
date: 2026-08-28 08:20:00 +0200
categories: [FHE]
tags: [chosen-ciphertext-security, lwe, naor-yung, standard-model]
link: https://eprint.iacr.org/2026/1756
byline: "Rupeng Yang et al. (IACR ePrint 2026/1756, Aug 21 2026)"
description: "This paper constructs fully homomorphic encryption with chosen-ciphertext security from the learning-with-errors assumption in the standard model, relying only on the same circular-secure LWE assumption used for CPA-secure FHE."
---

The authors construct 1-hop fully homomorphic encryption schemes with chosen-ciphertext security from the learning with errors assumption in the standard model, with security resting only on circular-secure LWE, matching the assumption needed for FHE with basic chosen-plaintext security. The scheme achieves a security notion strictly stronger than CCA1 security, whereas prior FHE schemes with even just CCA1 security required either the random oracle model or non-falsifiable assumptions. The construction follows the well-known Naor-Yung double encryption paradigm, but unlike previous works that employ general zero-knowledge succinct non-interactive arguments of knowledge, the authors design a special succinct argument to prove the validity of FHE ciphertexts, built from batch arguments for NP and a new primitive they call predicate extractable commitment, which they suggest may be of independent interest. The paper is presented as a major revision of an IACR publication that appeared at CRYPTO 2025.
