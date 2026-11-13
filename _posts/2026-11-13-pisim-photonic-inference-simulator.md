---
title: "PISim: A Unified Photonic Inference Simulator for Hardware-Aware Cross-Layer Design-Space Exploration"
date: 2026-11-13 08:04:00 +0200
categories: [Photonics]
tags: [photonic-computing, neural-accelerators, design-space-exploration]
link: https://arxiv.org/abs/2611.16522
byline: "Andreas Falkenberg (arXiv:2611.16522, Nov 12 2026)"
description: "PISim is an open simulator that couples pretrained neural network execution with physics-based noise models to explore photonic accelerator designs before tape-out."
---

Photonic neural accelerators promise ultra-low latency linear algebra, but their usable numerical precision, sustainable throughput, and application accuracy are tightly bounded by the surrounding electro-optical interfaces and physical non-idealities. The author presents PISim, a unified photonic inference simulator that couples pretrained deep neural network execution with physics-based models of six accelerator architecture families, six electro-optic modulator technologies, four optical source organizations, and both direct and coherent readout schemes. PISim embeds stage-resolved impairment operators, including quantization, finite extinction ratio, shot noise, correlated relative-intensity noise, thermal drift, propagation loss, and channel crosstalk, alongside an analytical cycle-level interface timing model to expose electronic-optical bottlenecks. Using simulated MNIST multilayer perceptron benchmarks, PISim identifies optimal precision operating points under multi-impairment stress, peaking at 6 bits for Mach-Zehnder and microring modulators, quantifies a 52.5 percentage-point accuracy gap between VCSEL-array and parallel-fanout laser architectures arising from power partitioning and correlated source noise, and models interface-limited throughput scaling across emitter-array widths from 32 to 128 channels. The framework is presented as a reproducible foundation for accuracy-constrained design-space exploration prior to photonic chip fabrication.
