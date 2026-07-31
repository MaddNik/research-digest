---
title: "Correcting the Modulus Switch Error in TFHE Bootstrapping for Real-Valued Computation"
date: 2026-07-31 08:16:00 +0200
categories: [FHE]
tags: [tfhe, bootstrapping, modulus-switching, numerical-integration]
link: https://eprint.iacr.org/2026/1533
byline: "Thomas Crasson et al. (IACR ePrint 2026/1533, Jul 27 2026)"
description: "A first-order Taylor-expansion correction applied after programmable bootstrapping reduces the rounding error introduced by TFHE's modulus-switching step."
---

TFHE's programmable bootstrapping requires a modulus-switching step that introduces a rounding error, which discretizes the input space and limits achievable precision for real-valued computation. The authors propose a correction algorithm based on a first-order Taylor expansion, applied after bootstrapping, that directly mitigates this rounding error. They use the many-LUT technique to recover both function encryptions and derivative encryptions within a single bootstrapping operation, keeping the approach computationally efficient. The method achieves roughly a tenfold reduction in bootstrapping noise standard deviation and is demonstrated on encrypted numerical integration of ordinary differential equations.
