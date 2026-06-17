---
title: "FEnc2: Unifying Data Packing for Efficient Private Inference via Convolution and Architecture-Aware Fragment Encoding"
date: 2026-06-17 08:21:00 +0200
categories: [FHE]
tags: [private-inference, ckks, ciphertext-packing, cnn]
link: https://arxiv.org/abs/2606.16359
byline: "Ran Ran et al. (arXiv:2606.16359, Jun 15 2026)"
description: "A fragment-based ciphertext packing framework for CKKS private CNN inference that jointly optimizes slot utilization, rotation complexity, and ciphertext density."
---

FEnc2 is a unified, fragment-based encoding framework for CKKS-based private
convolutional neural network inference, motivated by the observation that existing
packing strategies preserve either neighboring data elements or feature grouping
but not both, wasting ciphertext slots and inflating rotations and ciphertext
counts. It has two components: Conv-aware Encoding, which analytically selects an
optimal fragment size to decouple spatial dependencies and jointly minimize inner
and outer rotations across layers, and Arch-aware Ciphertext Compression, which
restores ciphertext density after feature- or channel-reduction layers. Together
these transformations reduce homomorphic operations by one to two orders of
magnitude. At maximum batch size, the authors report end-to-end latency speedups
over the state-of-the-art Orion of up to 228.83 times on GPU and 226.06 times on
CPU for LeNet on MNIST, and up to 4.55 times on GPU and 9.43 times on CPU for
MobileNet on ImageNet. The approach is hardware-agnostic and frames
application-level data layout as a first-order design dimension complementing
primitive-level accelerators.
