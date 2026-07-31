---
title: "TroPUF: Evaluating Hardware Trojan Insertion in Delay-Based Physical Unclonable Functions"
date: 2026-07-31 08:29:00 +0200
categories: [Hardware Security]
tags: [puf, hardware-trojan, authentication]
link: https://arxiv.org/abs/2607.23418
byline: "Marissa Marcarelli et al. (arXiv:2607.23418, Jul 26 2026)"
description: "A simulation framework shows that dormant hardware Trojans can be inserted into delay-based physical unclonable function circuits while preserving normal behavior, only revealing degradation after activation."
---

Physical unclonable functions built on gate or wire delays are widely used for device authentication and key generation, and are generally assumed secure against tampering because any modification would alter their unique response signatures. This paper challenges that assumption by inserting Trojans into multiple delay-based physical unclonable function architectures and evaluating them with a simulation framework covering functional metrics, hardware overhead, and resistance to machine-learning modeling attacks. The key finding is that dormant Trojans preserve expected challenge-response behavior and pass standard validation, so detectable degradation appears only after the Trojan is activated. This reveals a security gap in current validation practices, since existing tests are not designed to catch a Trojan that intentionally mimics normal behavior until triggered. The authors argue physical unclonable function security and hardware Trojan defense need to be treated as interconnected concerns rather than separate problems.
