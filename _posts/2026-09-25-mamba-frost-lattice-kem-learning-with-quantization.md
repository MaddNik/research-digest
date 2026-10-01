---
title: "MAMBA-Frost: A Lattice KEM from Learning With Quantization"
date: 2026-09-25 08:10:00 +0200
categories: [PQC]
tags: [lattice-kem, learning-with-quantization, key-encapsulation, nist-submission]
link: https://eprint.iacr.org/2026/2136
byline: "Shanxiang Lyu, Ke Ma, and Junzuo Lai (IACR ePrint 2026/2136, Sep 22 2026)"
description: "A key encapsulation mechanism built on Learning With Quantization uses power-of-two arithmetic to beat FrodoKEM-640 on both size and speed."
---

Learning With Errors gives a conservative security foundation for lattice cryptography, while Learning With Rounding improves bandwidth but resists tight reductions to LWE because its rounding noise correlates with the hidden linear term. The authors build on the Learning With Quantization framework, which replaces additive noise with quantization error under a tight reduction from LWE, by instantiating the quantization lattice as a scaled integer lattice with aligned power-of-two moduli. This yields MAMBA-Frost, a plain LWQ-based key encapsulation mechanism that pairs unstructured LWE security with quantization-based compression and operates entirely with hardware-friendly power-of-two arithmetic. The authors instantiate the scheme, called Frost, at NIST security levels 1, 3, and 5, submitted as a first-round candidate to the NICCS next-generation commercial cryptographic algorithms call. At level 1, Frost-128 reduces combined public-key and ciphertext size by about 40 percent versus FrodoKEM-640 and about 8 percent versus SCloud+-128, while achieving AVX2 speedups of 2.3, 1.8, and 1.5 times for key generation, encapsulation, and decapsulation over FrodoKEM-640.
