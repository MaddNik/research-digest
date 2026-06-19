---
title: "Fuzzy PSI from Symmetric Primitives with Exact Logarithmic Dependence on Distance Threshold"
date: 2026-06-19 08:10:00 +0200
categories: [Cryptography]
tags: [fuzzy-psi, oblivious-transfer, private-set-intersection, symmetric-primitives]
link: https://arxiv.org/abs/2606.15093
byline: "Cong Zhang et al. (arXiv:2606.15093, Jun 13 2026)"
description: "Fuzzy private set intersection over Lp distances built from oblivious transfer and symmetric primitives, with optimal logarithmic cost in the distance threshold."
---

This work presents fuzzy private set intersection protocols supporting Lp distances across
multiple dimensions, built from oblivious transfer and symmetric cryptographic operations
instead of additive homomorphic encryption. A central idea is to use prefix representations
to perform fuzzy matching, determining the correct prefixes through equality checks. The
authors argue their construction achieves logarithmic complexity in the distance threshold
delta, which they describe as an information-theoretic lower bound. Experimental results
report improvements of up to 43.7 times in runtime and 31.3 times in communication compared
to prior state-of-the-art fuzzy private set intersection supporting general Lp distances.
The result is notable for removing reliance on public-key homomorphic machinery while
improving concrete efficiency.
