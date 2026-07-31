---
title: "Low-Latency Bootstrapping for CKKS using Roots of Unity"
date: 2026-07-31 08:13:00 +0200
categories: [FHE]
tags: [ckks, bootstrapping, latency-optimization]
link: https://arxiv.org/abs/2607.27401
byline: "Jean-Sebastien Coron et al. (arXiv:2607.27401, Jul 29 2026)"
description: "Sparse Roots of Unity bootstrapping for CKKS embeds modular reduction directly into complex roots of unity rather than approximating it with polynomials, cutting bootstrapping latency."
---

The paper targets the bootstrapping step of the CKKS approximate-arithmetic FHE scheme, which normally relies on polynomial approximation of modular reduction. The proposed method, Sparse Roots of Unity, instead embeds the additive group modulo q into the complex roots of unity, which CKKS can evaluate natively. This substantially reduces the multiplicative depth required for bootstrapping, which in turn allows smaller ring dimensions to be used. Using the OpenFHE library, the authors report up to a 5 times reduction in latency for ciphertexts with a small number of slots.
