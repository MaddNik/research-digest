---
title: "NonSense: On the (In)security of FPGA Anti-tamper Sensors"
date: 2026-11-13 08:30:00 +0200
categories: [Hardware Security]
tags: [fpga, fault-injection, anti-tamper, physical-attacks]
link: https://arxiv.org/abs/2611.17065
byline: "Mehmet Ali Cetin et al. (arXiv:2611.17065, Nov 12 2026)"
description: "A survey and analysis argues that the on-chip sensors modern FPGAs use to detect glitching and other active physical attacks are themselves a fragile and underexplored attack surface."
---

FPGAs are widely used in mission-critical systems, where a successful physical attack can have serious consequences, and modern FPGAs defend against active physical attacks such as glitching by relying on on-chip sensors that detect disturbances and trigger responses like key zeroization before a device is compromised. These sensors are deployed as both hard-IP blocks and soft-IP cores, and the authors challenge the common assumption that their trustworthiness can be taken for granted, arguing that the sensors themselves are a fragile and underexplored attack surface. Drawing on recent results, they show that both the detection and response mechanisms of state-of-the-art sensors can be bypassed without invasive tampering. They further argue that sensor reliability is reduced by factors rarely captured in existing threat models, including the spatial and frequency-dependent behavior of the power delivery network, which can steer a fault toward a target while sparing nearby sensors, environmental conditions such as temperature that shift detection thresholds, and long-term aging that drifts sensor calibration and may open silent detection gaps. The paper proposes a set of countermeasures intended to harden detection and response mechanisms against these effects.
