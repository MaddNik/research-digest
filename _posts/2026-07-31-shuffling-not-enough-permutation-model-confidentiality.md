---
title: "Shuffling is Not Enough: Breaking Permutation-Based Model Confidentiality in Hybrid FHE Inference"
date: 2026-07-31 08:17:00 +0200
categories: [FHE]
tags: [tfhe, model-extraction, hybrid-fhe, security-analysis]
link: https://eprint.iacr.org/2026/1527
byline: "Jiseung Kim et al. (IACR ePrint 2026/1527, Jul 25 2026)"
description: "Noise-flooding and output-permutation defenses used in hybrid FHE inference systems fail to protect model confidentiality, enabling exact parameter recovery including on TFHE-based networks."
---

The paper analyzes hybrid FHE inference systems where servers add noise and permute outputs to try to hide model parameters from clients. The authors prove that for a linear layer with d inputs, d plus 1 admissible queries suffice for exact recovery of that layer's parameters, and argue that input differential privacy does not protect model confidentiality and that assumptions underlying shuffle-based amplification cannot hold under correctness constraints. They demonstrate the attack by recovering all linear layers, with zero error, from neural networks including a TFHE-based ResNet-20 and ImageNet-scale convolutional networks, using a total of 5,712 direct queries. The recovered parameters are shown to enable model fingerprinting and lineage attribution, and the authors note that preventing this leakage compromises inference utility.
