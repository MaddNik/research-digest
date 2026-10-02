---
title: "FALCON++: Shorter Signatures without NTRU Smoothing Estimates"
date: 2026-10-02 08:12:00 +0200
categories: [PQC]
tags: [falcon, ntru-lattices, gaussian-sampling, signature-compression]
link: https://eprint.iacr.org/2026/2226
byline: "Hao Yan and Nicholas Zhao (IACR ePrint 2026/2226, Sep 26 2026)"
description: "FALCON++ shrinks Falcon signatures by up to 37 percent by analyzing accepted preimages directly instead of relying on NTRU smoothing-parameter estimates."
---

Falcon is an NTRU-lattice-based digital signature scheme prized for its compact signatures, and its weak-smoothness variant FalconWS, presented at ASIACRYPT 2025, shrinks signatures further by allowing narrower Gaussian sampling distributions. Pushing sizes down further needs both efficient sampling at narrower widths and a security analysis that accounts for the resulting distributions, so the authors analyze the distribution of accepted preimages directly rather than estimating the NTRU lattice's smoothing parameter. They also modify the rejection-corrected Klein-GPV sampler to cut sampling cost while controlling the resulting distributional error, combining these ideas into FALCON++ with UF-CMA and SUF-CMA security bounds in the classical random-oracle model. At ring degrees 512 and 1024, the resulting signature size estimates are 419 and 921 bytes, which are 37.09 percent and 28.05 percent smaller than standard Falcon signatures, and 11.60 percent and 5.92 percent smaller than the FalconWS estimates at matching parameter sets.
