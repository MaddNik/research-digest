---
title: "Single-atom-based asynchronous photonic interconnect for scalable modular quantum computing"
date: 2026-09-25 08:05:00 +0200
categories: [Photonics]
tags: [quantum-interconnect, cavity-qed, modular-quantum-computing, entanglement-distribution]
link: https://arxiv.org/abs/2609.21961
byline: "Jeremy Raskop et al. (arXiv:2609.21961v2, Sep 18 2026, revised Sep 22 2026)"
description: "A single trapped atom mediates asynchronous entanglement between modular quantum processors, letting the rate scale linearly rather than quadratically with photon loss."
---

Most loss-resilient protocols for connecting modular quantum processors rely on linear-optics fusion gates whose entanglement rate scales quadratically with each processor's photon-delivery probability. This paper analyzes a memory-assisted quantum interconnect that instead uses a near-deterministic photon-atom controlled-Z gate via a single atom trapped in a high-finesse cavity. Detecting a photon from one processor heralds entanglement between that processor and the atom, which is preserved while the process repeats with a second processor until its photon is detected, after which reading out the atomic qubit finalizes the entanglement between the two processors. Because the atom mediates the entanglement, the photons from the two processors do not need to be indistinguishable, removing a major source of infidelity, and removing the simultaneous photon-arrival requirement lets the entanglement rate scale linearly rather than quadratically with photon-arrival probability over a wide parameter range. The authors derive entanglement rates under realistic parameters and find nanosecond-scale gate and readout operations give orders-of-magnitude entanglement-rate gains over linear optics.
