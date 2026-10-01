---
title: "An Open-Source End-to-End FHE Implementation for Privacy-Preserving Llama 3 8B Inference"
date: 2026-09-18 08:19:00 +0200
categories: [FHE]
tags: [ckks, llm-inference, ciphertext-packing, gpu-acceleration]
link: https://arxiv.org/abs/2609.12378
byline: "Yuhang Fan et al. (arXiv:2609.12378, Sep 11 2026)"
description: "Odin is an open-source, GPU-accelerated CKKS implementation that runs full Llama 3 8B inference under FHE in about 366 seconds, a 4.51 times speedup over a prior baseline."
---

Cloud LLM services typically require users to send prompts in the clear, creating a privacy risk that fully homomorphic encryption can address by letting a server compute on ciphertexts, but the packing scheme that maps logical tensors to ciphertexts and slots in CKKS-based inference strongly determines ciphertext count, computational cost, and how data pass between linear layers, attention, and nonlinear computation. The authors present Odin, an FHE inference system that co-designs ciphertext packing and model execution for Llama, starting from a THOR-style baseline whose bottleneck is weight encoding. Odin uses a feature-major cross-layer layout to unify residual connections and layer interfaces and builds transient intra-operator layouts for linear projections and attention, reducing redundant plaintext encoding of weights in wide projections, and it lets QK^T scores feed directly into Softmax and PV consume the resulting probabilities without intermediate repacking. For nonlinear operations it uses minimax polynomial approximation with input-range control and joint error allocation guided by model quality to reduce polynomial degree and multiplicative depth. With Llama-3-8B weights and a 128-token input, Odin evaluates all 32 Transformer layers on a single NVIDIA H100 80 GB GPU in 366.4 seconds and 58.9 GiB peak memory, compared with 1651.9 seconds for THOR under the same settings, a 4.51 times speedup, and the authors describe it as the first open-source end-to-end GPU CKKS implementation of Llama-3.
