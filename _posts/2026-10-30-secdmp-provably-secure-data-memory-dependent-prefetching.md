---
title: "SecDMP: Provably Secure Data Memory-Dependent Prefetching"
date: 2026-10-30 08:38:00 +0200
categories: [Hardware Security]
tags: [data-memory-dependent-prefetcher, microarchitectural-side-channel, constant-time, risc-v]
link: https://arxiv.org/abs/2610.37454
byline: "Jens Sprengers et al. (arXiv:2610.37454, Oct 27 2026, NDSS 2027)"
description: "SecDMP is a formally proven hardware defense against data memory-dependent prefetcher leakage, shown on an open-source RISC-V implementation to eliminate all DMP leakage classes that an existing performance-preserving defense fails to cover, at minimal overhead."
---

Data memory-dependent prefetchers are a recently introduced microarchitectural optimization in mainstream desktop and server CPUs that improve performance but have been shown to leak secrets through side channels, even from constant-time code already hardened against Spectre attacks, and existing defenses either cost significant performance or, as this paper shows, fail to block all leakage. The authors first propose a classification of data memory-dependent prefetcher leakage, categorize existing and novel attacks, and analyze which leakage classes current defenses actually mitigate, validating the analysis empirically by implementing the first open-source such prefetchers on a RISC-V processor and showing that the only existing performance-preserving defense fails to protect against entire leakage classes. They then propose SecDMP, a hardware-based defense that requires secrets to be marked in memory and ensures the prefetcher never encodes these secrets in the microarchitecture without compromising performance on public data, formally proving that SecDMP introduces no leakage beyond a baseline semantics without such prefetchers. When combined with speculative-execution defenses, SecDMP is shown to restore complete microarchitectural security for constant-time code, and empirical evaluation shows it prevents all prefetcher leakage while incurring minimal performance overhead and hardware cost.
