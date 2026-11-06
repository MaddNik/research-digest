---
title: "Revisiting Hash-ECB-Hash Enciphering: Plaintext Recovery Attacks on PEP and TET"
date: 2026-11-06 08:25:00 +0200
categories: [Cryptography]
tags: [tweakable-encryption, disk-encryption, plaintext-recovery, pep-tet]
link: https://eprint.iacr.org/2026/2691
byline: "Hailun Yan et al. (IACR ePrint 2026/2691, Oct 30 2026)"
description: "Classical attacks break the length-preserving PEP and TET tweakable enciphering schemes, exposing a repeating-coefficient flaw in PEP and encryption-decryption mismatches in TET."
---

Storage encryption often relies on tweakable enciphering schemes that encrypt an entire multi-block data unit without expanding its length, using a public tweak to bind it to its context. This paper revisits PEP, from FSE 2006, and TET, from CRYPTO 2007, two Hash-ECB-Hash designs that combine parallel block-cipher calls with invertible mixing, and presents classical distinguishing and plaintext-recovery attacks on both. For PEP, the authors exhibit a fixed public field, satisfying the scheme's own published parameter-selection rule, whose generated position coefficients repeat, yielding a two-query algebraic distinguisher, recovery of a secret tweak-derived value with a single encryption query, and recovery of target plaintexts over a range of block lengths using at most nine encryption queries and one decryption query. For TET, they analyze two proposed corrections to a previously reported encryption-decryption mismatch and find that both admit two-query distinguishers on messages with a partial final block; for tails of at least two bits, they achieve deterministic plaintext recovery with two decryption queries under one correction, or two encryption queries plus one decryption query under the other. These TET attacks hold for every data permutation and valid parameter choice, exposing concrete weaknesses in coefficient generation and partial-block handling that any repair of these constructions must address.
