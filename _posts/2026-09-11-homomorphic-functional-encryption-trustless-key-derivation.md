---
title: "Homomorphic Functional Encryption: Trustless Key Derivation for Functional Encryption"
date: 2026-09-11 08:16:00 +0200
categories: [FHE]
tags: [functional-encryption, key-derivation, trust-minimization]
link: https://eprint.iacr.org/2026/1921
byline: "Camille Nuoskala et al. (IACR ePrint 2026/1921, Sep 8 2026)"
description: "A new three-party construction uses homomorphic encryption to let functional encryption key derivation be computed without the key curator ever holding the master secret key in the clear."
---

Functional encryption (FE) schemes typically rely on a trusted key curator who holds the master secret key and derives functional decryption keys, making that curator a sensitive single point of compromise. The authors study how homomorphic encryption (HE) can mitigate this problem by letting FE key-derivation algorithms be evaluated homomorphically, extending prior work on function-blind key derivation to a three-party deployment in which the key curator never holds the FE master secret key in the clear. Their construction preserves function blindness while removing the trust placed in the curator, reducing the trust assumptions of conventional FE key management. The authors built a proof-of-concept implementation, ran benchmarks to test the approach's practicality, and released their code publicly.
