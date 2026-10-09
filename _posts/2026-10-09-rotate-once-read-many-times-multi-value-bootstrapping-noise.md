---
title: "Rotate Once, Read Many Times: on the Output Noise of Multi-Value Bootstrapping"
date: 2026-10-09 08:20:00 +0200
categories: [FHE]
tags: [tfhe, programmable-bootstrapping, noise-analysis]
link: https://eprint.iacr.org/2026/2332
byline: "Philippe Chartier, Michel Koskas, and Mohammed Lemou (IACR ePrint 2026/2332, Oct 4 2026)"
description: "A unified noise analysis compares single-value and multi-value bootstrapping modes in FHEW/TFHE and identifies which cofactor choice minimizes output noise for different accumulator error models."
---

In FHEW/TFHE, a programmable bootstrap evaluates an arbitrary function of the encrypted message via the test polynomial of a blind rotation, and this paper works in a prime-power cyclotomic ring to compare Single-Value Mode, which uses one rotation per function, with Multi-Value Mode, which shares one function-independent rotation across all functions. By factoring the test polynomial into a function part and a rotated factor, the authors show that a single hypothesis about the accumulator error covariance covers both modes, with the ratio of their variances giving the exact noise amplification. The function-independent factorizations are parametrized by a cofactor and an integer lift of the lookup table, and the authors identify two competing cofactor designs: a canonical cofactor and a pivot cofactor that reads the integer table directly. Under a spherical error model the canonical cofactor favors generic tables, while under a block Laplacian model it is optimal for every table size, and both designs are measured, in the key-noise regime, on a complete, publicly available implementation.
