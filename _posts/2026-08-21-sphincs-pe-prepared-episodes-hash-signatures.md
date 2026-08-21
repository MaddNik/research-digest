---
title: "Prepared Episodes for Short Online Hash Based Signatures"
date: 2026-08-21 08:11:00 +0200
categories: [PQC]
tags: [hash-based-signatures, sphincs-plus, slh-dsa, signature-compression]
link: https://eprint.iacr.org/2026/1708
byline: "Chongxu Ren et al. (IACR ePrint 2026/1708, Aug 17 2026)"
description: "SPHINCS-PE reduces SPHINCS+/SLH-DSA signature sizes by precomputing an upper hypertree segment ahead of message arrival."
---

The paper proposes SPHINCS-PE, a variant of the SPHINCS+ hash-based signature scheme, aimed at its main drawback of large signature sizes despite being stateless and self-contained to verify. The construction divides the hypertree at an episode boundary so that an upper portion of the tree can be prepared before a message is known, which then reduces the size of the FORS and WOTS+ components carried in each final signature. Compared to the FIPS 205 SLH-DSA standard, the authors report signature size reductions of 3 to 12 percent for parameter profiles optimized for short signatures and 25 to 40 percent for profiles optimized for speed. When combined with cached certificates, they report additional reductions of 24 to 70 percent in the online signature size, while preserving self-contained verification.
