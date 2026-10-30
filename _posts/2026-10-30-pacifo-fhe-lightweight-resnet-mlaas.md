---
title: "Pacifo: An Efficient Fully Homomorphic Encryption-based Lightweight ResNet for Trustworthy Machine Learning as a Service"
date: 2026-10-30 08:22:00 +0200
categories: [FHE]
tags: [privacy-preserving-inference, resnet, relu-approximation, machine-learning-as-a-service]
link: https://arxiv.org/abs/2610.33525
byline: "Yang Li et al. (arXiv:2610.33525, Oct 24 2026)"
description: "Pacifo fine-tunes ResNet20 with a public-private layer partitioning scheme and an efficient ReLU approximation under FHE, achieving 3.7 to 21.7 times faster inference than prior FHE ResNet20 implementations while keeping 95 to 99 percent of plaintext accuracy."
---

Machine Learning as a Service raises privacy concerns because raw client data typically must be uploaded to a server for inference, and while fully homomorphic encryption allows computing directly on encrypted data, current private inference implementations remain slow due to the cost of FHE operations. This paper presents Pacifo, a framework that adapts customized fine-tuning strategies to efficiently evaluate the ResNet20 model under FHE. Pacifo introduces a public-private layer partitioning scheme and an efficient ReLU approximation that together significantly reduce the number of private layers and costly FHE operations needed during inference, while offering flexible security configurations to accommodate different client privacy requirements. Compared to state-of-the-art FHE implementations of ResNet20, Pacifo achieves a runtime speedup of 3.7 to 21.7 times while preserving 95 to 99 percent of the original plaintext model's accuracy across downstream tasks, and the authors have open-sourced the implementation.
