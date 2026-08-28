---
title: "Billion-Scale Nearest-Neighbor Search under Fully Homomorphic Encryption on a Single GPU, Balancing Leakage and Cost"
date: 2026-08-28 08:21:00 +0200
categories: [FHE]
tags: [private-information-retrieval, nearest-neighbor-search, gpu-acceleration, access-pattern-leakage]
link: https://arxiv.org/abs/2608.21131
byline: "Isamu Isozaki et al. (arXiv:2608.21131, Aug 21 2026)"
description: "A GPU-accelerated FHE system answers encrypted billion-scale nearest-neighbor queries in a few seconds by combining rank reduction with hierarchical routing, while quantifying and mitigating the access-pattern leakage this routing introduces."
---

The authors build a system that answers which database vectors are most similar to an encrypted query without the server seeing the query, executing all scoring on ciphertexts under fully homomorphic encryption. Because scoring every row under encryption is far too slow at billion-vector scale, they combine rank reduction, which shrinks each vector's dimension, with a hierarchy that routes to a small candidate set instead of scanning everything, executed under encryption on a single GPU. On DataComp-1B, with 1.39 billion 512-dimensional CLIP vectors, they reach a recall at 10 of 0.90 in about 6 seconds per encrypted query on a GPU, and on Deep1B, with 1 billion 96-dimensional vectors, they reach recall at 10 of 0.90 at 2.3 seconds per query under all-levels FHE. The authors also measure what this speed costs in privacy, showing that the hierarchy's access pattern leaks database geometry, letting an observer recover 72 percent of the coarse-cell neighbor graph from access patterns alone, but that seeded, fixed-group padding cuts this leakage by about 35 times, to roughly 2 percent, where naive padding is defeated by a repeated-query attack.
