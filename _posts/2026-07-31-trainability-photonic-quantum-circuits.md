---
title: "The Trainability of Photonic Quantum Circuits"
date: 2026-07-31 08:01:00 +0200
categories: [Photonics]
tags: [quantum-photonics, variational-quantum-computing, linear-optics]
link: https://arxiv.org/abs/2607.21544
byline: "Alexander Makarovskiy et al. (arXiv:2607.21544, Jul 23 2026)"
description: "The paper introduces a trainability metric for passive linear-optical quantum circuits, identifying which observable classes can be optimized efficiently and which suffer exponential sampling costs."
---

The authors introduce a trainability metric based on the ratio of sample variance to circuit variance, which determines how many circuit samples are needed to resolve small differences in loss and gradients to a given accuracy. Applying this to photon-number observables in linear-optical circuits, they identify regimes that are trainable and regimes that are not. They find that fixed-order photon-number polynomials need only a polynomial number of samples as system size grows, while higher-order polynomials and observables built from output probabilities generally need an exponential number of samples. Within the trainable regime they identify observable classes where quantum estimation gives a polynomial speedup over several classical methods, including a practical neural-network-based observable construction. The work positions photonic variational quantum computing as viable for near-term applications, at least for the identified trainable observable classes.
