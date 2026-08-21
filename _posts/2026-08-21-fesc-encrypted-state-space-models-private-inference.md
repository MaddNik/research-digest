---
title: "FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models"
date: 2026-08-21 08:18:00 +0200
categories: [FHE]
tags: [private-inference, state-space-models, hybrid-fhe-mpc, ckks]
link: https://arxiv.org/abs/2608.17442
byline: "Yufan Zhu et al. (arXiv:2608.17442, Aug 18 2026)"
description: "A hybrid FHE-MPC system makes private inference over long documents practical by encrypting selective state-space models instead of Transformer attention."
---

The paper targets privacy-preserving inference over long, sensitive documents, where prior private-inference systems that encrypt Transformer attention are bottlenecked by attention's quadratic cost in sequence length. The authors turn instead to selective state-space models (SSMs), which offer linear-time recurrence in plaintext but, the paper notes, incur linear multiplicative depth, sequence-wide state residency, or dense FHE-to-MPC conversion overhead when implemented directly under encryption. Their system, called Factorized Encrypted Scan-Contract (FESC), is a hybrid FHE-MPC design whose factorized scan-contract mechanism keeps input-dependent state transitions compact across FHE and MPC conversion boundaries, composes them without dense expansion, streams state chunks on demand, and contracts outputs before conversion. They show the scan-contract interface is compatible across both invariant and selective SSM architectures, and for a Mamba-2 instantiation they build GPU-optimized CKKS kernels for linear computations plus MPC protocols for the nonlinear functions SiLU, softplus, exponential, and RMSNorm, using approximation-aware fine-tuning. The authors report FESC is, to their knowledge, the first private long-document inference system to run natively end to end at sequence lengths of 1,024 tokens or more on a single GPU, with a twelve-layer Mamba-base model completing inference on a 2,048-token sequence in 77.3 minutes on one A100 GPU at a peak memory footprint of 32.7 gigabytes, while maintaining accuracy close to the unencrypted baseline on the long-document tasks evaluated.
