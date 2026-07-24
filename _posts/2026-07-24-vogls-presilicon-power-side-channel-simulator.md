---
title: "Vogls: a Fast Interactive Full-timing Simulator for Pre-silicon Power Side-Channel Analysis"
date: 2026-07-24 08:28:00 +0200
categories: [Hardware Security]
tags: [pre-silicon-simulation, power-side-channel, differential-power-analysis, verilog-tooling]
link: https://arxiv.org/abs/2607.15782
byline: "Gijs Burghoorn et al. (arXiv:2607.15782, Jul 17 2026)"
description: "The paper introduces an open-source Verilog simulator built specifically for pre-silicon power side-channel analysis rather than functional correctness verification."
---

The authors present Vogls, a simulator combining compiled-code performance, full-timing simulation, and fine-grained control over simulation state, aimed at generating the many short traces with input variations that side-channel analysis requires rather than the long correctness-focused traces typical tools produce. It runs 5.9 times faster than Icarus Verilog on timing-annotated gate-level AES designs. A Python interface lets users pause, fork, inspect, and mutate simulations around points of interest, and a trace-collection workflow runs setup code once then forks at the point of interest to avoid repeated full simulations. The authors demonstrate the tool with a differential power analysis attack that recovers cryptographic keys at the RTL, gate-level, and full-timing gate-level abstraction levels.
