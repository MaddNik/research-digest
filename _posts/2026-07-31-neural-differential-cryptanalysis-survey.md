---
title: "Rich Input Representations in Neural Differential Cryptanalysis: A Taxonomy and Survey"
date: 2026-07-31 08:23:00 +0200
categories: [Cryptography]
tags: [cryptanalysis, neural-cryptanalysis, symmetric-key]
link: https://eprint.iacr.org/2026/1530
byline: "Alireza Gholizadeh Shahrbejari et al. (IACR ePrint 2026/1530, Jul 26 2026)"
description: "A survey and taxonomy organizes how neural differential distinguishers encode their inputs, spanning single-pair, multi-pair, multi-difference, and structured-encoding representations used in symmetric-key cryptanalysis."
---

Since deep-learning-based attacks on round-reduced SPECK, neural differential distinguishers have become an active line of symmetric-key cryptanalysis, and this survey focuses specifically on how the input to such classifiers is represented rather than on network architecture. The authors propose a representation-centric framework describing any input representation by five components: its difference set, number of observations per sample, sharing structure, encoding function, and ciphertext cost. Using this framework they organize prior work, from single ciphertext-pair inputs to multi-pair, matrix-style, multi-round, and score-aggregation approaches, into representation families and compare their tradeoffs. They argue that comparisons of these distinguishers must be cost-aware, since fixed-sample and fixed-ciphertext comparisons can yield different conclusions about which representation is better. The paper closes by listing open problems including automated representation search, theoretical explanation of representation gains, and cross-cipher transferability.
