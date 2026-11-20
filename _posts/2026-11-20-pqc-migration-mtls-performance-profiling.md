---
title: "PQC Migration: End-to-End Performance Profiling of Post Quantum Cryptographic Algorithms in mTLS"
date: 2026-11-20 08:13:00 +0200
categories: [PQC]
tags: [mtls, performance-profiling, hybrid-key-exchange, tls-1.3]
link: https://arxiv.org/abs/2611.21206
byline: "Rahul et al. (arXiv:2611.21206, Nov 16 2026)"
description: "End-to-end measurements of NIST-standardized post-quantum and hybrid algorithms in TLS 1.3 mutual authentication find no measurable slowdown from pure post-quantum algorithms, but noticeable degradation from hybrid algorithms under poor network conditions."
---

As migration to quantum-safe key exchange and signature algorithms accelerates, the authors analyze the end-to-end performance of TLS with the post-quantum and hybrid cryptographic algorithms standardized by NIST. They build a test setup that evaluates TLS connections between a client and server under various network conditions, focusing on how the new algorithms affect throughput, connection time, energy use, and CPU cycles for TLS 1.3 with mutual authentication. The analysis finds that the standardized post-quantum algorithms introduce no measurable performance degradation despite their larger key lengths, but hybrid algorithms that combine classical and post-quantum components introduce noticeable degradation that becomes more pronounced under adverse network conditions. The authors conclude that migration to hybrid algorithms should be network-condition aware, since poor network conditions can severely hurt TLS 1.3 performance, and they provide code and a web interface for analyzing the performance of different algorithm combinations.
