---
title: "Improved Conversion for Gao-Zheng FHE Scheme with $O(1)$ Bootstrapping"
date: 2026-09-04 08:16:00 +0200
categories: [FHE]
tags: [ckks, discrete-ckks, bootstrapping, arithmetic-logic-unit]
link: https://eprint.iacr.org/2026/1836
byline: "Yuchen Wei et al. (IACR ePrint 2026/1836, Aug 30 2026)"
description: "A new conversion method turns a single triangle-encoded ciphertext into discrete-CKKS encoding using O(1) CKKS bootstraps plus O(log n) extra level consumption, closing an open question left by the Gao-Zheng FHE scheme."
---

Supporting both arithmetic and logic operations efficiently in fully homomorphic encryption is an important step toward general-purpose privacy-preserving computation. Gao and Zheng, at CRYPTO 2026, introduced a triangle encoding for arithmetic over n-bit machine words with a refreshing cost of O(1) CKKS bootstrapping operations, and showed triangle encoding can be converted to discrete-CKKS encoding for logic operations at amortized O(1) bootstraps for O(n) input ciphertexts, or O(n) bootstraps for a single input ciphertext, leaving open whether a cheaper single-ciphertext conversion exists. This paper answers that question, proposing a new conversion method to discrete-CKKS encoding for a single ciphertext in triangle encoding that costs only O(1) CKKS bootstrapping plus an additional O(log n) level consumption. Combined with the existing refreshing and conversion methods from Gao-Zheng, this yields a full FHE scheme for a SIMD arithmetic logic unit with O(1) bootstrapping overall.
