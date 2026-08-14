---
title: "On the Sensitivity to Errors in Homomorphic Computing: Single Transient Bit-flip Client-side Error Characterization"
date: 2026-08-14 08:20:00 +0200
categories: [FHE]
tags: [fault-injection, ckks, silent-data-corruption]
link: https://arxiv.org/abs/2608.11155
byline: "Matias Mazzanti et al. (arXiv:2608.11155, Aug 11 2026)"
description: "Client-side single transient bit-flip faults in CKKS homomorphic encryption identify homomorphic multiplication as the most error-sensitive operation, exposing a silent-data-corruption risk."
---

Homomorphic encryption's security relies on injected noise, and the authors argue this same noise reliance creates intrinsic sensitivity to bit-level faults that can evade traditional fault-detection mechanisms, leading to silent data corruption in domains such as healthcare, finance, and government that might deploy encrypted computation. Focusing on CKKS, which is widely used for approximate arithmetic in AI and machine learning workloads, the paper analyzes how single transient bit-flip faults on the client side propagate and amplify through the computation. The authors identify homomorphic multiplication as the most error-sensitive operation in practical HE pipelines and characterize the propagation and amplification behavior, framing this as exposing a robustness vulnerability that motivates more fault-resilient HE deployments. This is a companion study to a separate paper by an overlapping author team examining server-side transient errors in CKKS multiplication.
