---
title: "ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour"
date: 2026-08-28 08:17:00 +0200
categories: [FHE]
tags: [ckks, transformers, homomorphic-inference, automated-search]
link: https://eprint.iacr.org/2026/1817
byline: "Jianhang Xie et al. (IACR ePrint 2026/1817, Aug 27 2026)"
description: "ATLAS automates the search for per-layer polynomial approximation settings needed to run Transformers under CKKS-based fully homomorphic encryption, completing the search in about one hour."
---

Running a Transformer under fully homomorphic encryption is expensive because non-linear operations such as softmax, normalization, and activation must be replaced with polynomial approximations whose depth dominates inference cost, and existing FHE Transformers rely on hand-tuned, uniformly applied approximation settings even though per-layer settings could push the search space to about 10 to the 85th power configurations for BERT and ViT and about 10 to the 228th power for LLaMA3. The authors present ATLAS, a training-free framework that treats each layer's approximation setting as a multi-objective optimization over latency and accuracy, using a two-stage optimization strategy and a surrogate model to complete the search in about one hour despite each configuration taking 70 to 1,000 seconds to evaluate even in cleartext and 85 to 90 percent of configurations being invalid. Compared to an iterative softmax baseline, ATLAS cuts multiplicative depth and end-to-end latency by about 35 percent with little accuracy loss. The framework is demonstrated across encoder-only, decoder-only, and vision Transformers, and the authors position it as complementary to parallel work on packing and matrix multiplication.
