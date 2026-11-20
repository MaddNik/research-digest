---
title: "Communication-Efficient Threshold-CKKS Aggregation for Secure Cross-Silo Federated Learning"
date: 2026-11-20 08:15:00 +0200
categories: [FHE]
tags: [ckks, threshold-encryption, federated-learning, secure-aggregation]
link: https://eprint.iacr.org/2026/2897
byline: "Jihyung Kook, Dokyeong Kang, Eunsang Lee (IACR ePrint 2026/2897, Nov 15 2026)"
description: "A threshold-CKKS protocol without a trusted key-distribution center cuts the online communication gap between encrypted and plaintext cross-silo federated learning."
---

Federated learning avoids sharing raw data directly, but the model updates that are exchanged can still reveal sensitive information, and homomorphic encryption can protect them if collusion resistance, flexible aggregation, dropout handling, and communication efficiency can all be achieved together. The authors propose a communication-efficient threshold-CKKS protocol for cross-silo federated learning with Full and Sparse profiles that needs no trusted key-distribution center. Independent local encryption keys let the server apply weighting and dropout-aware reaggregation without retransmitting ciphertexts, while the Sparse profile uses RLWE-to-MLWE conversion for fine-grained chunk-wise aggregation and retains compact RLWE packing; seeded ciphertext reconstruction, selective coefficient transmission, and compressed collective decryption further cut communication. The authors establish simulation security against a semi-honest server colluding with up to a bounded number of clients, under a minimum cohort requirement. On CIFAR-10 and CIFAR-100, the Full profile incurs only 0.32 and 0.29 percentage-point accuracy losses at 1.78 and 1.76 times the online communication of plaintext, while at matched accuracy the Sparse profile reduces online communication by factors of about 79 and 84 compared with FedPHE.
