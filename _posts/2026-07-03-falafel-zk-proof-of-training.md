---
title: "Falafel: Modular Zero-Knowledge Proofs of Training in the Federated Setting"
date: 2026-07-03 08:20:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, federated-learning, verifiable-computation]
link: https://eprint.iacr.org/2026/1335
byline: "Bontekoe et al. (IACR ePrint 2026/1335, Mon 29 Jun 2026)"
description: "Falafel is a modular zero-knowledge proof-of-training scheme for federated learning that lets an external verifier check an entire training pipeline without revealing local data."
---

Falafel produces a zero-knowledge proof of training for federated learning of deep neural networks with a centralized server for weight updates, providing active security during training and publicly verifiable correctness of the final model without revealing local datasets or intermediate model states. It attests both to local training steps and the centralized weight update, and introduces a trusted auditor for input authenticity so an external verifier can check the complete process from dataset to final model. Unlike prior proof-of-training work, the construction relies only on well-understood cryptographic assumptions, is highly parallelizable, and takes a modular commit-and-prove approach with swappable proof components. For LeNet, the authors report generating a proof of about 70 kilobytes in roughly 150 seconds per training round, with proof size 10 to 15 times smaller than prior work while keeping comparable prover time.
