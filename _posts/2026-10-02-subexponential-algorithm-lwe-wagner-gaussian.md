---
title: "A Provable Subexponential-Time Algorithm for LWE from n+o(n) Samples via Wagner-Style Gaussian Sampling"
date: 2026-10-02 08:14:00 +0200
categories: [PQC]
tags: [learning-with-errors, wagners-algorithm, gaussian-sampling, lattice-cryptanalysis]
link: https://eprint.iacr.org/2026/2261
byline: "Xuyuan Han, Yiming Gao, and Honggang Hu (IACR ePrint 2026/2261, Sep 29 2026)"
description: "A new provable subexponential algorithm solves decision LWE in two complementary error and modulus regimes using only n plus o(n) samples, building on a Wagner-style Gaussian sampler."
---

The authors give a randomized subexponential-time algorithm for decision Learning with Errors that works in two complementary parameter regimes: for a polynomial prime modulus with a fixed exponent greater than one half, it handles independent discrete Gaussian errors whose width grows slowly with the dimension, while for polynomial error width it instead needs a quasipolynomial modulus. In both regimes and for an arbitrary secret distribution, the algorithm succeeds with probability approaching one using close to n original samples, where n is the LWE dimension, with expected time and space that are subexponential in n. The construction starts from the Wagner-style Gaussian sampler of Ducas, Engelberts, and Loyer from CRYPTO 2025, instantiating its auxiliary extensions with random P-ary lattices whose improved smoothing bound supports the needed accuracy without increasing the leading list-size exponent. Because the smaller Gaussian width this geometry enables makes the exact sampler from prior work unusable, the authors instead use a statistically approximate shifted discrete Gaussian sampler and control its error under adaptively chosen shifts, then apply a Fourier distinguisher via a martingale analysis to handle the resulting dependence. The analysis covers unstructured LWE with independent uniform public vectors and explicitly does not apply to ML-KEM, whose Module-LWE structure introduces algebraic dependencies the paper does not address.
