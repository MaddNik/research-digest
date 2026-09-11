---
title: "VERA: VERifiable Microarchitectural Monitoring for Adversarially Robust Edge AI"
date: 2026-09-11 08:29:00 +0200
categories: [Hardware Security]
tags: [microarchitectural-monitoring, zero-knowledge-range-proofs, edge-ai, adversarial-detection]
link: https://eprint.iacr.org/2026/1887
byline: "Soumi Chatterjee et al. (IACR ePrint 2026/1887, Sep 4 2026)"
description: "VERA lets an edge device prove to a remote model owner, using zero-knowledge range proofs over hardware performance counters, that an inference exhibits benign microarchitectural behavior without revealing the underlying measurements."
---

Machine learning models increasingly run on edge devices outside a model owner's direct control, and existing black-box defenses can detect adversarial inputs using microarchitectural signals but provide no privacy-preserving way for a remote model owner to verify the detection outcome. The authors introduce VERA, a framework that combines lightweight hardware performance counter (HPC) monitoring with zero-knowledge range proofs (ZKRPs), since adversarial perturbations alter internal activation patterns and the resulting microarchitectural behavior during inference. Rather than revealing potentially sensitive HPC measurements, VERA lets an edge device prove that a committed HPC value lies within a calibrated benign range, avoiding the overhead of general-purpose zk-SNARKs and enabling lightweight verification on resource-constrained devices. The interactive ZKRP can also be made non-interactive via the Fiat-Shamir transform, and evaluation against multiple adversarial attacks on MNIST and CIFAR-10 shows millisecond-scale verification overhead with proof-generation costs that amortize across batches of inferences.
