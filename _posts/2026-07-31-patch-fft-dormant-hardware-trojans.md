---
title: "PATCH-FFT: Unmasking Dormant Hardware Trojans with Patch-Based Frequency-Domain Transformers"
date: 2026-07-31 08:28:00 +0200
categories: [Hardware Security]
tags: [hardware-trojan, power-side-channel, trojan-detection]
link: https://arxiv.org/abs/2607.23421
byline: "Hasala Senevirathne et al. (arXiv:2607.23421, Jul 26 2026)"
description: "A patch-based Transformer analyzing FFT-transformed power traces detects dormant, not-yet-triggered hardware Trojans, reaching 90.94 percent average detection accuracy."
---

Hardware Trojans that leak sensitive information through power side channels are especially dangerous while dormant, since once the trigger condition fires and the secret is exfiltrated, detection comes too late. The authors convert time-domain power measurement traces into frequency-domain representations using the real fast Fourier transform, exposing spectral signatures that time-domain analysis misses. A patch-based Transformer architecture is then trained on these frequency-domain representations to distinguish Trojan-infected chips from clean ones in both dormant and active states. Reported results show 90.94 percent average detection accuracy across dormant and active Trojan scenarios, with the method outperforming prior state-of-the-art time-domain approaches specifically on dormant-Trojan detection.
