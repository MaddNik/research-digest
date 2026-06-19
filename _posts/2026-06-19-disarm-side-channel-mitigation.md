---
title: "DISARM: Target Electronic Device Informed Mitigation of Software Runtime Side-Channel Vulnerabilities"
date: 2026-06-19 08:16:00 +0200
categories: [Hardware Security]
tags: [timing-side-channel, hardware-aware-mitigation, embedded-devices, constant-time]
link: https://arxiv.org/abs/2606.19807
byline: "Tasneem Suha et al. (arXiv:2606.19807, Jun 18 2026)"
description: "A hardware-informed methodology that uses real embedded-device timing to generate targeted fixes for runtime side-channel leaks."
---

Timing attacks exploit variations in a program's execution times to extract sensitive
information such as encryption keys. Existing mitigations that balance execution times
across code paths ignore the underlying hardware, which can lead to over-fixing,
under-fixing, or outright failures. DISARM is a joint hardware-software methodology that
uses timing values measured from real embedded devices to generate targeted software fixes
rather than generic mitigations. It supports C, C++, and Java codebases and was evaluated
across 22 benchmarks and five different embedded and edge devices. The authors report that
DISARM outperforms state-of-the-art solutions such as PENDULUM and DifFuzzAR in
execution-time overhead, code-size overhead, and correctness.
