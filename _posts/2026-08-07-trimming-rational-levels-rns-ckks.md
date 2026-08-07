---
title: "Trimming: Decoupling Multiplicative Depth from Modulus Chains in RNS-CKKS via Rational Levels"
date: 2026-08-07 08:23:00 +0200
categories: [FHE]
tags: [ckks, modulus-chain, rns]
link: https://arxiv.org/abs/2608.00375
byline: "John Chiang (arXiv:2608.00375, Aug 1 2026)"
description: "Introduces Trimming, a rational-level abstraction for RNS-CKKS that lets multiplicative depth be managed by partial modulus transitions rather than by removing whole factors."
---

The paper builds on prior work called Grafting that decoupled scale factors from ciphertext moduli in CKKS to improve precision handling. Trimming extends this idea by using an auxiliary chain of smaller modulus factors, allowing the scheme to make partial depth transitions instead of dropping an entire modulus factor at once. This is framed through a rational-level abstraction that stays compatible with existing RNS-CKKS operations, aiming to give more flexible depth management and adaptive modulus transitions. The author positions Trimming as complementary to Grafting, addressing depth-management limitations in RNS-CKKS. Per the abstract, implementation and experimental validation of the technique are described as forthcoming work, so no benchmark results are reported yet.
