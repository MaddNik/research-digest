---
title: "BMRaccoon: Blind Multi-Signatures from Lattices"
date: 2026-11-13 08:09:00 +0200
categories: [PQC]
tags: [lattice-cryptography, blind-signatures, multi-signatures, raccoon]
link: https://eprint.iacr.org/2026/2870
byline: "Keerthi Aiswarya Varshini et al. (IACR ePrint 2026/2870, Nov 11 2026)"
description: "BMRaccoon is the first lattice-based post-quantum blind multi-signature scheme, built on a two-round protocol compatible with Raccoon signatures."
---

Blind multi-signatures let a user obtain a compact signature on a hidden message through the joint participation of multiple signers, providing a basis for decentralized issuance of anonymous tokens. The authors present BMRaccoon, the first lattice-based post-quantum blind multi-signature construction, with a two-round signing protocol that is secure under concurrent sessions and produces signatures syntactically compatible with Raccoon signatures under the sum of the signers' verification keys. As a building block, they introduce MRaccoon, the first Raccoon-based multi-signature scheme, and prove its strong unforgeability under the Algebraic One-More MISIS and MSIS assumptions in the random oracle and knowledge-of-secret-key models. Their modular security analysis establishes one-more unforgeability of BMRaccoon through a straight-line reduction to the strong unforgeability of MRaccoon, modeling the user's blinding contribution as an auxiliary signer with a zero verification key, and they additionally prove blindness against malicious, colluding signers. For up to 2 to the power of 32 signing sessions and 32 signers, the concrete instantiation yields signatures of about 67 kilobytes and verification keys of about 15 kilobytes.
