---
title: "Encrypt What Matters: When Selective Homomorphic Inference Is Efficient"
date: 2026-09-11 08:18:00 +0200
categories: [FHE]
tags: [selective-encryption, homomorphic-inference, model-architecture]
link: https://arxiv.org/abs/2609.09357
byline: "Ali Backour et al. (arXiv:2609.09357, Sep 8 2026)"
description: "Encrypting only a sensitive region of interest rather than an entire input can give order-of-magnitude homomorphic inference speedups, but only for neural network architectures that keep computation local."
---

Fully homomorphic encryption (FHE) allows inference on private data without revealing it to the server, but evaluating an entire input under FHE is expensive. The authors study selective homomorphic inference, where only a sensitive region of interest is encrypted and computations independent of that region are performed in plaintext, producing the same output as full FHE evaluation on the same model without retraining. They find that the efficiency of this approach depends on how quickly encrypted dependencies spread through the network: for small encrypted regions of interest, locality-preserving architectures can achieve order-of-magnitude speedups in homomorphic evaluation, while architectures with early global mixing provide essentially no speedup. The results identify locality as the key architectural property that determines whether selective homomorphic inference is worthwhile.
