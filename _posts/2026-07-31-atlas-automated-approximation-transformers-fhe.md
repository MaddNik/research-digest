---
title: "ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour"
date: 2026-07-31 08:15:00 +0200
categories: [FHE]
tags: [ckks, transformer-inference, approximation-search]
link: https://arxiv.org/abs/2607.23478
byline: "Jianhang Xie et al. (arXiv:2607.23478, Jul 26 2026)"
description: "ATLAS automates per-layer approximation configuration for transformer models under CKKS-based FHE inference by formulating it as a multi-objective optimization problem."
---

Deploying transformer models under FHE requires replacing non-linear operations with polynomial approximations compatible with CKKS, and different layers can tolerate different levels of approximation error. ATLAS formulates the choice of per-layer approximation settings as a multi-objective optimization over latency and predictive accuracy, rather than using a uniform configuration across all layers. The search space can reach on the order of 10 to the 225th power configurations for large models, so the authors use a two-stage optimization strategy combined with surrogate models to make evaluation tractable. The paper also notes that 35 to 50 percent of candidate configurations yield numerically invalid solutions, motivating their search-signal handling.
