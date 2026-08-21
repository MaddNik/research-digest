---
title: "Qlapoty: Improved Analysis and Efficiency for Quaternionic Ideal to Isogeny Transformation"
date: 2026-08-21 08:13:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-based, norm-equation-solving, algorithm-correction]
link: https://eprint.iacr.org/2026/1700
byline: "Max Duparc et al. (IACR ePrint 2026/1700, Aug 15 2026)"
description: "A corrected and accelerated version of the Qlapoti algorithm, a core building block of SQIsign, yielding 6 to 9 times faster norm equation solving."
---

The paper revisits Qlapoti, an algorithm that simplified and accelerated the quaternionic ideal-to-isogeny translation step central to SQIsign. The authors identify that the original analysis did not treat several technical details in sufficient depth, resulting in a flawed failure-probability analysis, and that discrepancies existed between the published pseudocode and the actual implementation that were never explicitly analyzed. This work addresses those shortcomings and introduces further improvements, producing a new norm equation solving algorithm with negligible failure probability. Their C implementation shows speedups of 6x to 9x over the original Qlapoti norm equation solver, and 1.3x to 2.1x speedups for a full SQIsign signature depending on the NIST security level.
