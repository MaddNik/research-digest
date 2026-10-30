---
title: "Towards Quantum Sensing for Side-Channel Analysis"
date: 2026-10-30 08:32:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, quantum-sensing, electromagnetic-emanation, nv-centers]
link: https://eprint.iacr.org/2026/2660
byline: "Oliver Butowski et al. (IACR ePrint 2026/2660, Oct 27 2026)"
description: "A nitrogen-vacancy-center-based radio-frequency spectrometer with 1.1 gigahertz real-time bandwidth performs spectral-temporal electromagnetic side-channel analysis of an RSA decryption and detects leakage from an NTT implementation on a Cortex-M4 microcontroller."
---

Electromagnetic near-field side-channel analysis exploits the data-dependent currents flowing through an integrated circuit, and this paper studies whether quantum sensing based on nitrogen-vacancy centers, previously used mainly for static or quasi-static magnetic field imaging of chips, can be applied to the dynamic electromagnetic fields relevant to side-channel attacks. The authors build a nitrogen-vacancy-center-based radio-frequency spectrometer with 1.1 gigahertz of real-time bandwidth and an adjustable center frequency that probes the frequency spectrum directly via nitrogen-vacancy center interactions in the time domain, avoiding the need for Fourier transforms or frequency sweeps. Using this sensor, the authors demonstrate, for what they describe as the first time, spectral-temporal analysis of the electromagnetic side-channel from an RSA decryption. They further use the spectrometer to perform leakage detection on a software implementation of the Number Theoretic Transform, a core building block of current lattice-based post-quantum algorithms, running on a commercial off-the-shelf Cortex-M4 microcontroller.
