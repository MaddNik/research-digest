---
title: "When Every Simulation Counts: Value-Based Reinforcement Learning for Accelerated Photonics Inverse Design"
date: 2026-07-31 08:06:00 +0200
categories: [Photonics]
tags: [photonic-computing, inverse-design, reinforcement-learning]
link: https://arxiv.org/abs/2607.23469
byline: "Longying Wen et al. (arXiv:2607.23469, Jul 26 2026)"
description: "A comparison of value-based reinforcement learning algorithms for optimizing photonic-crystal surface-emitting laser designs finds Dueling DQN the most reliable choice under a tight simulation budget."
---

The authors study reinforcement learning methods for inverse design of photonic-crystal surface-emitting lasers under strict computational constraints, comparing a baseline deep Q-network against six value-based variants across a seven-variable design problem with a budget of only 83 simulations. Their results show that Dueling DQN was the only variant to improve outcomes across all four random seeds tested. Relative to the initial designs, the structures selected by Dueling DQN showed improvements in quality factor, wavelength accuracy, and output power. The authors conclude that Dueling DQN is the most dependable choice among the variants tested for simulation-constrained inverse design optimization, a setting where each electromagnetic simulation is computationally expensive.
