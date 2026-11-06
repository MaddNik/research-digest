---
title: "Randomized Caches in Hardware: Challenges and Trade-offs"
date: 2026-11-06 08:34:00 +0200
categories: [Hardware Security]
tags: [randomized-caches, cache-side-channels, fpga, risc-v]
link: https://arxiv.org/abs/2611.00282
byline: "Xinrui Wang et al. (arXiv:2611.00282, Oct 30 2026)"
description: "The first comparative full-system FPGA evaluation of four randomized cache designs shows that preserving mapping and rekeying policies costs up to 35 percent clock frequency and up to 11 percent instructions per cycle."
---

Randomized caches defend against cache side-channel attacks by obfuscating how memory addresses map to cache locations, but most prior proposals describe only architectural behavior without addressing practical hardware implementation challenges. This paper implements four prominent randomized cache designs, CEASER-S, ScatterCache, SassCache, and MIRAGE, as the last-level cache of a multi-core out-of-order RISC-V system-on-chip, and evaluates complete FPGA implementations running SPEC CPU 2017 rate and GAPBS workloads to completion, providing what the authors describe as the first comparative evaluation of these designs on a common full-system hardware platform. They find that pipelining the index derivation function alone is insufficient, since in three of the four variants other components become the frequency bottleneck, reducing clock frequency by up to 35 percent relative to a baseline set-associative cache; redesigning the critical paths while preserving the mappings, rekeying, and victim-selection policies brings the three affected variants back to within 10 percent of the baseline frequency, at the cost of added latency or reduced concurrency. Increased last-level-cache access latency, rather than additional cache misses, dominates the instructions-per-cycle degradation, reducing it by up to 5 percent for SPEC and 11 percent for GAPBS. Hardware overhead varies by design and implementation technology, with FPGA lookup-table usage increasing by 10 to 35 percent and ASIC area increasing by 1 to 14 percent.
