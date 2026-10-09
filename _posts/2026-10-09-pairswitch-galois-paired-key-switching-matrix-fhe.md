---
title: "PairSwitch: Efficient Galois-Paired Key Switching for Gentry-Lee Matrix FHE"
date: 2026-10-09 08:18:00 +0200
categories: [FHE]
tags: [matrix-fhe, key-switching, galois-automorphisms]
link: https://eprint.iacr.org/2026/2373
byline: "Zhenyu Xiong, Mingsheng Wang, and Han Wang (IACR ePrint 2026/2373, Oct 6 2026)"
description: "PairSwitch halves the key material needed for the BigSwitch operation in Gentry-Lee matrix fully homomorphic encryption while matching or beating the speed of the original, larger-key construction."
---

Matrix-native fully homomorphic encryption, introduced by Gentry and Lee, multiplies encrypted matrices with a trace product and then converts the four-component output back to an ordinary ciphertext using a BigSwitch operation, whose keys over an extended ring dominate the scheme's key material. The authors propose a pair-merge BigSwitch that rewrites the target of each diagonal so it can borrow its inverse's product key at the cost of one Galois step, cutting the number of product keys needed roughly in half while proving that no per-diagonal BigSwitch with the same number of key switches can use fewer keys. Building on this, they introduce public key rebasing, which turns Galois keys into product keys using one relinearization key placed one small modulus layer above the chain, so clients publish only as many keys as the prior Trace-Factored BigSwitch plus one compact layer key. On the parameters used by prior work, their implementation runs a BigSwitch 1.89 to 1.99 times faster than the Trace-Factored BigSwitch and 1.28 to 1.38 times faster than the original BigSwitch, with less noise growth than the factored version, and the code is publicly available.
