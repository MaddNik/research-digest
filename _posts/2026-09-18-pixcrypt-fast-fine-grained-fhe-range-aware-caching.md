---
title: "PixCrypt: Fast Fine-Grained FHE with Range-Aware Caching"
date: 2026-09-18 08:16:00 +0200
categories: [FHE]
tags: [ckks, bfv, bgv, ciphertext-caching]
link: https://arxiv.org/abs/2609.14137
byline: "Chao Wang et al. (arXiv:2609.14137, Sep 12 2026, ICICS 2026)"
description: "PixCrypt uses a range-aware ciphertext cache to speed up fine-grained FHE image analytics by up to 35 times while cutting the need for bootstrapping."
---

Fine-grained encrypted analytics, such as pixel-level tumor segmentation or anomaly detection, need fully homomorphic encryption's ability to compute arbitrary operations on encrypted data, but FHE remains computationally expensive for both software and hardware accelerators, and alternatives like MPC, differential privacy, or partially homomorphic encryption each fall short for this setting. The authors present PixCrypt, a caching-based acceleration mechanism for fine-grained FHE that replaces expensive fresh-ciphertext generation with cache retrieval and coefficient-level operations, working across the CKKS, BFV, and BGV schemes, while randomized reconstruction ensures ciphertexts do not repeat. Its linear noise growth reduces how often bootstrapping is needed and lowers NTT load, which the authors say improves hardware accelerator efficiency. PixCrypt yields up to 35 times faster fine-grained encryption while maintaining IND-CPA security, and experiments on five real-world pixel-level image processing tasks show it improves the practicality of FHE for privacy-preserving analytics. The paper is accepted at ICICS 2026.
