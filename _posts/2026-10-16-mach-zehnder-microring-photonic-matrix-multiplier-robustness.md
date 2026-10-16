---
title: "Comparative Robustness of Mach-Zehender and Microring Photonic Matrix Multipliers Under Laser RIN and Thermal Drift"
date: 2026-10-16 08:02:00 +0200
categories: [Photonics]
tags: [photonic-matrix-multiplier, mach-zehnder-modulator, microring-resonator, optical-neural-networks]
link: https://arxiv.org/abs/2610.15400
byline: "Andreas Falkenberg (arXiv:2610.15400, Oct 11 2026)"
description: "A simulation study compares how Mach-Zehnder modulator and microring-resonator photonic matrix multipliers tolerate laser relative-intensity noise and thermal drift during neural-network inference."
---

Photonic matrix multipliers can accelerate neural-network inference, but their practical value depends on how the optical weight elements hold up against source noise, thermal variation, and calibration error. This paper compares Mach-Zehnder modulator and microring-resonator implementations under laser relative-intensity noise, column-wise thermal and phase drift, and their combined effect. Two CIFAR-10 classifiers, a compact four-layer CNN and a ResNet-8, are mapped onto matched photonic multiply-accumulate chains that share the same source, detection, numerical, and calibration assumptions, reproducing baseline accuracies of 79.5 percent and 70.0 percent respectively with no perturbation. Robustness is then evaluated with separate noise-only and drift-only sweeps plus a joint two-dimensional grid spanning perturbation levels from 0.5 percent to 20 percent, reporting classification accuracy, confusion matrices, and response surfaces. The work provides a controlled, device-model-based framework for comparing interferometric and resonant photonic weight elements, with conclusions limited to the implemented models, perturbation ranges, and workloads.
