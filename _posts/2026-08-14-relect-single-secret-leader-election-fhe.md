---
title: "Relect: Single Secret Leader Election via FHE with Reduced Computation and Communication and Transparent Setup"
date: 2026-08-14 08:15:00 +0200
categories: [FHE]
tags: [threshold-fhe, secret-leader-election, ring-lwe]
link: https://eprint.iacr.org/2026/1619
byline: "Haofei Liang et al. (IACR ePrint 2026/1619, Aug 6 2026)"
description: "Relect is a single secret leader election protocol built on Ring-LWE threshold fully homomorphic encryption that removes the trusted setup required by the prior state of the art while running substantially faster."
---

In a single secret leader election, a group of parties jointly and obliviously choose one leader whose identity stays hidden unless the leader chooses to reveal it. The paper builds on Qelect, the first concretely feasible lattice-based construction, and improves it by designing custom homomorphic circuits over threshold FHE. For 32 to 2048 parties, the authors report local FHE computation between about 7.15 and 42.4 times faster than Qelect on a single thread, and up to about 48 times faster with 16 threads, along with 1.14 to 2 times lower communication. End-to-end, across 2 to 128 parties, Relect is reported as 2.77 to 345 times faster than Qelect under a local area network setting and about 1.94 to 17.2 times faster under a wide area network setting. All of this is achieved while eliminating the trusted setup and enabling dynamic leader selection each round.
