---
title: "EI-DDLGN: Efficient Encrypted Inference with Deep Differentiable Logic Gate Networks under TFHE"
date: 2026-09-18 08:17:00 +0200
categories: [FHE]
tags: [tfhe, programmable-bootstrapping, boolean-circuits, encrypted-inference]
link: https://arxiv.org/abs/2609.13636
byline: "Mahmoud Y. M. Yassin et al. (arXiv:2609.13636, Sep 12 2026, FPS 2026)"
description: "EI-DDLGN shows that Boolean-native Deep Differentiable Logic Gate Networks avoid TFHE's costly arithmetic accumulation, cutting encrypted inference latency by up to 13.4 times."
---

Torus fully homomorphic encryption (TFHE) protects sensitive data during outsourced deep learning inference, but most TFHE-compatible neural network frameworks use arithmetic architectures, which suffer high latency from programmable bootstrapping, accumulator growth, and sensitivity to circuit bit-width. The authors investigate Deep Differentiable Logic Gate Networks (DDLGNs), which learn Boolean computations directly and discretize into fixed logic gate networks, as a Boolean-native alternative whose inference naturally aligns with TFHE's Boolean execution model and avoids arithmetic accumulation in hidden layers. They present EI-DDLGN, described as the first in-depth study of TFHE-based DDLGN inference, and characterize how encrypted execution cost depends on model size, the learned Boolean-function distribution, and propagated wire status. They also introduce Model-Fixed-Wire PBS Bypass, an execution strategy that eliminates unnecessary programmable bootstrapping operations without changing the learned network topology. Across 72 depth-width configurations on MNIST, FashionMNIST, and UCI Phishing, DDLGNs give substantially improved accuracy-latency trade-offs, with EI-DDLGN-Small matching the accuracy of a QAT-FCNN-4 baseline on MNIST while cutting encrypted inference latency by 13.4 times; the paper is accepted at FPS 2026.
