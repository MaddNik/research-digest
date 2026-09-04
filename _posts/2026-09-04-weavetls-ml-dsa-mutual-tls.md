---
title: "WeaveTLS: High-Throughput Cross-Connection ML-DSA Authentication in Mutual TLS"
date: 2026-09-04 08:10:00 +0200
categories: [PQC]
tags: [ml-dsa, mutual-tls, avx-512, lattice-signatures]
link: https://eprint.iacr.org/2026/1828
byline: "Ganqin Liu et al. (IACR ePrint 2026/1828, Aug 28 2026)"
description: "WeaveTLS batches ML-DSA signing and verification across concurrent mutual-TLS connections in an nginx worker, improving one-core throughput by up to 4.31 times over OpenSSL's default post-quantum signature path."
---

Mutual TLS authenticates both peers on every connection, which means every handshake now pays post-quantum ML-DSA signature costs, but batching these operations across concurrent connections is difficult because ML-DSA signing is rejection-divergent, verification uses heterogeneous keys, and synchronous TLS APIs expose authentication work one connection at a time. WeaveTLS is a wire-transparent architecture that executes ML-DSA authentication jointly across concurrent TLS connections, combining rejection-aware slot refill with per-request expanded-key handles and a stackless OpenSSL continuation that lets an nginx worker suspend authentication on one connection to service others through optimized AVX-512 kernels, all while preserving the standard TLS authentication barrier, certificate validation, and wire protocol. On an AMD Ryzen 9 9950X3D, WeaveTLS improves one-core nginx mutual-TLS throughput by 2.81 to 4.31 times over OpenSSL's default ML-DSA path across ML-DSA-44, 65, and 87, and rejection-aware refill makes ML-DSA-65 signing 1.90 times faster than an otherwise identical lockstep schedule. The authors also show that cohort publication weakens client-visible rejection-count timing correlations under load, reducing a potential timing side channel relative to singleton execution.
