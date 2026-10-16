---
title: "Heterogeneous CPU-NPU Implementation of the AIMer Post-Quantum Signature for Low Latency on a Mobile SoC"
date: 2026-10-16 08:13:00 +0200
categories: [PQC]
tags: [aimer, mpc-in-the-head, npu-acceleration, mobile-soc]
link: https://eprint.iacr.org/2026/2486
byline: "Myoungsu Shin et al. (IACR ePrint 2026/2486, Oct 14 2026)"
description: "Splitting AIMer signing across a phone's CPU and neural processing unit cuts signing latency and energy use on Snapdragon mobile systems on chip."
---

Signatures built in the MPC-in-the-head paradigm, such as AIMer, rest only on symmetric primitives, but signing is slow because it computes hash functions and a linear map for every simulated party of every repetition. The authors show that the Hexagon neural processing unit found in Snapdragon systems on chip can shorten a complete AIMer signing operation, where AIMer is the MPC-in-the-head signature selected by the Korean post-quantum cryptography competition. Their implementation splits each signing operation along its dependency graph, letting the NPU compute the hashing and per-party linear map of the last repetitions, which need no secret key, while the CPU retains the secret key and the hashes that absorb the repetitions in order. Against a fast AArch64 baseline that already signs 4.5 to 6.1 times faster than the reference implementation on one core, using one core together with the NPU signs 1.30 to 1.42 times faster than two CPU cores and 1.74 to 1.97 times faster than a single core on a Snapdragon 8 Gen 3 tablet, while using 13 to 27 percent less energy per signing operation than two cores. Similar speedups of 1.28 to 1.82 times over two-core execution are reported on Snapdragon 8 Elite and 8 Gen 2 phones.
