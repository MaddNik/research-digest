---
title: "Combinatorial Lock for Trojan-Resilient AI Engines via Hash-Assisted Spectral Filtering"
date: 2026-10-30 08:39:00 +0200
categories: [Hardware Security]
tags: [hardware-trojan, backdoor-defense, fpga, asic]
link: https://arxiv.org/abs/2610.33437
byline: "Soumita Chatterjee et al. (arXiv:2610.33437, Oct 24 2026)"
description: "Combinatorial Lock is a training-free, hardware-implementable defense against multi-trigger backdoor attacks on AI models, cutting attack success rates to as low as 0.1 percent while keeping 97.8 percent clean accuracy, with ASIC and FPGA implementations adding only 19 to 20 percent latency."
---

Multi-trigger backdoor attacks, where heterogeneous trigger mechanisms such as patch, blend, warping, and latent-domain triggers coexist within a single poisoned model, defeat existing shortcut-based defenses that assume a single static attack mechanism, and current multi-trigger remedies rely on backdoor unlearning, which is costly to train and loses effectiveness at low poisoning ratios. This paper proposes Combinatorial Lock, a training-free, reference-calibrated defense that reduces multi-trigger identification to a combinatorial problem over binary activation signatures, a formulation the authors say is the key novelty since it is trigger-oblivious and directly implementable in hardware using integer and logic operations. The framework combines anomaly-gated spectral scrubbing, which removes a malicious subspace only from inputs flagged as anomalous, with a hash-compressed combinatorial signature checked by an ensemble of detection experts including one aware of compound attacks, and a joint threshold-shrinkage search identifies an operating point that reduces attack success rate to as low as 0.1 percent while preserving 97.8 percent clean accuracy. Evaluated on six models including ResNet18, VGG16, MobileNet, AlexNet, ViT-Small, and ViT-Base, near-100 percent attack success rates drop to single digits across poisoning rates of 1 to 10 percent and 1 to 9 simultaneous triggers, and ASIC and FPGA implementations confirm practicality, adding a consistent 19 to 20 percent latency overhead across all evaluated architectures.
