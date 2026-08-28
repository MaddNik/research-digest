---
title: "Cross-Layer Roots of Trust: Integrating Biometrics, PUFs, and Hardware Obfuscation"
date: 2026-08-28 08:36:00 +0200
categories: [Hardware Security]
tags: [physical-unclonable-functions, biometrics, hardware-obfuscation, logic-locking]
link: https://arxiv.org/abs/2608.21643
byline: "Nima Karimian (arXiv:2608.21643, Aug 21 2026)"
description: "This survey unifies biometrics, physical unclonable functions, and hardware obfuscation into a joint human-device-function model of hardware trust, formalizing how the three primitives can be composed."
---

Modern cyber-physical, IoT, wearable, and edge systems need trust in three distinct entities: the human requesting access, the physical device executing the computation, and the hardware function permitted to operate, but these are usually studied by separate research communities. The author decomposes biometrics, physical unclonable functions, and hardware obfuscation or logic locking into their complete processing chains, identifying each primitive's security assumptions, implementation mechanisms, and evaluation metrics alongside its known attacks, such as presentation attacks and template leakage for biometrics, environmental instability and modeling attacks for PUFs, and oracle-guided or structural attacks for logic locking. The survey then formalizes pairwise compositions of biometric-PUF, PUF-obfuscation, and biometric-obfuscation, as well as a three-way architecture that binds correct functionality jointly to an authorized user and a genuine device, giving particular attention to biometric key reconstruction, PUF stabilization, logic-locking attack evaluation, and cross-layer error propagation. It concludes with a taxonomy and research agenda covering revocable human-device credentials, compositional security, leakage-aware integration, and standardized end-to-end evaluation.
