---
title: "Homomorphic Encryption and Bootstrapping for Real Matrices over Conjugate-Invariant Rings"
date: 2026-11-20 08:16:00 +0200
categories: [FHE]
tags: [ckks, bootstrapping, matrix-encryption, conjugate-invariant-rings]
link: https://eprint.iacr.org/2026/2887
byline: "Ilaria Chillotti et al. (IACR ePrint 2026/2887, Nov 13 2026)"
description: "Combining conjugate-invariant CKKS with the Gentry-Lee matrix scheme yields a new real-matrix FHE variant whose keys have half the rank of the original Gentry-Lee scheme."
---

The conjugate-invariant variant of CKKS encrypts real vectors over a subring of a power-of-two cyclotomic ring fixed by inversion, giving as many real slots as the rank of the ring, while the separate Gentry-Lee scheme packs batches of complex matrices into a three-variable ring that multiplies them natively, with bootstrapping that replaces slot-transform rotations with ciphertext-plaintext matrix products. The authors combine the two lines of work. They first give a bootstrapping procedure for conjugate-invariant CKKS whose transforms factor the real decoding matrix into sparse stages and whose modular reduction runs only once, on real slots, needing no conjugation key. They then fold the three Gentry-Lee variables under their inversions to obtain three subrings with real slots that are closed under the matrix product, defining three conjugate-invariant Gentry-Lee variants, and describe the third in detail: it encrypts real matrices, needs no conjugation, and for the same matrix size and count has keys of half the rank of the original Gentry-Lee scheme's keys. Finally, they adapt Gentry-Lee's matrix-product bootstrapping to this variant and prototype the resulting techniques.
