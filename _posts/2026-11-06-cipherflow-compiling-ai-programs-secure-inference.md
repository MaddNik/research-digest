---
title: "CipherFlow: Compiling AI Programs for Efficient Cryptographically Secure Inference"
date: 2026-11-06 08:18:00 +0200
categories: [FHE]
tags: [fhe-mpc-compiler, secure-inference, hybrid-protocols, neurips]
link: https://arxiv.org/abs/2611.01450
byline: "Hedong Zhang, Mengxin Zheng, and Qian Lou (arXiv:2611.01450, Nov 1 2026)"
description: "CipherFlow compiles AI computation graphs into latency-optimized secure inference programs that jointly plan homomorphic encryption and secure multiparty computation placement."
---

Cryptographically secure inference is hard to deploy because developers must correctly compose cryptographic primitives while performance depends on the hardware, network, and the ever-changing ciphertext state of a computation. This paper presents CipherFlow, a compiler framework that takes a high-level AI computation graph, a library of available cryptographic primitives, and a target hardware and network configuration, and generates an executable, latency-optimized secure inference program automatically. CipherFlow combines three techniques: MicroBench, which profiles deployment-specific primitive costs; state-expanded planning, which jointly optimizes the placement of homomorphic encryption and secure multiparty computation operations, their conversions, and ciphertext maintenance under cryptographic-state constraints; and BlockFold, which summarizes branched regions so planning scales to full Transformer graphs. Using measured homomorphic encryption and MPC backend costs across CPU, GPU, and network settings, the evaluation shows up to 16.5 times speedup on BERT-base and over 22 times speedup on ViT compared with static hybrid placement baselines. The paper, accepted at NeurIPS 2026, separates AI model programming from cryptographic execution decisions so that developers can express computations while the compiler builds the efficient secure program.
