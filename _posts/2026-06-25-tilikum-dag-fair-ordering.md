---
title: "Tilikum: Transaction Fair Ordering on a DAG without Weak Edges"
date: 2026-06-25 08:09:00 +0200
categories: [Cryptography]
tags: [blockchain]
link: https://arxiv.org/abs/2606.27250
byline: "Segalini et al. (arXiv:2606.27250, Wed 25 Jun 2026)"
description: "Fair transaction ordering protocol for DAG-based blockchains achieving 39× higher throughput than baselines."
---

Decentralized Finance applications are vulnerable to transaction reordering attacks that allow adversaries to extract Blockchain Extractable Value, yet while linear blockchain systems have inspired extensive fair ordering research, DAG-based consensus protocols remain largely unprotected despite growing adoption for scalability. This work introduces Tilikum, a DAG-based ledger protocol ensuring fair transaction ordering without relying on weak edges. Tilikum achieves ordering linearizability by leveraging median-based timestamp aggregation or batch order fairness while maintaining low data redundancy and robust garbage collection. The implementation in Rust was evaluated against representative baselines (Narwhal/Tusk, Pompē, Themis, and FairDAG), demonstrating up to 39× higher throughput than other fair-ordering baselines while fully blocking state-of-the-art DAG-specific reordering attacks. This protocol addresses a critical gap in DAG-based systems, enabling fair transaction ordering as scalability improves.
