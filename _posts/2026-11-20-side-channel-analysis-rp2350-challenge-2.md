---
title: "Side-Channel Analysis of the RP2350 Challenge 2"
date: 2026-11-20 08:26:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, power-analysis, aes, rp2350]
link: https://arxiv.org/abs/2611.25479
byline: "Nikhil Tattikota, Vincent Immler (arXiv:2611.25479, Nov 19 2026)"
description: "An independent side-channel analysis of the RP2350 hardened AES bug-bounty challenge recovers the key, contradicting the challenge authors' hardening claims after the challenge sat unsolved for over a year."
---

Bug bounty programs and community side-channel challenges are an established way to crowd-source security assessment, but the authors note that participants carry risk twice over, both in doing the work and in having it officially accepted on terms that can be unfavorable, which makes independent publications free of third-party obligations valuable for highlighting real deficiencies. They analyze the RP2350 side-channel analysis challenge and its hardened AES implementation, which they consider significant enough to warrant such independent scrutiny given that the challenge had remained unsolved for more than a year. The paper presents a side-channel analysis demonstrating comprehensive leakage detection, plaintext dependence, and full key extraction from the challenge implementation, which the authors say reveals concerning weaknesses that contradict the challenge authors' hardening claims. They share the analysis openly to encourage further public scrutiny of the implementation.
