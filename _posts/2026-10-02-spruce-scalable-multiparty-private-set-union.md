---
title: "SPRUCE: Scalable Multiparty Private Set Union in Constant Rounds"
date: 2026-10-02 08:28:00 +0200
categories: [Cryptography]
tags: [private-set-union, multiparty-computation, constant-round-protocols, secure-shuffling]
link: https://eprint.iacr.org/2026/2188
byline: "Zhengwei Tong, Saba Eskandarian, Jonathan Katz, and Kartik Nayak (IACR ePrint 2026/2188, Sep 26 2026)"
description: "SPRUCE removes the sequential shuffling step that prior multiparty private set union protocols needed, running in constant rounds regardless of party count and outperforming prior work by an order of magnitude."
---

Multiparty private set union lets a group of mutually distrusting parties, each holding a private set, learn the union of their sets without revealing anything else, a primitive useful for tasks like cyber-risk assessment and private record matching. State-of-the-art protocols require parties to sequentially shuffle encrypted values to hide which party contributed which inputs to the final result, which ties round complexity to the number of parties. The authors introduce a new paradigm for semi-honest multiparty private set union that eliminates this sequential shuffling, letting the protocol run in constant rounds no matter how many parties are involved, while also improving parallelism, giving an information-theoretic online phase, and natively supporting unbalanced input sizes without the padding most prior work needs to hide individual set sizes. An implementation and evaluation across party counts, input sizes, and network conditions shows that in the unbalanced setting SPRUCE significantly outperforms the state-of-the-art PULSE (CCS '25) and DZBC25 (USENIX Security '25) protocols, while in the balanced setting it achieves an order-of-magnitude improvement over PULSE in most settings and beats DZBC25 in wide-area-network deployments with 100 millisecond latency.
