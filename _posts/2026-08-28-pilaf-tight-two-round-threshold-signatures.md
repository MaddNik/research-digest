---
title: "Pilaf: Fully Tight Two-Round Threshold Signatures with Adaptive Corruptions"
date: 2026-08-28 08:27:00 +0200
categories: [Cryptography]
tags: [threshold-signatures, tight-security-proof, adaptive-corruptions, pairing-free]
link: https://eprint.iacr.org/2026/1762
byline: "Chen Qian et al. (IACR ePrint 2026/1762, Aug 21 2026)"
description: "TPilaf is the first two-round, pairing-free threshold signature scheme that combines partially non-interactive signing with a fully tight security proof against adaptive corruptions."
---

Two-round threshold signature schemes let first-round messages, which are independent of the signed message, be preprocessed offline, but this creates tension when a later corruption must reveal randomness consistent with commitments already published in earlier transcripts, and existing adaptive constructions have addressed this by adding rounds, relying on stronger assumptions, or accepting non-tight security losses. The authors construct TPilaf, the first two-round threshold signature scheme combining partially non-interactive signing with a fully tight proof against adaptive corruptions, built in prime-order groups from the MDDH assumption in the random oracle model, where any threshold set of signers can aggregate their second-round shares into a single publicly verifiable signature. The security proof introduces a linearly homomorphic dual-mode commitment with targetable opening, letting the simulator open an already fixed commitment to a target imposed by a later Fiat-Shamir challenge, together with profile-wise zero-sum masking with posterior completion so that corruption openings and signing responses are sampled from the exact conditional distribution. The resulting bound has no combinatorial loss in the number of users, threshold, sessions, or corruption patterns, containing only explicit bad-event and assumption terms.
