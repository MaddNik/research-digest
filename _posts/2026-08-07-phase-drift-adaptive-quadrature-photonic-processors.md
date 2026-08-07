---
title: "Phase-Drift Limits and Adaptive Quadrature Readout in Programmable Photonic Processors"
date: 2026-08-07 08:09:00 +0200
categories: [Photonics]
tags: [photonic-computing, programmable-photonics, coherent-detection]
link: https://arxiv.org/abs/2608.02249
byline: "Gokhan Elmas, Igor A. Litvin, and Janis Notzel (arXiv:2608.02249, Aug 3 2026)"
description: "A theoretical and experimental study quantifies how phase drift between sequential quadrature measurements degrades programmable photonic processors, and proposes an adaptive readout order that cuts the error by 84.9 percent."
---

Programmable photonic processors rely on coherent interference, so phase fluctuations between optical inputs limit their accuracy, particularly when sine and cosine quadratures must be measured one after another instead of simultaneously. Using 35 free-running recordings of 300 seconds each, taken at about 125 samples per second per channel from an eight-mode programmable photonic processor, the authors derive closed-form error expressions for the standard fixed-order quadrature readout. They show that a phase-predicted ordering rule, which measures the less informative quadrature first and the more informative one second, reduces the first-order drift error by 84.9 percent relative to fixed ordering. They further derive an increment-aware estimator from a local state-space model showing how marginalizing an unknown phase increment lowers the Fisher information of a stale measurement. Monte Carlo simulations validate these perturbative results and compare simultaneous, fixed-order, increment-aware, and adaptive receiver strategies under a common noise model.
