---
title: "Characterizing the Variance Envelope: A Multi-Dimensional Analysis of Spectre Telemetry Across Architectures and Workloads"
date: 2026-08-21 08:28:00 +0200
categories: [Hardware Security]
tags: [spectre, transient-execution, performance-counters, detection]
link: https://arxiv.org/abs/2608.13920
byline: "Jaya Keshava Chandra Kotha and Jean-Luc Gaudiot (arXiv:2608.13920, Aug 14 2026)"
description: "A cross-architecture study of how Spectre-class attacks show up in hardware performance-counter telemetry, and why machine-learning detectors trained in the lab fail to generalize."
---

The authors study how Spectre-family transient-execution attacks manifest in processor performance counter telemetry across Intel, ARM, and AMD hardware, and multiple workloads and noise conditions. They find that detection models trained under controlled lab conditions degrade substantially when exposed to real-world system noise and varied attack timing, indicating an overfitting problem in prior detection work. One specific finding is that AMD Jaguar processors have an architectural characteristic that prevents reliable Prime plus Probe attack detection through this telemetry approach. They conclude that robust runtime Spectre detection needs architecture-specific, flexible models rather than a single generic detector.
