---
title: "Nothing Up My Matrix: Kleptographic Backdoors in ZK-friendly Hash Functions"
date: 2026-09-11 08:24:00 +0200
categories: [Cryptography]
tags: [kleptography, zk-friendly-hashing, backdoors, algebraic-cryptanalysis]
link: https://eprint.iacr.org/2026/1901
byline: "Hyunsik Jeong et al. (IACR ePrint 2026/1901, Sep 6 2026)"
description: "A malicious matrix generator for the linear layer of zero-knowledge-friendly hash functions can plant a kleptographic backdoor that still passes standard MDS security checks, with demonstrated attacks against Plonky2, Plonky3, and Neptune Cash."
---

Zero-knowledge-friendly hash functions built from algebraic SPN permutations rely on a linear-layer matrix for diffusion, but there is no uniform convention for selecting that matrix, and some specifications simply accept any MDS matrix or let implementations swap in alternative instantiations. The authors show that this freedom creates a kleptographic attack surface: a malicious designer who controls matrix selection can choose a matrix that maps a chosen input to a chosen output under appropriate round and parameter conditions, while the resulting matrix remains MDS and passes the additional security checks required by the target primitive. Three case studies illustrate the real-world impact: in Plonky3 the backdoor would let a prover control a Fiat-Shamir challenge and make a verifier accept an invalid claim, in Neptune Cash it would permit a digest collision enabling counterfeit currency, and in Plonky2 it would enable a forged Merkle-tree membership proof. The authors conclude that satisfying MDS and other algebraic checks is insufficient to trust a matrix; its generation process must also be transparent and verifiable.
