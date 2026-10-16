---
title: "Provably Subexponential Algorithms for Bounded-Error LWE with Few Samples"
date: 2026-10-16 08:11:00 +0200
categories: [PQC]
tags: [lwe, subexponential-algorithm, lattice-cryptanalysis, bkw-algorithm]
link: https://eprint.iacr.org/2026/2426
byline: "Haoxing Lin and Prashant Nalini Vasudevan (IACR ePrint 2026/2426, Oct 9 2026)"
description: "A new analysis of a Wagner and BKW style algorithm solves bounded-error Learning With Errors in subexponential time using far fewer samples than previously required."
---

This paper studies a variant of the Wagner and BKW style algorithm for Learning With Errors due to Kirchner and Fouque, and shows that it solves both decision and search LWE for secrets of size n over prime moduli q equal to n to the power kappa plus a vanishing term, for any fixed kappa greater than zero, with errors bounded by a subexponentially small quantity, running in time 2 to the power O(n divided by log log n) given only n plus O(n divided by log log n) original samples. If each coordinate of the secret is also appropriately bounded, the same running time holds with smaller errors and even fewer samples. Earlier work by other authors had shown that the same underlying algorithm could solve LWE with these parameters in subexponential time but required a much larger number of samples, on the order of n log n, and a related line of work adapted the algorithm to the dual SIS problem with its own sample requirements. The authors' approach differs from that prior lattice-chain-based analysis by relying on an elementary argument that bounds the lower moments of a Fourier statistic, tightening the known sample complexity for this class of subexponential LWE algorithms.
