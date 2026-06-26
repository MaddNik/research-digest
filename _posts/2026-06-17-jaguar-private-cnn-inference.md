---
title: "Jaguar: Fast Private CNN Inference with Power-of-Two Homomorphic Arithmetic"
date: 2026-06-17 08:20:00 +0200
categories: [FHE]
tags: [fhe, hardware-acceleration, mpc]
link: https://arxiv.org/abs/2606.11827
byline: "Yewon Jeong et al. (arXiv:2606.11827, Jun 10 2026)"
description: "A hybrid homomorphic-encryption and two-party-computation CNN inference system built around a power-of-two ciphertext ring to speed up convolution and truncation."
---

Jaguar targets the bottleneck in hybrid homomorphic-encryption and
two-party-computation private convolutional neural network inference, which arises
from prime-modulus homomorphic arithmetic in convolution and from running ReLU at
doubled bitwidth before a separate truncation protocol. The system is built on a
single design choice, a power-of-two ciphertext ring, which addresses both issues.
It enables a coefficient-domain convolution kernel that replaces transform-centric
polynomial multiplication with scalar-polynomial accumulation, and an exact
ciphertext-side truncation by local right shifts so ReLU runs directly at the
target fixed-point precision. Where the number theoretic transform remains useful,
at the client for the single polynomial multiplication during decryption, it is
recovered through an auxiliary transform prime while keeping decryption order N log
N. On ImageNet-scale ResNet-18, ResNet-50, and MobileNetV2 with AVX disabled,
Jaguar reports 2.07 to 3.72 times lower end-to-end latency than Cheetah and 2.16 to
3.36 times lower than Rhombus, with 1.16 to 1.76 times lower communication than
Cheetah.
