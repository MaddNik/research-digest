---
title: "Signed Dyadic Path Encoding for Efficient Non-Interactive Private Decision Tree Evaluation over TFHE"
date: 2026-11-13 08:20:00 +0200
categories: [FHE]
tags: [tfhe, decision-trees, programmable-bootstrapping, private-inference]
link: https://arxiv.org/abs/2611.16818
byline: "Xintong Song et al. (arXiv:2611.16818, Nov 12 2026)"
description: "A new signed dyadic path-sum encoding nearly halves the number of programmable bootstraps needed for non-interactive private decision tree evaluation over TFHE."
---

Private decision-tree evaluation lets a server classify a client's encrypted query without learning the input, and in the non-interactive, path-based setting over TFHE, the server returns a single encrypted prediction by aggregating per-path comparison outcomes, where the standard per-leaf formulation pays one programmable bootstrap per leaf, dominating the cost. The authors propose a signed dyadic path-sum encoding that nearly halves this cost: each internal node receives a signed dyadic label so that every root-to-leaf path accumulates a distinct integer sum, letting the two children of a leaf-parent be packed into a single test polynomial and resolved by one programmable bootstrap, reducing the bootstrap count from the number of leaves to the number of leaf-parents. They formalize the distinct-sum property and prove that the dyadic labeling is the range-minimal encoding satisfying it, with its half-symmetric signed form being magnitude-optimal, tightening the comparison-stage noise bound at fixed parameters. They derive the conditions under which encrypted evaluation returns the exact prediction, instantiate parameters with a per-inference failure probability below 2 to the power of negative 64 at 128-bit security, and show that the ring degree grows linearly with the consumed plaintext range, confining the profitable regime to tree depths of 4 or less. On standard UCI benchmarks at depths 1 through 4, the method reduces single-tree latency by 1.51 to 1.92 times and ensemble latency by 2 times, without accuracy loss, while preserving a compact, non-interactive response.
