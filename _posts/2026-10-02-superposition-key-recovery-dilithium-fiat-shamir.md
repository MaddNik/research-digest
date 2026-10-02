---
title: "Superposition Key-Recovery Attacks on Dilithium and Fiat-Shamir Signature Schemes"
date: 2026-10-02 08:11:00 +0200
categories: [PQC]
tags: [ml-dsa, dilithium, superposition-attacks, fiat-shamir]
link: https://eprint.iacr.org/2026/2258
byline: "Carlos Cid, David Elkouss, and Manuel Goulão (IACR ePrint 2026/2258, Sep 29 2026)"
description: "New superposition-attack techniques give full quantum key recovery against the original CRYSTALS-Dilithium and its early NIST rounds, but the final standardized ML-DSA resists them."
---

The authors assess the security of ML-DSA, NIST's main standardized signature scheme, and its precursor identification schemes under an extended quantum adversarial model where the adversary can use quantum resources to interact with a prover or signer. They develop new techniques for superposition attacks that realize a relative phase oracle for the least significant bits of a classical function evaluated on a quantum computer, then extend these to a relative phase oracle for arbitrary bits. Leveraging this, they demonstrate full key-recovery attacks on several lattice-based identification schemes by exploiting the affine structure of their output, and extend the attacks to the corresponding Fiat-Shamir signature schemes under reasonable implementation assumptions. This yields full key-recovery attacks in the Q2 model against the original CRYSTALS-Dilithium scheme and the NIST Standardization Rounds 1 and 2 proposals, though the authors find that modifications introduced during the NIST process block their superposition attacks against the final standardized ML-DSA. They identify which specific aspects of the algorithm's execution determine whether the technique applies, expanding the body of work on superposition attacks and quantum security of signature constructions.
