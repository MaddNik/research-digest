---
title: "SALUS: Large-Scale Homomorphic Circuit Synthesis via Logic-Aware LUT Optimization"
date: 2026-10-23 08:16:00 +0200
categories: [FHE]
tags: [circuit-synthesis, lookup-tables, functional-bootstrapping, boolean-circuits]
link: https://eprint.iacr.org/2026/2561
byline: "Ran Mao et al. (IACR ePrint 2026/2561, Oct 20 2026, IEEE Transactions on Information Forensics and Security)"
description: "SALUS automatically synthesizes and evaluates gate-level graphs over homomorphic lookup tables, achieving up to a 26 times reduction in computational latency over the prior state-of-the-art homomorphic circuit synthesis method."
---

Optimizing fully homomorphic encryption circuits to evaluate Boolean functions over ciphertexts has drawn growing interest, and while functional bootstrapping efficiently evaluates logic gates, evaluation efficiency for large-scale circuits has remained limited. Building on a recent fast ciphertext conversion method that makes it feasible to evaluate look-up tables (LUTs) over a homomorphic multiplexer operation, the authors propose SALUS, a circuit synthesis framework that automatically generates and evaluates gate-level graphs over homomorphic LUTs given an input Boolean circuit. SALUS applies binary decision diagram reordering and multi-value refresh techniques to efficiently evaluate complex LUTs, along with a heuristic algorithm that merges LUTs in a circuit into multi-output LUTs. Across a wide range of benchmark suites, including the EPFL and ISCAS benchmark circuits, SALUS achieves up to a 26 times reduction in computational latency compared with the state-of-the-art homomorphic circuit synthesis method, and on real-world applications such as image filtering and matrix multiplication it achieves an average speedup of 8.6 times, with a maximum speedup of 24 times, over the functional-bootstrapping-based method.
