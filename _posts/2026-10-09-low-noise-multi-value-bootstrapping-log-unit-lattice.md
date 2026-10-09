---
title: "Low-Noise Multi-Value Bootstrapping via Log-Unit Lattice Search and LUT Shifting"
date: 2026-10-09 08:19:00 +0200
categories: [FHE]
tags: [tfhe, programmable-bootstrapping, multi-value-bootstrapping]
link: https://eprint.iacr.org/2026/2310
byline: "Olivier Bernard et al. (Zama, IACR ePrint 2026/2310, Oct 2 2026)"
description: "A log-unit lattice search for common factors, combined with alternative lookup-table representations, substantially reduces the noise penalty of multi-value bootstrapping in TFHE."
---

Programmable bootstrapping is central to the FHEW and TFHE families of fully homomorphic encryption, and multi-value bootstrapping tries to amortize its cost by sharing a single blind rotation across several functions, but the standard choice of common factor can cause unnecessarily large noise amplification that erodes this benefit. The authors' main contribution is a log-unit lattice search for selecting common factors that substantially reduce this noise amplification, complemented by LUT shifting, which generates alternative function-preserving test-polynomial representations to enlarge the search space further. Both optimizations are performed offline, so the online multi-value bootstrapping procedure is essentially unchanged. Evaluated in TFHE at a failure probability of 2 to the power of negative 128, the construction achieves a 1.47 times latency speed-up and a 1.59 times throughput improvement on 256-bit homomorphic integer multiplication relative to a baseline that evaluates each output with a separate programmable bootstrapping.
