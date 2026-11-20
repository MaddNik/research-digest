---
title: "PMKPIR: Parallel Multi-Keyword PIR with Interleaved Batching for Private Boolean Retrieval"
date: 2026-11-20 08:18:00 +0200
categories: [FHE]
tags: [private-information-retrieval, bfv, simd-batching, keyword-search]
link: https://arxiv.org/abs/2611.24248
byline: "Rongxi Wang et al. (arXiv:2611.24248, Nov 18 2026)"
description: "An interleaved batching method built on BFV's SIMD capability lets PMKPIR match multiple keywords and evaluate universal boolean queries in a single database traversal."
---

Keyword private information retrieval lets a user fetch data associated with specific keywords from a database while hiding the query, but existing schemes that support boolean retrieval either need multiple database traversals, raising computational cost, or cannot support universal boolean computation. The authors propose PMKPIR, a keyword PIR scheme that supports both parallel multi-keyword queries and universal boolean computation. It uses the single instruction multiple data capability of BFV homomorphic encryption to build an interleaved batching method, on top of which they design IBPIR for private matching of multiple keywords within a single database traversal. A boolean query processing method then extends the parallel capability of interleaved batching from keyword querying to boolean query computation, supporting universal boolean computation and accelerating boolean operations. Integrating this method with IBPIR yields PMKPIR, which the authors describe as the first keyword PIR scheme to support multi-keyword batch matching within boolean queries while preserving the core security guarantees of classic PIR. Compared with state-of-the-art schemes, PMKPIR reduces query time, communication overhead, storage overhead, and peak memory by up to 79.06, 75.00, 97.92, and 80.26 percent respectively.
