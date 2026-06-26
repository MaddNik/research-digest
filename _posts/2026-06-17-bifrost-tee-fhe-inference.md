---
title: "Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving"
date: 2026-06-17 08:23:00 +0200
categories: [FHE]
tags: [fhe, hardware-security]
link: https://arxiv.org/abs/2606.17421
byline: "Chenghao Chen et al. (arXiv:2606.17421, Jun 16 2026)"
description: "A hybrid trusted-execution-environment and FHE serving architecture that delegates linear layers to a CKKS accelerator while keeping non-linear and refresh operations inside a CPU TEE."
---

Bifrost addresses the confidentiality problem in cloud-hosted transformer and large
language model inference, where user prompts can contain sensitive data yet remote
serving exposes intermediate state to the cloud software stack and accelerator
runtime. Fully homomorphic encryption keeps accelerator-side execution
ciphertext-only, but end-to-end inference is expensive because linear layers are
interleaved with non-linear, cache-state, and refresh-sensitive operators. In
Bifrost, secrets are provisioned only to an attested CPU trusted execution
environment, while the accelerator, device memory, driver stack, and host software
stay outside the trusted computing base; FHE serves as a secure delegation
mechanism for projection and feed-forward linear layers on accelerator-backed CKKS,
and non-linear operators, attention control logic, key-value state transitions, and
decrypt-then-encrypt refresh run inside the CPU TEE. A Bifrost+ variant applies a
prefill and decode split so only decode-side state enters the hybrid ciphertext
path. In an estimator-style comparison the authors report latency reductions of
9.25 times on GPT-2 (1.5B) and 9.91 times on LLaMA 3 (8B), and in direct CKKS
deployments Bifrost+ reduces time-to-first-token by 14.6 to 45.8 times on GPT-2
(124M) and 15.3 to 53.4 times on Qwen3 (0.6B).
