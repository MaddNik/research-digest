---
title: "Shuffling is Not Enough: Breaking Permutation-Based Model Confidentiality in Hybrid FHE Inference"
date: 2026-09-18 08:18:00 +0200
categories: [FHE]
tags: [tfhe, model-extraction, differential-privacy, hybrid-inference]
link: https://arxiv.org/abs/2609.12911
byline: "Jiseung Kim and Hyung Tae Lee (arXiv:2609.12911, Sep 11 2026)"
description: "Researchers show that permutation-based defenses for protecting model confidentiality in hybrid FHE inference can be broken with only a handful of queries per layer, recovering entire neural networks from TFHE transcripts."
---

Hybrid fully homomorphic encryption inference improves practicality by letting a server evaluate linear layers homomorphically while the client decrypts and applies nonlinearities, and some recent schemes try to protect model confidentiality by returning noisy, output-permuted responses justified by shuffle-model differential privacy. The authors show this protection fails in the correctness regime hybrid FHE systems require: for a d-input linear layer, only d+1 admissible queries suffice for exact recovery of a permutation-invariant layer summary, and hence for perfect model distinguishability. They further show that input differential privacy is orthogonal to model confidentiality, and that the local differential privacy premise needed for shuffle amplification cannot hold under correctness-bounded noise. Using this query model, they recover all linear layers of a SAFHIRE-style ResNet-20 end-to-end from TFHE transcripts with zero error using 5,712 total direct queries, and they confirm exact per-layer recovery on pretrained ImageNet-scale CNNs and ViT-B/16 as well. The leaked spectra enable model fingerprinting, lineage attribution, and improved logit-based extraction, while the authors note that suppressing them to prevent the attack destroys inference utility.
