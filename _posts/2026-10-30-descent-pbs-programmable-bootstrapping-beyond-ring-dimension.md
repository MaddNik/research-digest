---
title: "Descent-PBS: Programmable Bootstrapping beyond the Ring Dimension"
date: 2026-10-30 08:20:00 +0200
categories: [FHE]
tags: [tfhe, programmable-bootstrapping, lookup-tables, sparse-secrets]
link: https://eprint.iacr.org/2026/2616
byline: "Zhenyu Xiong et al. (IACR ePrint 2026/2616, Oct 23 2026)"
description: "Descent-PBS pays the module rank cost of a large lookup table only once, evaluating a 16-bit negacyclic table in 196 milliseconds and beating prior module and WoP bootstrapping methods by up to 6.6 times."
---

Programmable bootstrapping in FHEW/TFHE evaluates a lookup table while refreshing a ciphertext, but a table with many entries must fit, with redundancy, into the signed rotation positions of a ring accumulator, and prior module-based bootstrapping methods pay a cost linear in both the module rank and that redundancy on every rotation. This paper presents Descent-PBS, which pays the module rank of a large table only in its first rotation by proving that, for a module secret embedded from a subring, truncation commutes with the secret, so a single public functional key switch with merged columns can repack all components of a module accumulator into the ring and remove the per-component repacking factor. The bootstrapping then continues with ring-based refinements at a cost of tau_0 plus K external products instead of (K'+1) times tau_0, and for block one-hot secrets the first-rotation exponents become multiples of tau_0 so every combined key is a scalar matrix, letting components share keys and letting one pass over the bootstrapping key build the keys for every rotation of a negacyclic table in advance. In a TFHE-rs-based engine, Descent-PBS evaluates a 16-bit negacyclic lookup table in 196 milliseconds on one thread at 128-bit security, running 1.44 to 2.40 times faster than Meta-PBS run inside the module for dense secrets and 3.8 to 6.6 times faster than WoP-PBS for general 13 to 16-bit lookup tables, at roughly twice the memory cost.
