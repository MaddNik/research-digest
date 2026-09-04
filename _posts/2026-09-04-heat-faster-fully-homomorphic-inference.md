---
title: "HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation"
date: 2026-09-04 08:17:00 +0200
categories: [FHE]
tags: [encrypted-inference, bootstrapping, gpt-2, fine-tuning]
link: https://arxiv.org/abs/2609.01730
byline: "Alessandro Zirilli et al. (arXiv:2609.01730, Sep 1 2026)"
description: "HEAT fine-tunes a model so its per-nonlinearity bootstrapping-iteration counts become learnable alongside the weights, cutting encrypted GPT-2 decoding latency by 1.4 times."
---

Fully homomorphic encryption lets a server run a language model on encrypted prompts, but every nonlinearity must be approximated by an iterative method whose multiplications consume the limited depth budget before a costly bootstrap is needed, and existing approaches fix the iteration count uniformly across the whole model rather than tailoring it to each site's actual error tolerance. The authors introduce Homomorphic Encryption-Aware Training (HEAT), a fine-tuning method that makes the per-nonlinearity iteration counts learnable so they can co-adapt with the model weights during training, optimizing iteration counts against the task objective without architectural changes or retraining from scratch. On encrypted GPT-2 decoding, HEAT reduces the number of iterations by 3.1 times, the number of bootstraps by 1.6 times, and end-to-end latency by 1.4 times, while also improving decode agreement over a calibrated baseline.
