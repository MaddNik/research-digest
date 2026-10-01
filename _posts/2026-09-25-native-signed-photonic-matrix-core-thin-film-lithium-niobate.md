---
title: "A native signed incoherent photonic matrix core on thin-film lithium niobate supporting in situ backpropagation"
date: 2026-09-25 08:02:00 +0200
categories: [Photonics]
tags: [thin-film-lithium-niobate, photonic-computing, optical-matrix-multiplication, in-situ-training]
link: https://arxiv.org/abs/2609.27709
byline: "Yuan Ren et al. (arXiv:2609.27709, Sep 23 2026)"
description: "A 16 by 16 thin-film lithium niobate photonic core natively multiplies signed numbers and trains itself through in situ backpropagation."
---

This paper presents a signed incoherent optical matrix multiplier built on thin-film lithium niobate that natively supports signed inputs and weights, avoiding the extra encoding overhead many photonic accelerators need to represent negative numbers. The authors demonstrate closed-loop in situ backpropagation on a 16 by 16 photonic core, covering forward computation, nonlinear operations, error propagation, and gradient computation, so that measured physical outputs directly participate in optimization and actual device nonidealities are incorporated into training. The core achieves 8-bit multiplication and 10-bit accumulation precision across 256 channels, and maintains 10-bit accuracy in tiled 256 by 256 matrix computation. It further executes Transformer linear operations in a BERT-mini workload. The authors present this as a scalable building block for large-scale, high-efficiency photonic neuromorphic systems.
