---
title: "HULK: An Efficient Algorithm for Enabling Fast Bulk Bitwise Operations on Homomorphically Encrypted Data"
date: 2026-10-16 08:20:00 +0200
categories: [FHE]
tags: [bulk-bitwise-operations, homomorphic-encryption, gpu-acceleration, hamming-weight]
link: https://arxiv.org/abs/2610.18391
byline: "Mayank Kabra et al. (arXiv:2610.18391, Oct 13 2026)"
description: "HULK speeds up bulk bitwise AND, OR, and XOR operations on homomorphically encrypted data by up to 7.26 times on CPU and 6.65 times on GPU by replacing costly multiplications with low-cost homomorphic additions."
---

Many important cloud applications in healthcare, graph, and database analytics spend 62 to 100 percent of their execution time on bulk bitwise operations such as AND, OR, and XOR over sensitive data, and homomorphic encryption lets these run without decryption but existing approaches rely on high-latency multiplications or lookup tables that also increase ciphertext size. HULK reduces the use of these costly operations in two steps: it constructs bulk bitwise operations from low-cost homomorphic additions that compute the Hamming weight of the encrypted operand bits in every slot of a packed ciphertext without any homomorphic multiplication, and it then decodes the AND, OR, or XOR result from that Hamming weight using a single indicator polynomial, keeping the result in the standard encoding. Across 13 end-to-end applications spanning healthcare, graph, and database analytics, HULK improves performance over the prior arithmetic approach by up to 7.26 times on CPU and 6.65 times on GPU, averaging roughly 1.5 to 2.3 times depending on the domain and platform. When the reduction depth is increased in a representative application, HULK's speedup over the state-of-the-art GPU baseline grows to 10.10 times.
