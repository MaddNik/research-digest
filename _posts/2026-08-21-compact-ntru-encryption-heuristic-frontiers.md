---
title: "How Compact Can NTRU Encryption Be? Heuristic Frontiers and Practical Schemes"
date: 2026-08-21 08:09:00 +0200
categories: [PQC]
tags: [ntru, ciphertext-compactness, lattice-encoding, ml-kem-comparison]
link: https://eprint.iacr.org/2026/1715
byline: "Yijian Liu et al. (IACR ePrint 2026/1715, Aug 17 2026)"
description: "A theoretical and practical study of how small NTRU-style lattice ciphertexts can be made, culminating in a scheme half the size of ML-KEM-512."
---

The paper studies the limits of compactness for NTRU-style lattice encryption by proposing a unified framework relating compactness to efficiency requirements. It introduces a technique called Free Candidate Localization (FCL) that is applicable broadly across lattice-based schemes and is reported to reduce ML-KEM ciphertext size by about 10 percent with minimal added computational overhead. The authors organize NTRU designs into two frameworks, one leveraging algebraic structure via encoding and one exploiting geometric structure via trapdoors, and derive theoretical compactness frontiers for each. Based on this analysis they propose a concrete instantiation named END. This scheme is reported to achieve a 384-byte ciphertext, exactly half the 768-byte ciphertext size of ML-KEM-512, while keeping computational efficiency comparable to existing designs.
