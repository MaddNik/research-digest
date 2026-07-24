---
title: "Fuzz'EMup: Leveraging EM Side-Channel Emanation to Guide Black-Box Embedded Firmware Fuzzing"
date: 2026-07-24 08:27:00 +0200
categories: [Hardware Security]
tags: [em-side-channel, firmware-fuzzing, black-box-testing, iot-security]
link: https://arxiv.org/abs/2607.16487
byline: "Fatemeh Moradihaghighi et al. (arXiv:2607.16487, Jul 17 2026)"
description: "The paper uses electromagnetic side-channel emanations, rather than code instrumentation or emulation, to guide black-box fuzzing of embedded firmware."
---

The authors address vulnerability discovery in IoT and embedded firmware where code instrumentation or accurate emulation is not available. Their method converts noisy electromagnetic measurements into fuzzing guidance by combining frequency band selection with dynamic time warping to align traces and detect behavioral divergence, organized hierarchically for computational efficiency. Evaluated across four real firmware targets, the electromagnetic feedback yields higher code coverage than unguided fuzzing. This validates electromagnetic side channels as a practical guidance signal for security testing when traditional instrumentation is unavailable.
