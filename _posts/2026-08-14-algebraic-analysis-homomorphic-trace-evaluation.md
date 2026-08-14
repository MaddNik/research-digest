---
title: "Algebraic Analysis of Homomorphic Trace Evaluation and Its Applications"
date: 2026-08-14 08:17:00 +0200
categories: [FHE]
tags: [noise-analysis, bootstrapping, trace-evaluation]
link: https://eprint.iacr.org/2026/1604
byline: "Han Xia (IACR ePrint 2026/1604, Aug 6 2026)"
description: "A refined, coefficient-wise noise analysis of homomorphic field trace evaluation tightens prior uniform noise bounds used in bootstrapping, ciphertext packing, and coefficient extraction."
---

Field trace evaluation is a widely used primitive in FHE, applied in bootstrapping algorithms and privacy-preserving protocols, and recent work has reduced its noise growth by combining tower-based evaluation with rescaling. The author argues existing analyses use uniform noise bounds that do not reflect the actual noise behavior across different output coefficients, leaving a gap between theory and experiment. This work presents an algebraic analysis showing structured cancellation among noise coefficients induced by the trace mappings of subextensions, finding that, apart from the constant term, the variance of each output coefficient depends on the 2-adic valuation of its index. The resulting bounds improve on prior uniform estimates by a factor of O(log n) for non-constant coefficients, where n is the ring degree, and the analysis is extended to ciphertext packing and coefficient extraction, improving prior bounds there by factors ranging from Theta(n) up to Theta(n squared). Experiments confirm the predicted coefficient-wise noise pattern and show it can guide parameter selection in practice.
