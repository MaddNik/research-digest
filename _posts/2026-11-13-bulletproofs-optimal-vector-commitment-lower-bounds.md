---
title: "Bulletproofs are Optimal: Lower Bounds for Vector Commitments from Fiat-Shamir in Pairing-Free Groups"
date: 2026-11-13 08:24:00 +0200
categories: [Cryptography]
tags: [vector-commitments, lower-bounds, generic-group-model, bulletproofs]
link: https://eprint.iacr.org/2026/2868
byline: "Marian Dietz, Emanuele Giunta (IACR ePrint 2026/2868, Nov 11 2026, CRYPTO 2026)"
description: "New lower bounds show that Bulletproofs-style logarithmic-size opening proofs are essentially optimal for vector commitments built from plain, pairing-free prime-order groups."
---

Vector commitments let parties commit to an ordered vector and later succinctly open it at any position, and in plain, pairing-free prime-order groups, all state-of-the-art constructions rely on combining a generalized Pedersen commitment with an inner product argument, including the well known constructions of Bootle et al. and Bunz et al. and their successors, all achieving proofs of a logarithmic number of group elements while breaking that barrier has proven hard, in contrast to pairing-friendly or unknown-order group settings where constant-size constructions have existed for over a decade. The authors investigate whether this limitation is inherent to prime-order group constructions by proving new lower bounds for any accumulator, a weaker object than a vector commitment, with an interactive public-coin membership proof in Maurer's Generic Group Model. Their result implies that in this setting, at least one of three things must hold: the commitment has super-constant size, the opening proof contains a logarithmic number of group elements, or the opening proof has polynomial length close to the vector length. The bound further extends to related primitives that imply accumulators or vector commitments, including polynomial and functional commitments and inner product arguments, and the paper is a major revision of a publication appearing at CRYPTO 2026.
