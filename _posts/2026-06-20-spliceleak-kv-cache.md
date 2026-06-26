---
title: "Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG"
date: 2026-06-20 08:14:00 +0200
categories: [Hardware Security]
tags: [side-channel, machine-learning]
link: https://arxiv.org/abs/2606.21842
byline: "Sun et al. (arXiv:2606.21842, Thu 20 Jun 2026)"
description: "First end-to-end side-channel attack on non-prefix KV cache fusion extracting semantic content token-by-token from LLM serving."
---

Large-language model serving systems increasingly use Key-Value cache fusion and Retrieval-Augmented Generation to accelerate multi-tenant inference, yet existing side-channel attacks assume strict linear prefix alignment that renders them ineffective against real-world RAG queries containing unique private prefixes. This work uncovers a critical class of structural vulnerabilities in chunk-aware memory scheduling where deterministic micro-architectural mechanisms used to align and fuse disjoint memory chunks leak a continuous timing signature. The researchers introduce SpliceLeak, the first end-to-end side-channel attack on non-prefix KV cache fusion, executing a two-phase privacy breach: first structurally fingerprinting the exact length of hidden private prompts, then manipulating boundary collisions to extract exact semantic content token-by-token. Evaluations on production frameworks (vLLM with LMCache) achieve up to 100 percent extraction success rate in bounded-entropy scenarios. The attack requires as few as 63 requests per token despite realistic continuous batching noise. To resolve the inherent conflict between memory deduplication and security, the authors propose SpliceDefense, combining Quantized Chunk Padding and Constant-Time Boundary Fusion to flatten the side-channel signal with negligible throughput overhead.
