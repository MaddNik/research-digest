---
title: "A Time-Encoded Analog Photonic Interposer for Energy-Efficient Integration of Analog Vision Sensors and Analog Accelerators"
date: 2026-09-04 08:04:00 +0200
categories: [Photonics]
tags: [optical-interconnect, analog-computing, chiplet-integration, wavelength-division-multiplexing]
link: https://arxiv.org/abs/2609.03125
byline: "Subhradip Chakraborty et al. (arXiv:2609.03125, Sep 2 2026)"
description: "A time-encoded analog photonic interposer transports analog signals between separated chiplets over a wavelength-division-multiplexed link without an explicit high-precision ADC/DAC pipeline."
---

This work introduces a time-encoded analog photonic interposer that transports analog signals over long distances between spatially separated chiplets with high fidelity, unlike prior silicon-photonic links that are limited to digital data. An analog-to-time converter turns amplitudes into timing intervals, which are sent over a wavelength-division-multiplexed photonic link and reconstructed at the receiver, embedding an implicit 6-bit time-domain quantization while using only a single wavelength per processing element regardless of bit precision. In a fully analog vision pipeline built around an in-pixel computing sensor, the interposer achieves a 2.04 times energy-delay-product improvement over an 8-bit digital electrical baseline on a 560 by 560 Visual Wake Words dataset, with the advantage growing with link length even against a precision-matched 6-bit baseline. The pipeline reaches 89.87 percent and 86.15 percent accuracy on ResNet18 and MobileNetV2 for Visual Wake Words, and stays within 2 percent of the digital baseline on CIFAR-10 and ModelNet40.
