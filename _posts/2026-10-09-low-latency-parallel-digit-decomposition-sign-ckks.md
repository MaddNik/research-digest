---
title: "Low-Latency Parallel Digit Decomposition and Sign Evaluation for CKKS"
date: 2026-10-09 08:21:00 +0200
categories: [FHE]
tags: [ckks, sign-evaluation, bootstrapping]
link: https://eprint.iacr.org/2026/2368
byline: "Jung Hee Cheon et al. (IACR ePrint 2026/2368, Oct 5 2026)"
description: "A parallel digit-extraction method obtains all radix digits of a CKKS-encrypted value with a single bootstrapping, speeding up sign evaluation by nearly eight times at high precision."
---

Nonlinear functions such as sign, comparison, and ReLU are usually evaluated in CKKS with polynomial approximations, but distinguishing inputs separated by about 2 to the negative p requires multiplicative depth that grows as O(p), which the authors show drives modulus consumption up to O(p squared) bits in a standard noise model. Extracting digits from a radix-B representation avoids this cost, but previous digit-extraction methods pulled out digits one at a time with u sequential bootstrappings. This paper obtains all u digits in parallel with a single bootstrapping, producing each digit with at most one carry error from the digit below and then correcting all carries in O(log u) depth using carry look-ahead, which for the sign function combines digits directly without fully recovering them. As a result, inputs separated by about 2 to the negative p can be distinguished using O(p) modulus bits instead of O(p squared), and benchmarks show a 2.04 times speedup for ten-digit radix-64 coefficient decomposition and a 7.83 times speedup for sign evaluation on 1,024 input pairs separated by 2 to the negative 60.
