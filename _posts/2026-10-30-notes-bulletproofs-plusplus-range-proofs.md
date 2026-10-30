---
title: "Notes on BulletProofs++ Range Proofs"
date: 2026-10-30 08:28:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, range-proofs, bulletproofs, rust-implementation]
link: https://eprint.iacr.org/2026/2648
byline: "Philipp Jovanovic and Arnab Roy (IACR ePrint 2026/2648, Oct 26 2026)"
description: "A self-contained specification and Rust implementation of Bulletproofs++ 64-bit and batched range proofs proves up to 7.8 times faster and verifies up to 4.5 times faster than regular Bulletproofs, while correcting two formulas from the original paper."
---

This paper reviews the Bulletproofs++ construction, which replaces the bit-decomposition inner-product argument used in Bulletproofs with a reciprocal set-membership argument over base-16 digits. The authors give a self-contained specification of the 64-bit range proof as well as a general batched variant parameterized by batch size and bit width, and they prove honest-verifier zero-knowledge and exact-form knowledge soundness for the construction. Their Rust implementation over the Ristretto255 group proves up to 7.8 times and verifies up to 4.5 times faster than regular Bulletproofs after evaluation and optimization. Along the way, the authors correct two formulas from the original Bulletproofs++ paper: the affine T cubed term of the scalar polynomial carries a factor of 2, and the slot-0 component of the blinding vector carries the opposite sign from what was originally stated.
