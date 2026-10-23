---
title: "Rank Ceiling for Twiddle-Perturbation Faults on the Forward NTT"
date: 2026-10-23 08:34:00 +0200
categories: [Hardware Security]
tags: [fault-attack, ntt, ml-kem, ml-dsa]
link: https://arxiv.org/abs/2610.30383
byline: "Chakshu Gupta (arXiv:2610.30383, Oct 21 2026)"
description: "A formally certified rank-and-kernel analysis characterizes how much secret-polynomial information leaks from arbitrary static twiddle-factor faults on the forward NTT used in ML-KEM and ML-DSA, even when the faulty transform remains invertible."
---

NIST standardized ML-KEM and ML-DSA in 2024, and both compute forward number-theoretic transforms (NTTs) on secret polynomials. Prior published attacks zero every fixed twiddle multiplier during Kyber key generation with a single fault, or target individual twiddles in one Dilithium signing variant, with countermeasures designed to detect or mask these specific faults; this paper observes that nonzero twiddle replacements preserve invertibility of the transform, yet the uncompressed correct-minus-faulted transform difference can still expose input information. The author characterizes the linear map from a secret polynomial to this difference under arbitrary static twiddle replacements, including bit-flips, showing that for one fault the rank equals the number of butterflies sharing that twiddle, halving by NTT layer from 128 down to 2 for ML-KEM and to 1 for ML-DSA, and that with one fault per layer, all but the constant and linear coefficients for ML-KEM, or just the constant coefficient for ML-DSA, become determined, a rank-and-kernel result certified in the Lean 4 proof assistant. The paper further shows that if only one ML-KEM secret-polynomial NTT is faulted, comparing a known correct key with a released faulty key from the same seed lets the key difference reconstruct the transform difference via an invertible matrix column, while for ML-DSA neither this reconstruction nor the number of candidate secret polynomials from compressed key differences is yet established, leaving the per-layer rank results as a closed-form measure of raw exposure to guide future countermeasure design.
