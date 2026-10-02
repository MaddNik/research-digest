---
title: "Decryption Failures in NGCC Lattice KEMs: Correlated Blocks, Omitted Compression Noise, and Failure Boosting under a Query Cap"
date: 2026-10-02 08:15:00 +0200
categories: [PQC]
tags: [ngcc, lattice-kem, decryption-failure-rate, key-encapsulation]
link: https://eprint.iacr.org/2026/2250
byline: "Yuyang Xiao (IACR ePrint 2026/2250, Sep 28 2026)"
description: "Recomputing decryption failure rates for several NGCC first-round lattice KEMs finds three distinct modeling gaps that push some candidates' estimated failure costs below their claimed security levels."
---

The Chinese NGCC post-quantum competition received a family of lattice key encapsulation mechanisms whose decryption failure rates are certified by their designers using models that differ in detail, and the author recomputes the failure probability for first-round candidates whose claimed rate, or a simple recomputation of it, sits near or below the nominal level. Three mechanisms matter: correlated decoding blocks in DTRU, where paired octets place the same bit on both halves of a repetition code, raise the estimated decryption failure rate of six of seven parameter sets by roughly 50 to 110 bits, putting DTRU-648, DTRU-768, and DTRU-Prime within a 2 to the 64th power query budget after a modest number of offline encapsulations; omitted compression noise in Cheetah, where the specification's DFR analysis leaves out a public-key cross term, gives revised estimates of 2 to the negative 79.1 and negative 51.8 power for its two parameter sets rather than the claimed 2 to the negative 129 and negative 176; and bounded noise in the two-dimensional B2-Minal codes used by Rudraksh2 and Scabbard, where rederived two-dimensional tail estimates come out a few bits below the claimed levels. The author stresses that no attack described in the paper recovers a key; the results describe estimated first-failure costs under a 2 to the 64th or 2 to the 80th power query cap, subject to the paper's stated modeling and extrapolation limitations.
