---
title: "Compiling Sparse Keys for Bootstrapping FHEs: Algorithms, Hardware Acceleration, and Beyond"
date: 2026-08-28 08:18:00 +0200
categories: [FHE]
tags: [tfhe, blind-rotation, bootstrapping, hardware-acceleration]
link: https://eprint.iacr.org/2026/1783
byline: "Binwu Xiang et al. (IACR ePrint 2026/1783, Aug 23 2026)"
description: "A new NTRU-based bootstrapping framework uses cuckoo hashing on sparse binary LWE secrets to cut the sequential complexity of TFHE-style blind rotation from O(n) to O(h)."
---

Blind rotation is the dominant computational bottleneck in bootstrapping for bitwise FHE schemes such as TFHE, with existing constructions evaluating O(n) sequential external products for an LWE secret of dimension n. The authors present a new NTRU-based bootstrapping framework that uses cuckoo hashing to transform an n-dimensional binary LWE secret of Hamming weight h into extended one-hot buckets, reducing the sequential external products from O(n) to O(h), and further explore an NTT-free variant that eliminates online NTT and inverse-NTT operations during blind rotation for hardware-friendly implementations. On a single CPU thread with AVX-512, their implementation executes Boolean gate, 4-bit, and 6-bit bootstrapping in 0.83, 1.75, and 2.65 milliseconds respectively, outperforming TFHE-rs by 3.31 times, 4.18 times, and 20.47 times. On an RTX 4090 GPU they attain a throughput of 154,739 gate bootstraps per second, an amortized time of 6.46 microseconds, for speedups of 86.7 times over their own CPU result and 13.6 times over VeloFHE from TCHES 2025, and they build a first NTRU-based 8-bit FHE instruction set achieving over 10 times speedup with over 100 times smaller key size than prior work.
