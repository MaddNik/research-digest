---
title: "Anonymous Attribute-Based Signcryption: Definitions, Constructions, and Applications"
date: 2026-09-04 08:19:00 +0200
categories: [Cryptography]
tags: [attribute-based-encryption, signcryption, matchmaking-encryption, lattice-based]
link: https://eprint.iacr.org/2026/1861
byline: "Yongkang Lang et al. (IACR ePrint 2026/1861, Sep 2 2026)"
description: "A new primitive, anonymous attribute-based signcryption, adds ciphertext anonymity to attribute-based signcryption and yields a lattice-based general-policy construction with post-quantum security, plus generic constructions of matchmaking encryption."
---

The authors introduce anonymous attribute-based signcryption (A2BSC), a generalization of attribute-based signcryption that, beyond message confidentiality and ciphertext unforgeability, additionally requires ciphertext anonymity: no information about the signcryptor's attributes or about the ciphertext's attributes or policy leaks, regardless of the decryption outcome. They establish syntax and security notions for A2BSC within a unified framework covering key-policy, ciphertext-policy, dual-policy, and a hierarchical dual-policy variant called Special A2BSC, and construct a Special A2BSC scheme for general policies modeled as bounded-depth Boolean circuits from the succinct learning with errors and basis-augmented short integer solution assumptions in the standard model, giving post-quantum security and lattice-based instantiations of both ciphertext-policy and dual-policy A2BSC. As an application, the authors show A2BSC's generality by giving generic constructions of matchmaking encryption and arranged matchmaking encryption for arbitrary policies against unbounded collusions, and by strengthening the CPA-privacy of these primitives to CCA security, which their construction achieves for free since A2BSC natively provides CCA security. This is a major revision of a paper accepted at Asiacrypt 2026.
