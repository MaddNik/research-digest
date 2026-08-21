---
title: "A Descent to Hades: Attacks on PKP and PEP over Extension Fields"
date: 2026-08-21 08:15:00 +0200
categories: [PQC]
tags: [code-based-cryptography, permuted-kernel-problem, code-equivalence, cryptanalysis]
link: https://eprint.iacr.org/2026/1711
byline: "Alessandro Budroni et al. (IACR ePrint 2026/1711, Aug 17 2026)"
description: "New polynomial-time attacks on the Permutation Code Equivalence Problem and Permuted Kernel Problem when instantiated over field extensions undermine their use as hardness assumptions in that setting."
---

The paper examines the computational hardness of the Permutation Code Equivalence Problem (PEP) and the Permuted Kernel Problem (PKP), which underlie some code-based and multivariate cryptographic proposals, specifically when these problems are instantiated over field extensions rather than prime fields. By drawing connections to structured decoding problems, the authors identify new polynomial-time solvable parameter regimes for both PKP and PEP. They adapt existing algorithms designed for related problems to this setting and present a reduction linking certain PEP instances over odd-characteristic extension fields to the graph isomorphism problem. Based on these results, the authors conclude that their findings invalidate the use of PEP over extension fields for most practical scenarios, while also providing new understanding of PKP security in this setting.
