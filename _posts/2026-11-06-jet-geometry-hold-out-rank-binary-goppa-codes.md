---
title: "Projective Jet Geometry and Hold-Out Rank of Binary Goppa Codes"
date: 2026-11-06 08:10:00 +0200
categories: [PQC]
tags: [classic-mceliece, code-based-cryptography, goppa-codes, cryptanalysis]
link: https://eprint.iacr.org/2026/2769
byline: "Yongge Wang (IACR ePrint 2026/2769, Nov 4 2026)"
description: "A projective-geometric framework explains the higher-order polynomial relations exploited by recent structural attacks on the binary Goppa codes used in Classic McEliece."
---

Recent structural distinguishers and key-recovery methods against Classic McEliece exploit higher-order polynomial relations among the columns of its public generator matrix. This paper develops a projective-geometric and algebraic framework for these relations, realizing the public columns as rational points on a hidden curve and translating higher-order vanishing conditions into fat-point conditions pulled back along that curve's parametrization. The authors give an exact characterization of the codimension of the space containing products of code polynomials, along with a Frobenius-descent theorem relating vanishing on the hidden curve to vanishing on the union of its Frobenius conjugates. They derive Hilbert-function bounds from this theory, including a multilinear bound verified on twenty-six of twenty-seven tested Classic-McEliece-shaped keys. An experimental pipeline running the jet system of the recent attacks, without the key-recovery steps, confirms the predicted hidden-curve structure on six independently generated keys, clarifying the nuisance-space structure behind these attacks.
