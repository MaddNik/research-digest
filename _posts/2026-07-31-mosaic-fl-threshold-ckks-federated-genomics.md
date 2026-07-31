---
title: "MOSAIC-FL, a Micro-Service Based Privacy-Preserving Framework with Application to Genomics"
date: 2026-07-31 08:14:00 +0200
categories: [FHE]
tags: [ckks, threshold-fhe, federated-learning, genomics]
link: https://arxiv.org/abs/2607.25107
byline: "Paul Largillier et al. (arXiv:2607.25107, Jul 27 2026)"
description: "MOSAIC-FL is a micro-service federated learning framework that uses threshold CKKS homomorphic encryption for blind, fault-tolerant model aggregation, applied to genomic classification."
---

The framework combines a gRPC communication layer and a finite state machine for synchronization and threat detection with a fault-tolerant secure aggregation protocol built on a threshold variant of CKKS. Aggregation requires only t-out-of-N active clients to decrypt, and the design aims to minimize communication overhead through both cryptographic and network-level choices. The authors state they ensure IND-CPA-D security through noise flooding and mitigate a recent key-recovery attack on synchronized decryptors by renewing collective key material every round. Evaluation covers image recognition on EMNIST and genomic classification tasks including breast cancer subtyping on TCGA data, across varying threshold values and model scales.
