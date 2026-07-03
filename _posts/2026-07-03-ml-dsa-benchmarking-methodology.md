---
title: "Apples, Oranges, and Signatures: Pitfalls and Methodology in ML-DSA Benchmarking"
date: 2026-07-03 08:10:00 +0200
categories: [PQC]
tags: [ml-dsa, benchmarking, methodology, migration]
link: https://eprint.iacr.org/2026/1333
byline: "Riou et al. (IACR ePrint 2026/1333, Mon 29 Jun 2026)"
description: "This paper documents common mistakes in ML-DSA performance benchmarking and proposes a standardized methodology for fair, migration-relevant comparisons."
---

The authors argue that reliable performance data is essential for post-quantum migration engineering decisions, yet existing ML-DSA benchmarking practices often produce misleading or non-comparable results, including subtle inconsistencies when comparing across security levels. A central technical point is that ML-DSA signing has inherent execution-time variability from rejection sampling and other data-dependent components, which makes commonly reported metrics such as minimum, average, and maximum time unsuitable for migration planning, particularly for real-time systems that need worst-case guarantees. To address this, the paper proposes a benchmarking methodology built on standardized input data sets and clearly qualified reporting metrics, intended to enable fair comparison across different hardware and software implementations and to help designers assess worst-case execution time.
