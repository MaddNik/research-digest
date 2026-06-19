---
title: "CHERI-D: Secure and efficient inline object ID for CHERI temporal memory safety"
date: 2026-06-19 08:15:00 +0200
categories: [Hardware Security]
tags: [cheri, temporal-memory-safety, capabilities, use-after-free]
link: https://arxiv.org/abs/2606.19055
byline: "Yuecheng Wang et al. (arXiv:2606.19055, Jun 17 2026)"
description: "A CHERI architectural extension embedding inline object IDs to enforce strict use-after-free protection with low revocation overhead."
---

CHERI-D is an architectural extension that pairs object identification metadata with
capability pointers to enforce temporal integrity of allocations. By embedding object IDs
directly within allocated data structures, it strengthens protection from
use-after-reallocation to strict use-after-free detection. The approach leverages CHERI's
existing spatial safety to store identification data safely, potentially reusing
otherwise-wasted memory fragmentation, while significantly reducing revocation overhead
compared with the prior Cornucopia Reloaded software-based solution. The mechanism is
evaluated through both simulation and an actual hardware implementation. It targets
efficient temporal memory safety on capability-based hardware.
