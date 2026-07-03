---
title: "SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval"
date: 2026-07-03 08:17:00 +0200
categories: [FHE]
tags: [ckks, dense-retrieval, embedding-privacy, alignment-attacks]
link: https://arxiv.org/abs/2606.27976
byline: "Kurilenko (arXiv:2606.27976, Fri 26 Jun 2026)"
description: "SHARD hardens dense-embedding retrieval against inversion and alignment attacks by homomorphically reranking a CKKS-encrypted, per-cell-keyed residual."
---

The paper targets a weakness in protected vector stores for semantic search and retrieval-augmented generation: a single global embedding geometry can be recovered via orthogonal Procrustes alignment from a modest number of known plaintext pairs, even under a secret global rotation. SHARD removes this weak axis by rotating the centered embedding and splitting it into a short public prefix, used for stage-one retrieval, and a private residual sharded into a configurable number of cells, each rotated under a separate secret key. The residual is reranked under the CKKS homomorphic encryption scheme, where the per-cell keys cancel out and the inner product remains exact. A single parameter spans the design space from a global-linear baseline to per-document micro-keys, and the authors argue the keyed residual functions as a revocable, renewable, unlinkable template for text embeddings. Across five encoders, the scheme preserves full-dimensional reranking quality, and the authors report that recovering the cell-keyed residual under a diffuse known-plaintext leak costs roughly the number of cells times more anchors than the baseline, holding against learned-linear, non-linear, and unsupervised alignment attacks. The authors characterize SHARD as an attack-aware geometric defense rather than a cryptographic guarantee, noting limits such as within-cell similarity leakage.
