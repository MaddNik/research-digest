---
title: "When Masking Preimage Computation Isn't Enough: A Power Analysis Attack on Masked Implementations of Falcon"
date: 2026-10-09 08:33:00 +0200
categories: [Hardware Security]
tags: [falcon, power-analysis, masking-countermeasure]
link: https://eprint.iacr.org/2026/2313
byline: "Keng-Yu Chen (IACR ePrint 2026/2313, Oct 2 2026)"
description: "A new power analysis attack recovers the Falcon secret key by exploiting leakage during share recombination, even when the preimage computation itself is masked."
---

This paper presents a power analysis attack targeting a Falcon implementation that protects its preimage computation with masking, but still leaks through the share recombination phase. By analyzing the ratio between the real and imaginary parts of the public hash polynomial, the author shows that this leakage can be exploited to recover the secret key, and proposes two attack variants: a chosen-message attack where the adversary forces extreme coefficient ratios, and a non-chosen-message attack that filters naturally occurring vulnerable hashes. Using the ELMO leakage simulator for an ARM Cortex-M0 architecture, the attack achieves a 98.3 percent success rate with 4,000 traces. While a fully masked implementation of Falcon prevents the attack, the author proposes a practical rejection-sampling-based countermeasure that avoids the prohibitive computational overhead of a fully masked Gaussian sampler.
