---
title: "Lemur+: Compact Post-Quantum Synchronized Multi-Signatures and Multi-Hop Aggregation"
date: 2026-09-18 08:08:00 +0200
categories: [PQC]
tags: [lattice-signatures, module-lwe, multi-signatures, blockchain]
link: https://eprint.iacr.org/2026/2054
byline: "Yini Lin et al. (IACR ePrint 2026/2054, Sep 16 2026)"
description: "Lemur+ is a lattice-based post-quantum multi-signature scheme that cuts signature size by 8.8 times compared to its predecessor even at one million signers."
---

The authors introduce Lemur+, a compact post-quantum synchronized multi-signature scheme built on standard Module LWE and Module SIS lattice assumptions, aimed at large-scale, long-term distributed applications such as blockchain consensus with non-interactive aggregation. Lemur+ builds on the earlier Lemur scheme from CCS 2026 and maintains an almost constant signature size of about 56 kilobytes even for one million signers over a 42 year key lifetime, compared with 491 kilobytes for Lemur, an about 8.8 times reduction in communication and storage. Their end-to-end implementation shows practical runtime, with 7.75 seconds for signature aggregation and 0.29 seconds for verification at 2^13 signers, within about 2 times the corresponding Lemur runtimes. The core new tool is Homomorphic Vector Commitment with Succinct Opening Proof (HVC-SOP), which augments standard homomorphic vector commitments with succinct opening proofs and, combined with key-homomorphic one-time signatures, yields non-interactive synchronized multi-signatures provably secure against rogue-key attacks. The authors instantiate HVC-SOP using the lattice-based LaBRADOR proof system and further extend Lemur+ to support multi-hop aggregation across distributed network trees.
