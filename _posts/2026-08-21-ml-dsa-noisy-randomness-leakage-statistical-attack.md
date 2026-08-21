---
title: "Statistical Inference from Noisy Randomness Leakage for ML-DSA Attacks"
date: 2026-08-21 08:23:00 +0200
categories: [Hardware Security]
tags: [ml-dsa, masking, randomness-leakage, statistical-attack]
link: https://eprint.iacr.org/2026/1712
byline: "Niklas Paskarbeit et al. (IACR ePrint 2026/1712, Aug 17 2026)"
description: "A statistical framework extracts secret-key information from noisy, partially leaked masking randomness in ML-DSA signing."
---

The paper studies ML-DSA, the NIST post-quantum signature standard, implementations that leak a single bit of masking randomness per signature, showing that even a small, noisy leak breaks the intended masking guarantee. The authors introduce a method-of-moments estimator to characterize the bit-error rate of the leakage channel and to compute posterior probabilities for each leaked bit given noisy observations. They combine this with a preprocessing step that filters or reweights signature relations before feeding them into existing key-recovery attacks. Reported results show the preprocessing reduces the number of informative relations needed by roughly 20 to 44 percent in some settings, and raises recovery success from about 16 to 19 out of 30 trials up to 23 to 29 out of 30 in others.
