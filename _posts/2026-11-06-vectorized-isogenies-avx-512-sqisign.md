---
title: "Vectorized (2, 2)-Isogenies in the Theta Model Using AVX-512 and Applications to SQIsign"
date: 2026-11-06 08:08:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-cryptography, avx-512, vectorization]
link: https://eprint.iacr.org/2026/2773
byline: "Marius A. Aardal et al. (IACR ePrint 2026/2773, Nov 4 2026)"
description: "A new AVX-512 implementation vectorizes two-dimensional isogeny computations and speeds up SQIsign signature verification by up to 3.4 times."
---

Higher-dimensional isogenies are a key building block of isogeny-based post-quantum cryptography, including the SQIsign signature scheme, but evaluating these isogenies remains computationally expensive. This paper presents a high-performance AVX-512 implementation that exploits the data-level parallelism of these isogeny computations. The authors build a code generator that produces efficient AVX-512 arithmetic over the base field and its quadratic extension for the Montgomery-friendly primes used by several two-dimensional isogeny protocols, including SQIsign, and use it to vectorize isogeny formulas from prior work. The resulting implementation accelerates Round 2 SQIsign verification by 2.5 times at NIST security level I and by 3.2 to 3.3 times at levels III and V, with Round 3 SQIsign verification sped up by 3.1 to 3.4 times. The code generator also directly supports the larger primes used in Round 3 SQIsign parameter sets.
