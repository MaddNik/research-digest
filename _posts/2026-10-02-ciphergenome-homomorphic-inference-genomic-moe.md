---
title: "CipherGenome: Homomorphic Inference for Genomic Mixture-of-Experts"
date: 2026-10-02 08:24:00 +0200
categories: [FHE]
tags: [module-lwe, genomic-inference, mixture-of-experts, encrypted-inference]
link: https://arxiv.org/abs/2609.35883
byline: "Guang Yang and Fengchen Liu (arXiv:2609.35883, Sep 27 2026)"
description: "CipherGenome encrypts 95.8 percent of a 15.1-billion-parameter genomic mixture-of-experts model's parameters under module-LWE, closing an inversion attack that otherwise recovers input DNA with 99.8 percent accuracy."
---

Genome foundation models are growing into sparse mixture-of-experts networks whose expert weights no longer fit on the machines that hold the sequences, but the authors show that outsourcing those sequences to rented accelerators is risky: a single server hosting one expert can recover the input nucleotides with 99.8 percent top-1 accuracy. CipherGenome keeps the embedding, attention, and router of a 15.1-billion-parameter mixture-of-experts genome model on a trusted thin client and outsources every expert projection, 95.8 percent of the parameters, to untrusted and possibly colluding GPU servers under module-LWE encryption. The design exploits three structural facts: expert layers are linear between two SwiGLU gates, expert weights are public, and GPU integer tensor cores can evaluate a ciphertext-weight product exactly modulo 2 to the 48th power in a single matrix multiplication, so the client can evaluate the nonlinearity exactly and re-encrypt with fresh secrets, meaning no polynomial approximation or bootstrapping is ever needed. Across 72 windows from 12 bacterial genomes, encryption adds only 2.54 times 10 to the negative 4th power nats per token of KL divergence, below a pre-registered non-inferiority margin and indistinguishable from bf16 inference, while the same inversion attack falls to chance level. A reusable public hint cuts end-to-end latency by 3.54 times, wire compression reduces traffic 6.8 times, per-layer padding reduces routing leakage from 54.9 to 8.9 percent accuracy, and the server-side cost per expert and token is more than six orders of magnitude below a CKKS baseline.
