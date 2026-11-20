---
title: "FALCON-PARE: Full-Range Side-Channel Key Recovery of Falcon via Prior-Enhanced Evidence"
date: 2026-11-20 08:27:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, falcon, number-theoretic-transform, belief-propagation]
link: https://eprint.iacr.org/2026/2888
byline: "Shuyi Chen et al. (IACR ePrint 2026/2888, Nov 13 2026, ICCD 2026)"
description: "FALCON-PARE combines Falcon's discrete-Gaussian secret-key prior with leakage from NTT computations to achieve full-range single-trace key recovery on an STM32F407 board."
---

Falcon is a compact post-quantum signature scheme selected by NIST, and its number-theoretic transform computations form a critical side-channel attack surface, but existing NTT attacks have relied on truncated coefficient ranges that do not cover the full valid range of Falcon's secret coefficients, limiting them to incomplete key recovery. The authors propose FALCON-PARE, a prior-enhanced evidence framework for full-range key recovery of Falcon. It combines Falcon's discrete-Gaussian prior with aggregated leakage from range conversion and Montgomery multiplication to build input-layer soft evidence, propagated through the NTT factor graph, and uses posterior entropy to select reliable coefficients while using the public-key relation to complete the remaining unknowns, recovering the full secret polynomials f and g. Evaluated on an STM32F407 under both -O0 and -O3 compiler settings, FALCON-PARE achieves single-trace full key recovery with 40 and 120 profiling traces respectively, gaining 54.79 and 73.83 percentage points in coefficient-wise accuracy over existing soft-analytical side-channel attacks for NTT leakage, and reducing the residual candidate space from roughly 2 to the 4352 and 2 to the 5346 down to a single candidate.
