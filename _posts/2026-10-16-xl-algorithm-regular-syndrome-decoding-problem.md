---
title: "Refined Application of the XL Algorithm within the Algebraic Approach to the Regular Syndrome Decoding Problem"
date: 2026-10-16 08:14:00 +0200
categories: [PQC]
tags: [code-based-cryptography, syndrome-decoding, xl-algorithm, algebraic-cryptanalysis]
link: https://eprint.iacr.org/2026/2470
byline: "Hiroki Furue and Yusuke Aikawa (IACR ePrint 2026/2470, Oct 14 2026)"
description: "A refined algebraic attack on the Regular Syndrome Decoding Problem extends the XL algorithm with arbitrary solving degree and shows which variant is faster depending on block size."
---

The Syndrome Decoding Problem underlies code-based cryptography, a leading post-quantum candidate, and the Regular Syndrome Decoding Problem is a variant where the error vector follows a block-wise structure that has become important as more RSDP-based schemes adopt a wider variety of parameter settings. The main algebraic approach to solving RSDP converts an instance into a polynomial system and applies the XL algorithm, and this paper builds on the hybrid algorithm framework of prior work while allowing an arbitrary solving degree d, rather than being restricted to a fixed choice. The authors further develop two variants: an XFL-based method that combines partial Gaussian elimination with variable guessing, and a WXL-based method that exploits the sparsity of the Macaulay matrix. Their complexity analysis across various parameter settings shows that for fixed values of the code length and dimension, the WXL-based variant using a solving degree greater than two becomes particularly efficient when the block size is small, while the original hybrid algorithm is more efficient as the block size grows, giving a more complete picture of RSDP hardness across parameter regimes.
