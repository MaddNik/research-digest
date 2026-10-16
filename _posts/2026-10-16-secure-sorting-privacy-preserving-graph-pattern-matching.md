---
title: "On Secure Sorting and Its Application to Privacy-Preserving Graph Pattern Matching"
date: 2026-10-16 08:27:00 +0200
categories: [Cryptography]
tags: [secure-multiparty-computation, oblivious-sorting, anti-money-laundering, graph-algorithms]
link: https://eprint.iacr.org/2026/2457
byline: "Marcel Keller (IACR ePrint 2026/2457, Oct 13 2026)"
description: "A systematic comparison of Quicksort- and radix-sort-based completely secure sorting protocols for multi-party computation is applied to privacy-preserving detection of money-laundering patterns in graphs."
---

Secure sorting has been studied in multi-party computation for over a decade, and recent advances have produced completely secure implementations, revealing nothing beyond the list size, based on Quicksort and on radix sort. This paper provides the first extensive comparison of these two variants across a range of parameters for both honest-majority and dishonest-majority computation. The author then applies secure sorting to improve sparse matrix multiplication without oblivious RAM, building on recent work, with the main contribution of producing an output in the same format as the inputs so that graph adjacency matrices can be multiplied repeatedly. Repeated multiplication of this kind can find cycles in graphs, a pattern associated with money laundering, and the same approach also detects a related pattern dubbed scatter-gather, giving a concrete technique for privacy-preserving anti-money-laundering detection.
