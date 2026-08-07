---
title: "Beyond Affine Invariants: A Hamming-Weight Correlation Metric for Template-CPA Leakage in Key-Dependent S-boxes"
date: 2026-08-07 08:29:00 +0200
categories: [Hardware Security]
tags: [side-channel, power-analysis, sbox-design]
link: https://eprint.iacr.org/2026/1584
byline: "Wieslaw Maleszewski (IACR ePrint 2026/1584, Aug 3 2026)"
description: "A new Hamming-weight correlation metric detects template correlation-power-analysis leakage in key-dependent S-boxes that classical affine-invariant criteria such as nonlinearity and differential uniformity cannot see."
---

Classical S-box selection criteria like nonlinearity, differential uniformity, boomerang uniformity, and algebraic degree are invariant under affine transformations, but the Hamming-weight statistic that governs template correlation power analysis is not affine invariant. This means two S-boxes with identical classical scores can still leak differently under a template correlation power analysis attack. The author defines a Hamming-weight template correlation metric for a key-dependent S-box family built from the multiplicative inverse in the finite field of 256 elements composed with random affine transformations, and tests it against three sources of randomness with different statistical regularity across 300000 sampled S-boxes. While the classical invariants stay identical across all sources as expected, the new metric detects meaningfully wider correlation distributions for less-random sources, corresponding to a 29 percent relative increase in AES-template attack success rate in simulation at a fixed signal-to-noise ratio. The author notes the effect size is small by standard measures, but frames the contribution as a new detectability axis for template correlation power analysis leakage rather than a standalone design criterion.
