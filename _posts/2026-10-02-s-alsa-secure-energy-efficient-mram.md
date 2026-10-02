---
title: "S-ALSA: Co-Design of Adiabatic Logic-based Sensing and Balanced Bit-Cells for Secure and Energy-Efficient MRAM"
date: 2026-10-02 08:38:00 +0200
categories: [Hardware Security]
tags: [mram, power-analysis, adiabatic-logic, memory-security]
link: https://arxiv.org/abs/2609.33619
byline: "Wu Yang, Amit Degada, and Himanshu Thapliyal (arXiv:2609.33619, Sep 27 2026, IEEE ISVLSI 2026)"
description: "A co-designed adiabatic sense amplifier and balanced bit-cell for STT- and SOT-MRAM cuts read energy by up to 80 percent while fully suppressing key leakage under correlation power analysis."
---

Magnetoresistive RAM technologies such as Spin-Transfer Torque MRAM and Spin-Orbit Torque assisted STT-MRAM offer nonvolatility and low leakage, making them attractive for IoT systems, but the authors point out that conventional MRAM read circuits face two fundamental problems at once: high dynamic energy consumption and vulnerability to side-channel attacks caused by data-dependent current variations in magnetic tunnel junctions. Their Secured Adiabatic Logic Sense Amplifier, S-ALSA, addresses both through circuit-device co-design, combining structural current balancing via a 4T-2MTJ bit cell that eliminates read current asymmetry at the storage level with dynamic power equalization via adiabatic charge recovery in the sensing circuit itself, and the architecture supports both STT-MRAM and SOT-STT-MRAM. Case studies on 4x4 MRAM macros show up to 80 percent energy savings over conventional pre-charge sense amplifiers across IoT operating frequencies. Correlation power analysis attacks on PRESENT-80 encryption confirm complete suppression of key leakage when S-ALSA is combined with the balanced bit cell, establishing a unified framework where energy efficiency and hardware security are achieved together for secure, low-power IoT memory.
