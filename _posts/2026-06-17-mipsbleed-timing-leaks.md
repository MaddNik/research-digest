---
title: "MIPSBLEED: Uncovering Microarchitectural Timing Leaks in Pervasive Embedded Processors"
date: 2026-06-17 08:32:00 +0200
categories: [Hardware Security]
tags: [side-channel, microarchitectural, timing-attack, embedded]
link: https://arxiv.org/abs/2606.16372
byline: "Ahmed Najeeb et al. (arXiv:2606.16372, Jun 15 2026)"
description: "A framework that exposes practical timing side-channels in MIPS embedded processors and recovers elliptic curve keys."
---

MIPSBLEED is a systematic analysis and exploitation framework that uncovers leakage
in three shared microarchitectural components of MIPS processors: the L1 data cache,
the L1 instruction cache, and the execution engine. These chips are pervasive in
routers and Internet of Things systems but have been largely overlooked in
microarchitectural security research. The authors demonstrate practical,
high-resolution timing attacks that operate without privileged access. They achieve
key recovery against real elliptic curve cryptography implementations. The work
argues that MIPS remains a critical and understudied target for side-channel
analysis.
