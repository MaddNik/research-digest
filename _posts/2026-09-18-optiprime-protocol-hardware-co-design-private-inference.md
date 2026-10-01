---
title: "OptiPrime: Optimizing Private Inference through Protocol-Hardware Co-design"
date: 2026-09-18 08:20:00 +0200
categories: [FHE]
tags: [homomorphic-encryption, mpc, private-inference, hardware-accelerator]
link: https://arxiv.org/abs/2609.16898
byline: "Jiangrui Yu et al. (arXiv:2609.16898, Sep 15 2026, MICRO 2026)"
description: "OptiPrime co-designs a new homomorphic-encryption convolution protocol with a matching hardware dataflow, cutting private DNN inference latency by up to 5.7 times on CPUs and 4.2 times with an accelerator."
---

Private deep neural network inference built on hybrid homomorphic encryption and multi-party computation can protect user data with formal guarantees, but the latency overhead from homomorphic encryption is severe, and the authors find that plugging a commercial HE accelerator into state-of-the-art HE-MPC frameworks yields only limited end-to-end gains because those frameworks require wireless transmission of input and output ciphertexts for every HE operation, creating a network communication bottleneck. They introduce OptiPrime, a protocol-hardware co-optimization framework whose new HE protocol for convolutions substantially reduces the number of transmitted output ciphertexts to relieve that bottleneck. Because the new protocol shifts to more complex computation over fewer output ciphertexts, it introduces new memory-access pressure from a high volume of weight plaintexts and intermediate ciphertexts, which OptiPrime addresses with a lightweight compression system for weight plaintexts that cuts memory traffic by 10 times, plus a specialized dataflow that maximizes on-chip reuse of intermediate ciphertexts. Extensive experiments show OptiPrime outperforms the Cheetah baseline by up to 5.7 times on CPUs and 4.2 times with an accelerator. The paper is accepted at MICRO 2026.
