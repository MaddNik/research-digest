---
title: "NOMOS: Secure Non-Interactive kNN under CKKS"
date: 2026-10-02 08:21:00 +0200
categories: [FHE]
tags: [ckks, k-nearest-neighbor, encrypted-ranking, top-k-selection]
link: https://eprint.iacr.org/2026/2262
byline: "Shihao Li et al. (IACR ePrint 2026/2262, Sep 29 2026)"
description: "NOMOS speeds up encrypted k-nearest-neighbor ranking under CKKS with a gap-amplified sign approximation, cutting latency by up to 828 times on candidate-set workloads."
---

The k-nearest-neighbor algorithm is a core primitive for similarity search over sensitive data, but evaluating it under fully homomorphic encryption is expensive because it needs distance computation, encrypted ranking, and top-k extraction together, and while CKKS is attractive here for its packed approximate arithmetic, existing CKKS-based systems such as Engorgio incur high overhead when reranking candidate sets. NOMOS targets that ranking and top-k bottleneck directly, building on Mazzone et al.'s matrix-based ranking method but introducing a gap-amplified sign approximation that focuses precision on near-zero distance gaps, the region where k-nearest-neighbor rank decisions are most sensitive. It integrates this primitive into a complete encrypted k-nearest-neighbor pipeline using slot-index alignment and ReLU-based top-k extraction to avoid full sorting, and for large databases it uses offline k-means preprocessing to form fixed-capacity candidate sets so sign-approximation calls scale near-linearly with clustering rather than growing quadratically with database size. Across the Mazzone-style ranking benchmark and candidate-set workloads compared with Engorgio, NOMOS cuts latency by nearly 8 times and up to 828 times respectively, and on the real-world SIFT dataset it achieves 100 percent top-1 and top-8 retrieval accuracy on the evaluated candidate sets.
