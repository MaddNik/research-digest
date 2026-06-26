---
title: "bioETH-Beacon: A Confidential On-Chain Genomic Beacon with Encrypted Counts, Filters, and Bounded Noise over a Fully Homomorphic EVM"
date: 2026-06-19 08:09:00 +0200
categories: [FHE]
tags: [privacy, fhe, blockchain]
link: https://arxiv.org/abs/2606.20315
byline: "Christos Galanopoulos et al. (arXiv:2606.20315, Jun 18 2026)"
description: "A smart-contract prototype running encrypted genomic beacon count queries on a fully homomorphic Ethereum Virtual Machine."
---

bioETH-Beacon is a smart-contract prototype that enables Beacon aggregate count queries
over encrypted data on a fully homomorphic Ethereum Virtual Machine, removing the need for
a trusted compute evaluator. Hospitals upload encrypted genomic data, researchers submit
encrypted queries, and contracts return encrypted responses distributed through an
off-chain key service. The system uses a tiered design that trades confidentiality against
query cost. It can also add bounded noise to the results to counter probing attacks. The
authors present it as a research prototype for privacy-preserving genomics on blockchain
infrastructure, described across 11 pages with figures and tables.
