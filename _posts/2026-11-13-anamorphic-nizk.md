---
title: "Anamorphic NIZK: Definition, Construction and More"
date: 2026-11-13 08:25:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, anamorphic-encryption, fiat-shamir]
link: https://eprint.iacr.org/2026/2866
byline: "Wenhui Kong, Gongxian Zeng, Zhengan Huang (IACR ePrint 2026/2866, Nov 11 2026)"
description: "The authors introduce anamorphic non-interactive zero-knowledge proofs, where publicly verifiable proofs can carry a covert message recoverable only with a double key."
---

Anamorphic encryption enables covert communication even when ordinary decryption keys are disclosed, and prior work on anamorphic signatures extended this capability to authentication-only settings, showing that the Fiat-Shamir transform preserves anamorphism. The authors note that this prior result assumes an already anamorphic protocol and does not by itself ensure witness privacy against the recipient, which motivates building anamorphism directly into non-interactive zero-knowledge proofs. They introduce anamorphic NIZK, in which publicly verifiable proofs carry covert messages that are recoverable with a double key, formalizing anamorphic security, strong robustness, recipient anamorphic zero knowledge, and simulation extractability. A generic construction in the random oracle model combines suitable Sigma protocols with authenticated encryption with associated data through a salted Fiat-Shamir transform, and applying this anamorphic NIZK within the Naor-Yung paradigm yields recipient anamorphic encryption satisfying several of the strong security notions from recent unified frameworks. Finally, an asymmetric variant called ASY-ANIZK combines a labeled NIZK with public-key encryption satisfying ciphertext pseudorandomness and random ciphertext rejection, separating public embedding from secret recovery and achieving weak robustness, since public embedding precludes the stronger notion.
