---
title: "Error Propagation-Aware Scale Design for Efficient Homomorphic Encryption-Based LLM Inference"
date: 2026-10-02 08:22:00 +0200
categories: [FHE]
tags: [ckks, llm-inference, bootstrapping, scale-optimization]
link: https://eprint.iacr.org/2026/2242
byline: "Sieun Seo and Chohong Min (IACR ePrint 2026/2242, Sep 28 2026)"
description: "Tracking how numerical error propagates through a CKKS-encrypted Transformer lets this scheme allocate precision per operation, cutting bootstrapping calls by up to 83.6 percent."
---

Homomorphic encryption enables privacy-preserving inference by letting neural networks operate directly on encrypted data, but the computational cost remains a major obstacle to deploying large language models this way, since CKKS-based inference consumes ciphertext modulus with every homomorphic multiplication and needs costly bootstrapping once the available modulus runs out. The authors propose an error-propagation-aware scale design for CKKS-based privacy-preserving LLM inference, characterizing the numerical errors introduced by individual homomorphic operations and analyzing how those errors propagate through subsequent Transformer computations. Based on this analysis, they quantify how much each local error contributes to the final inference error and use that to determine the precision each operation actually needs, allocating operation-wise scales and modulus levels accordingly instead of applying uniformly conservative precision. This lets more computation fit within a given modulus chain, reducing how often costly bootstrapping has to run while keeping the target inference accuracy. Compared with the prior system THOR, the method cuts modulus consumption by 30.0 percent and the number of bootstrapping operations by 83.6 percent on a standard Transformer, and for an HE-friendly Transformer it cuts modulus consumption by 33.6 percent and bootstrapping operations by 80 percent compared with PowerFormer.
