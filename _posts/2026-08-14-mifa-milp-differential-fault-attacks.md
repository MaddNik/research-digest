---
title: "MIFA: An MILP-based Framework for Improving Differential Fault Attacks"
date: 2026-08-14 08:29:00 +0200
categories: [Hardware Security]
tags: [differential-fault-attack, milp-optimization, default-cipher]
link: https://arxiv.org/abs/2608.06837
byline: "Hanbeom Shin et al. (arXiv:2608.06837, Aug 7 2026)"
description: "A Mixed-Integer Linear Programming framework systematically finds better fault-injection positions for differential fault attacks, breaking the claimed fault-attack security margin of the DEFAULT block cipher."
---

The paper presents a Mixed-Integer Linear Programming (MILP) based framework for optimizing differential fault attacks against block ciphers, improving on a prior attack presented at ASIACRYPT 2024. Applied to the DEFAULT cipher, the framework identifies fault-injection points at deeper rounds than previously attacked, reducing the number of faults required. The authors report that three faults at the sixth-to-last round combined with two faults each at the seventh and eighth-to-last rounds are sufficient to reduce the key space to a single candidate value. The work includes a systematic, theoretical method for calculating the minimum number of faults needed for a given attack configuration, rather than relying on ad hoc trial and error. This demonstrates that DEFAULT's stated fault-attack security margin can be broken with fewer injected faults than its designers anticipated.
