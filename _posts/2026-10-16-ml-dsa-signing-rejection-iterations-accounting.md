---
title: "On the Expected Number of Iterations in ML-DSA Signing: A Complete Accounting of the Rejection Conditions"
date: 2026-10-16 08:10:00 +0200
categories: [PQC]
tags: [ml-dsa, dilithium, rejection-sampling, nist-fips-204]
link: https://eprint.iacr.org/2026/2456
byline: "Kris Kwiatkowski (IACR ePrint 2026/2456, Oct 12 2026)"
description: "A paper shows that the expected iteration count published in FIPS 204 for ML-DSA signing omits two rejection checks, and derives corrected values that match measurement to within 0.14 percent."
---

FIPS 204's Table 1 gives the expected number of iterations of the ML-DSA signing loop by citing an equation from the CRYSTALS-Dilithium specification, but that equation only covers the validity checks on the infinity norms of z and r0 and omits two encoding-correctness checks on the size of c times t0 and the hint weight, a scoping distinction the Dilithium specification states explicitly while FIPS 204 does not reproduce it. This paper gives a complete accounting of all four rejection conditions: the z check is computed exactly by counting, the c times t0 term follows a closed-form Irwin-Hall tail restating a known peer-reviewed result, and the hint-weight term's per-coefficient probability has a closed form but its tail across all coefficients does not, since the individual probabilities are unequal, random, and correlated, so the author estimates that tail by Monte Carlo. The corrected expected iteration counts come out to 4.36, 5.14, and 3.91 for ML-DSA-44, ML-DSA-65, and ML-DSA-87 respectively, matching a real end-to-end measurement to within 0.14 percent. The corrected figures are already reflected in NIST's own errata to FIPS 204.
