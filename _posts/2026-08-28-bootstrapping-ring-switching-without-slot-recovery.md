---
title: "Bootstrapping using Ring Switching without Slot Recovery"
date: 2026-08-28 08:19:00 +0200
categories: [FHE]
tags: [ckks, bgv, ring-switching, bootstrapping]
link: https://eprint.iacr.org/2026/1779
byline: "Zhaoyang Liang and Dan Ding (IACR ePrint 2026/1779, Aug 23 2026)"
description: "This work proves that the slot-recovery step normally required after ring switching in CKKS and BGV/BFV bootstrapping is unnecessary for affine functions, substantially improving bootstrapping throughput."
---

Ring switching can lower the cost of bootstrapping in ring-based FHE schemes by moving computation from a large ring to smaller rings, but for SIMD-packed ciphertexts it is usually followed by a slot-recovery step that consumes noise capacity needed for later operations. The authors show that slot recovery is not indispensable, proving that ring-switched realizations of CKKS and BGV/BFV bootstrapping operate correctly without it, and more generally that a continuous slotwise function on ring-switched leaves can be evaluated independently without slot recovery if and only if the function is affine. By exploiting the parallelism across smaller rings and lowering correction bounds, their implementation improves CKKS bootstrapping throughput by 99.7 to 113.5 percent with sparse-secret encapsulation and by 121.3 percent with an alternative dense-key bootstrapper at ring dimension 2 to the 17th power. For BGV at plaintext modulus 65537 and comparable ring dimensions, they report 3.16 times and 1.46 times speedups over partition-matched and capacity-comparable baselines respectively, along with server key size reductions of 16.4 to 57.6 percent.
