---
title: "ML-Assisted Power Side-Channel Attacks on ML Accelerators in Shared FPGAs"
date: 2026-10-16 08:32:00 +0200
categories: [Hardware Security]
tags: [fpga-security, power-side-channel, multi-tenant-fpga, model-extraction]
link: https://arxiv.org/abs/2610.16164
byline: "Anthony Etim et al. (arXiv:2610.16164, Oct 12 2026)"
description: "The first on-chip time-to-digital-converter attack to reconstruct full-color, ImageNet-scale images processed by a victim's machine learning accelerator on a shared FPGA combines on-chip power sensing with machine-learning-based upscaling."
---

Cloud providers now offer on-demand, multi-tenant FPGAs that let multiple users share a single device, which introduces the risk that a co-located adversary can mount power side-channel attacks against a victim's machine learning accelerator. Prior on-chip attacks using time-to-digital-converter sensors had only recovered small, MNIST-scale grayscale inputs, even with machine-learning-assisted reconstruction, but this work demonstrates the first on-chip, TDC-based attack to produce full-scale color reconstructions of ImageNet-scale inputs by combining machine-learning-based upscaling and recoloring with TDC measurements of a remote victim's accelerator. The authors frame the work as a proof-of-concept leakage study where the victim runs the first convolution layer of a CNN on 224 by 224 ImageNet inputs on a shared FPGA, and they quantify how much of each reconstruction reflects genuinely recovered information versus machine-learning-generated post-processing. As a preliminary countermeasure they study a pixel-substitution defense that replaces each pixel with one of different Hamming weight within a fixed intensity budget, and find that this transformation costs the victim's own model more accuracy than it costs the attacker, and because it applies the same fixed mapping to every image it is largely defeated by an attacker retrained on transformed data, meaning robust defenses will need randomized or input-dependent transformations.
