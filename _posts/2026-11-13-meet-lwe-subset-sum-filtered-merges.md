---
title: "Filtered merges make deeper representation trees pay: Subset Sum and Meet-LWE"
date: 2026-11-13 08:13:00 +0200
categories: [PQC]
tags: [lattice-cryptanalysis, meet-lwe, subset-sum, representation-technique]
link: https://eprint.iacr.org/2026/2802
byline: "Nick Howgrave-Graham (IACR ePrint 2026/2802, Nov 6 2026)"
description: "Adding bucketing-code filters to representation-technique merges improves the best known exponents for both random Subset Sum and May's Meet-LWE attack on ternary lattice keys."
---

Dubiner's bucketing codes, used as type-class filters on representation coordinates, let a merge step avoid generating matched pairs with the wrong split pattern. The author shows that in representation trees their main effect is to make going deeper in the tree pay off. For random density-one Subset Sum, the filters improve the exponent of the Bonnetain-Bricout-Schrottenloher-Shen attack from 0.2831, as recomputed here, to 0.2690 at search depth 5, with no better point found up to depth 9. For May's Meet-LWE attack on ternary lattice keys, the filters improve the asymptotic exponent by 0.013 to 0.023 for key weights of 0.375 or higher. The paper identifies precisely where filters can and cannot help, a survival recursion that justifies the accounting, and a symmetry lemma showing the filters do not bias the planted solution, with simulations supporting the remaining heuristics.
