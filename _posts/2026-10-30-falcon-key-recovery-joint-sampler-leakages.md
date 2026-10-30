---
title: "Falcon Key Recovery from Joint Sampler Leakages"
date: 2026-10-30 08:34:00 +0200
categories: [Hardware Security]
tags: [falcon, fn-dsa, power-analysis, gaussian-sampling]
link: https://eprint.iacr.org/2026/2656
byline: "Youngchang Kim et al. (IACR ePrint 2026/2656, Oct 27 2026)"
description: "A unified power analysis attack fusing three leakage channels from Falcon's Gaussian sampler recovers full Falcon-512 keys from a median of 11 signatures on a Cortex-M4, bypassing lattice reduction entirely."
---

Falcon, and the forthcoming FN-DSA standard based on it, generate signatures through discrete Gaussian sampling, and power consumption during each SamplerZ call leaks information about secret-dependent intermediate values. While prior attacks exploited individual or paired sampler leakages, this paper presents a unified key-recovery framework that fuses three observations from each SamplerZ call, the signed-exponent class of the integer center, the random-sign bit, and a multi-class proposal magnitude, mapping the resulting candidate sets directly into slab and halfspace constraints on the secret key via an exact public linear relation, entirely bypassing computationally intensive lattice reduction methods such as LLL or BKZ. For PQClean Falcon-512 running at -O3 on an ARM Cortex-M4, a 17-class center classifier achieves 99.34 percent call-level accuracy, and the resulting attack recovers all 50 evaluated keys using at most 34 signatures with a median of 11 signatures and a median post-classification runtime of 17.54 seconds per key. On c-fn-dsa, where center conversion relies on a single constant-time count-leading-zeros instruction, a reduced-resolution 7-class classifier combined with proposal leakage still recovers 38 of 50 keys within 200 signatures, showing that instruction-level normalization alone does not prevent key recovery and that side-channel countermeasures must protect all sampler leakage channels jointly.
