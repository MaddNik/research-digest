---
title: "ROSETTA: Efficient and Accurate Privacy-Preserving LLM Decoding via Hybrid CKKS/TFHE Evaluation"
date: 2026-09-18 08:15:00 +0200
categories: [FHE]
tags: [tfhe, ckks, llm-inference, lookup-tables]
link: https://arxiv.org/abs/2609.16915
byline: "Jiangrui Yu et al. (arXiv:2609.16915, Sep 15 2026, ACM CCS 2026)"
description: "ROSETTA speeds up privacy-preserving LLM decoding by automatically routing each nonlinear operation to whichever of CKKS or TFHE handles it fastest."
---

Fully homomorphic encryption enables privacy-preserving inference for large language models, but existing FHE frameworks are inefficient at evaluating the nonlinear operations that dominate the autoregressive decode stage. The authors observe that nonlinear operations during decoding have heterogeneous workload patterns that a hybrid approach can exploit, and they propose ROSETTA, a hybrid CKKS and TFHE framework built on two contributions. The first is an adaptive segmented lookup-table protocol based on TFHE for efficient and accurate evaluation of nonlinear operations, and the second is a scheme-aware operator-selection framework that automatically assigns each nonlinear operator to either CKKS or TFHE to minimize end-to-end decoding latency. ROSETTA achieves up to 4.8 times faster Softmax evaluation and an overall 1.5 to 2.1 times end-to-end speedup over the prior state-of-the-art framework CacheMir. The paper is accepted at ACM CCS 2026.
