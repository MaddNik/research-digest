---
title: "Efficient Large-Integer Arithmetic for FHE"
date: 2026-08-14 08:16:00 +0200
categories: [FHE]
tags: [rns-arithmetic, ckks, library-survey]
link: https://eprint.iacr.org/2026/1608
byline: "Ahmad Al Badawi et al. (IACR ePrint 2026/1608, Aug 6 2026)"
description: "A survey of Residue Number System techniques for the large-integer polynomial-ring arithmetic underlying vectorized FHE schemes such as BFV, BGV, and CKKS."
---

FHE schemes based on Ring Learning with Errors require arithmetic over polynomial rings with coefficient moduli spanning hundreds or thousands of bits, far beyond native processor word sizes, so essentially all practical libraries rely on Residue Number System (RNS) representations. The paper gives a formal treatment of the two core RNS building blocks, basis extension and scaling, and contrasts two long-standing algorithmic families for them: the integer-only BEHZ approach, which tolerates approximation overflows and corrects them with redundant moduli, versus the floating-point HPS approach. It traces how these primitives shaped the architecture of libraries including HElib, SEAL, PALISADE and OpenFHE, HEAAN, and Lattigo, with particular attention to the scaling error inherent in the original full-RNS CKKS variant and newer fixes such as reduced-error scaling, composite scaling, and grafting. The survey also covers GPU-accelerated implementations and closes by discussing renewed exploratory interest in non-RNS positional representations.
