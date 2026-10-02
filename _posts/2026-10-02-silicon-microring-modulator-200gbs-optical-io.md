---
title: "Co-design of Silicon Microring Modulator beyond 200 Gb/s per Lane: Device Physics, Operating Point, and Compact Models for Scale-Up and Scale-Out Optical I/O"
date: 2026-10-02 08:03:00 +0200
categories: [Photonics]
tags: [microring-modulator, optical-io, dwdm, compact-modeling]
link: https://arxiv.org/abs/2609.36690
byline: "Zhihong Huang et al. (arXiv:2609.36690, Sep 29 2026)"
description: "A device-physics and compact-model study maps how to push depletion-mode silicon microring modulators past 200 gigabits per second per lane for AI-system optical I/O."
---

Optical input and output links are increasingly used for high-bandwidth communication between processors in AI systems, and depletion-mode silicon microring modulators are attractive for this role because of their compact footprint, wavelength multiplexing capability, and femtojoule-scale switching energy per bit. The authors analyze the junction and cavity physics of these modulators to relate modulation efficiency, capacitance, optical loss, and coupling to the bandwidth and drive requirements needed above 200 gigabits per second per lane, since at these rates the digital signal processor doing equalization and forward-error correction can consume up to half the optical module's power. The paper examines laser detuning and optimal operating points, distinguishing maximum static slope, static and dynamic optical modulation amplitude, and gain-bandwidth product, and discusses how optical self-heating, photocarriers, and bias-network voltage droop affect the resonance alongside heater tuning in dense wavelength-division-multiplexed arrays. Cold-resonance design points are derived from the required hot detuning, link-budget-derived optical power, and thermal parameters, including heater reserve and startup acquisition as design constraints. A compact coupled electrical-optical-thermal model, with a Verilog-A implementation of the model core, is used to evaluate PAM4 eye diagrams for circuit-level simulation.
