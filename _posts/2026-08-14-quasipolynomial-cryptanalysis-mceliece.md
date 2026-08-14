---
title: "Quasipolynomial Cryptanalysis of the McEliece Cryptosystem (or: PIR Meets McEliece)"
date: 2026-08-14 08:13:00 +0200
categories: [PQC]
tags: [classic-mceliece, goppa-codes, distinguishing-attack]
link: https://eprint.iacr.org/2026/1630
byline: "Ashrujit Ghoshal et al. (IACR ePrint 2026/1630, Aug 7 2026)"
description: "A quasipolynomial-time distinguishing attack applies to all Classic McEliece parameter sets evaluated under NIST post-quantum standardization."
---

The authors present an algorithm that distinguishes McEliece public keys, based on binary Goppa codes, from uniformly random matrices with overwhelming advantage, running in quasipolynomial time of n to the O(log n). The attack applies to all Classic McEliece parameter sets that were evaluated during NIST's post-quantum standardization process. Notably, the authors describe the discovery as originating from a failed attempt to construct doubly efficient private information retrieval protocols from algebraic locally decodable codes, connecting two previously separate research areas. They also present a heuristic extension that attempts to recover plaintext from encrypted codewords, though they note this variant remains far from practical for real-world attacks given current computational limits.
