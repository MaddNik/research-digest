---
title: "Privacy-Preserving GNN Inference on Financial Transaction Graphs via Homomorphic Encryption"
date: 2026-10-16 08:21:00 +0200
categories: [FHE]
tags: [ckks, graph-neural-networks, anti-money-laundering, encrypted-inference]
link: https://arxiv.org/abs/2610.18054
byline: "H. Cagri Bilgi et al. (arXiv:2610.18054, Oct 13 2026)"
description: "A CKKS-based graph neural network inference framework lets multiple banks jointly run anti-money-laundering models on encrypted transaction features without exposing plaintext data to a central server."
---

Anti-money laundering in financial networks requires modeling transaction patterns that span multiple institutions, but banks cannot share account and transaction features in plaintext due to privacy regulations. The authors propose a privacy-preserving graph neural network inference framework for this multi-bank setting, where a central server holds the graph connectivity and pretrained model weights in plaintext while each bank keeps its transaction features encrypted under the CKKS homomorphic encryption scheme, so inference runs entirely on encrypted features and no plaintext features or predictions reach the server. The key enabler is an edge-centric graph neural network architecture that expresses message passing through operations on node-edge incidence matrices, preserving the edge-attributed multigraph structure of transaction networks while reducing every aggregation step to plaintext-ciphertext matrix products. Since CKKS can only evaluate polynomial circuits, each nonlinearity is approximated with a composite polynomial of the sign function, calibrated per activation site. On the IBM anti-money-laundering benchmark the model matches plaintext baseline performance, and with a consumer-grade GPU it classifies each queried transaction end to end in as little as 5.31 seconds, with per-transaction latency amortized to 1.65 seconds when optimized for throughput.
