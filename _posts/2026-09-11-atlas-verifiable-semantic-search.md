---
title: "Atlas: Efficient Verifiable Semantic Search"
date: 2026-09-11 08:19:00 +0200
categories: [Cryptography]
tags: [zero-knowledge-proofs, verifiable-search, hnsw, retrieval-augmented-generation]
link: https://arxiv.org/abs/2609.11841
byline: "Nikolay Avramov et al. (arXiv:2609.11841, Sep 10 2026)"
description: "Atlas introduces the first zero-knowledge proof for graph-based HNSW search, letting a provider prove a semantic search query was answered correctly against a committed index in under a second at million-scale."
---

Semantic search underlies recommender systems, web search, and retrieval-augmented generation, but clients must trust that a provider's index and query execution match what was agreed, since a provider could silently truncate search or bias results. Verifiability can remove this trust assumption by proving results follow the agreed algorithm over a committed index, but this is hard for HNSW, the graph-based algorithm used at scale, because its data-dependent traversal maps poorly onto the fixed constraint systems of zero-knowledge proofs. The authors present Atlas, built on three techniques: preprocessing that shifts database-dependent cost offline so per-query proving scales with the traversal, a restructuring of HNSW into a fixed-size-state procedure proven to return the same result, and timestep-tagged batching that merges per-step arguments across the whole traversal. Atlas proves a query in under a second on the SIFT1M benchmark and in 2.0 seconds at 100 million vectors while preserving the recall of plaintext HNSW, and in a complete retrieval-augmented generation pipeline it preserves end-to-end answer quality at lower proving cost than prior verifiable retrieval systems.
