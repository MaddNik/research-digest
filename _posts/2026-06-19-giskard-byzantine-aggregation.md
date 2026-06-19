---
title: "Giskard: Byzantine Robust and Confidential Aggregation for Large-Scale Decentralized Learning"
date: 2026-06-19 08:13:00 +0200
categories: [Cryptography]
tags: [secure-multiparty-computation, bgw, byzantine-robustness, secure-aggregation]
link: https://arxiv.org/abs/2606.19129
byline: "Ousmane Touat et al. (arXiv:2606.19129, Jun 17 2026)"
description: "A committee-tree MPC protocol that achieves confidential, Byzantine-robust aggregation while avoiding all-to-all communication."
---

Giskard tackles the joint goal of confidentiality and Byzantine robustness in large-scale
decentralized aggregation. It organizes n parties into a tree of committees of size order
log n and uses BGW-style secure multi-party computation within each committee to compute
robust aggregates. The protocol evaluates coordinate-wise approximate medians through a
distributed binary search, which lets it resist malicious inputs while keeping
communication manageable. The authors report comparable model utility under up to n over 4
Byzantine parties while reducing communication complexity relative to all-to-all
approaches. The contribution centers on the cryptographic aggregation mechanism rather than
on the learning task itself.
