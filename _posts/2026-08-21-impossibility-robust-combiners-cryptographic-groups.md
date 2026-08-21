---
title: "On the Impossibility of Robust Combiners for Cryptographic Groups"
date: 2026-08-21 08:20:00 +0200
categories: [Cryptography]
tags: [group-combiners, ddh, discrete-log, foundations]
link: https://eprint.iacr.org/2026/1695
byline: "Cong Zhang et al. (IACR ePrint 2026/1695, Aug 15 2026)"
description: "A foundational impossibility result shows that combining several candidate cryptographic groups into one that stays secure if at least k of n are secure cannot generically preserve DDH-style security."
---

The paper studies (k,n)-robust combiners for cryptographic groups, asking whether multiple candidate groups can be merged into a single group that remains secure as long as at least k out of n underlying candidates are secure. The authors prove that no generic (k,n)-robust combiner exists that preserves decisional Diffie-Hellman (DDH) security for all polynomially bounded n and k with k less than n. For the discrete logarithm problem specifically, they show robustness is achievable only when the combined group's order satisfies particular size constraints relative to the component group orders and the security parameter. They conclude that robustness for group-based cryptography generally cannot be achieved at the group-construction layer and must instead be pursued at higher layers such as protocol design or key derivation.
