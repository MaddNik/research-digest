---
title: "Exploiting Load/Store Leakage of Sparse Vectors for Key Recovery in HQC"
date: 2026-07-24 08:25:00 +0200
categories: [Hardware Security]
tags: [hqc, post-quantum-kem, electromagnetic-leakage, sparse-vector]
link: https://eprint.iacr.org/2026/1491
byline: "Gustavo Banegas et al. (IACR ePrint 2026/1491, Jul 23 2026)"
description: "The paper presents a physical side-channel attack that recovers HQC secret keys by observing which memory words holding the sparse secret vector are zero versus nonzero during load and store operations."
---

The researchers target HQC, a NIST-standardized code-based key encapsulation mechanism, using electromagnetic measurements collected from a Cortex-M4 processor. They exploit load and store leakage in the manipulation of HQC's sparse secret vectors with a zero-word distinguisher that identifies zero versus nonzero machine words. For HQC-1 they find approximately 88.7 percent of machine words are zero at 32-bit granularity, which reduces the remaining decoding problem to about 2 to the power of 46 bit operations. Experimental validation required roughly 500 traces for stronger signal conditions and 5,000 traces for weaker ones, and the paper discusses countermeasures.
