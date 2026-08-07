---
title: "GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG"
date: 2026-08-07 08:22:00 +0200
categories: [FHE]
tags: [ckks, retrieval-augmented-generation, privacy-preserving-search]
link: https://arxiv.org/abs/2607.29019
byline: "Yang Gao et al. (arXiv:2607.29019, Jul 31 2026)"
description: "A CKKS-based encrypted retrieval scheme for privacy-preserving retrieval-augmented generation avoids interactive ranking protocols by selecting documents above a similarity threshold."
---

This paper targets retrieval-augmented generation systems where document retrieval must happen over encrypted data without leaking the query or corpus contents. Instead of ranking all documents homomorphically, which is computationally expensive, the method selects documents whose similarity score exceeds a threshold, cutting down the work needed per query. The scheme is built on CKKS-based homomorphic computation and introduces a precision-stable mask polarization method to ensure the selected documents are recovered accurately. According to the abstract, experiments show the approach matches the effectiveness of ranking-based encrypted retrieval while substantially reducing latency, positioning threshold-based selection as a practical basis for scalable private retrieval-augmented generation systems.
