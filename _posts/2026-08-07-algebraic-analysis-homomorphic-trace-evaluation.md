---
title: "Algebraic Analysis of Homomorphic Trace Evaluation and Its Applications"
date: 2026-08-07 08:26:00 +0200
categories: [FHE]
tags: [bootstrapping, noise-analysis, ciphertext-packing]
link: https://eprint.iacr.org/2026/1604
byline: "Han Xia (IACR ePrint 2026/1604, Aug 4 2026)"
description: "A refined algebraic analysis of homomorphic trace evaluation over power-of-two cyclotomic rings finds structured noise cancellation that tightens prior noise-growth estimates."
---

Trace evaluation is a core sub-routine used in FHE bootstrapping, ciphertext packing, and coefficient extraction, and its noise behavior affects how parameters must be chosen. This paper provides an algebraic analysis of trace evaluation over power-of-two cyclotomic rings and identifies structured cancellation effects in the resulting noise coefficients that prior, uniform noise estimates missed. The author shows that the variance of each output noise coefficient depends on the two-adic valuation of its index, and that accounting for this yields improvements over prior estimates by a factor on the order of log n for general trace evaluation. For the specific applications of ciphertext packing and coefficient extraction, the improvements are larger still, on the order of n to n squared. Experimental results are reported to validate the coefficient-wise noise predictions, and the author states the findings give practical guidance for choosing parameters in homomorphic encryption systems.
