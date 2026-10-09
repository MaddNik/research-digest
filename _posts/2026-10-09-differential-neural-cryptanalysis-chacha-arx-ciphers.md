---
title: "Differential-Neural Cryptanalysis of ChaCha and Related ARX Stream Ciphers"
date: 2026-10-09 08:28:00 +0200
categories: [Cryptography]
tags: [chacha, neural-distinguisher, differential-cryptanalysis]
link: https://eprint.iacr.org/2026/2382
byline: "Nimai Parsa and Nitin Kumar Sharma (IACR ePrint 2026/2382, Oct 6 2026)"
description: "The first differential-neural cryptanalysis of the Salsa, ChaCha, and Forro family of ARX stream ciphers trains six neural architectures and produces new reduced-round distinguishers, including a perfect one for Forro."
---

This paper presents what the authors describe as the first differential-neural cryptanalysis of the Latin Dances family of ARX stream ciphers, Salsa, ChaCha, and Forro. They train and compare six neural architectures, including Gohr's residual network, DBitNet, an Inception network, an MLP-ResNet, an SE-ResNet, and a self-attention network, on a 3-round reduced version of ChaCha, in both the classical single-pair setting and a multi-pair setting that combines up to sixteen ciphertext pairs through a log-odds rule. Extending the study to the other ARX ciphers, they give the first distinguisher for 4.5 rounds of Salsa, reaching 0.53 accuracy for one pair and 0.60 for sixteen pairs, and the first distinguisher for 1.25 rounds of Forro with accuracy of 1 for both single and multiple pairs. They also introduce a family of experimental round-1-XOR variants that isolate the contribution of first-round diffusion to distinguishability, and four explainability experiments on the trained 3-round ChaCha distinguisher show that, although the output difference is its dominant feature, its decision is better interpreted as a learned mixture of round-1 truncated differentials, five of which already account for 99 percent of high-confidence ciphertext pairs.
