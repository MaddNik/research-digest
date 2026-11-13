---
title: "From Dependent Ciphertexts to Sharp Bounds for Polynomial Evaluation in BGV"
date: 2026-11-13 08:17:00 +0200
categories: [FHE]
tags: [bgv, noise-analysis, parameter-selection]
link: https://eprint.iacr.org/2026/2869
byline: "Chiara Marcolla, Nadir Murru, Matilda Urani (IACR ePrint 2026/2869, Nov 11 2026)"
description: "A new average-case noise analysis for BGV that accounts for ciphertext dependencies yields smaller ciphertext moduli than those used in OpenFHE and HElib."
---

A central challenge in fully homomorphic encryption is choosing ciphertext moduli, which depends on accurately estimating noise growth during homomorphic evaluation, since moduli that are too large hurt efficiency while underestimating noise can cause decryption failures or security problems. Existing average-case analyses give promising probabilistic estimates of noise growth, but recent studies show that reliable estimates must account for dependencies among ciphertext errors, since ignoring these correlations systematically underestimates noise. This work presents the first average-case analysis for the BGV scheme that accounts for both correlations induced by secret and public keys and for dependencies among ciphertexts, proposing new variance estimates for the noise coefficients in homomorphic additions and multiplications and extending the framework to homomorphic evaluation of polynomial functions. The theoretical estimates closely match experimental observations, with discrepancies smaller than 1.2 bits, and when used to choose initial BGV parameters they yield significantly smaller ciphertext moduli than those currently used in popular FHE libraries, giving an average reduction of about 11.5 percent in ciphertext modulus size compared to OpenFHE, and reducing the ratio between consecutive moduli by up to 23 bits per level relative to HElib in practical settings.
