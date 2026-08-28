---
title: "Bit Operation Cost of “Holdout” Key-Recovery Attacks Against Classic McEliece"
date: 2026-08-28 08:12:00 +0200
categories: [PQC]
tags: [classic-mceliece, code-based-cryptography, bit-operation-cost, cryptanalysis]
link: https://eprint.iacr.org/2026/1786
byline: "Markku-Juhani O. Saarinen (IACR ePrint 2026/1786, Aug 24 2026)"
description: "A living costing analysis tallies bit operations for the holdout key-recovery attack on Classic McEliece and shows that its full end-to-end attack cost is not yet established."
---

This paper tallies bit operations for a proposed holdout key-recovery attack on Classic McEliece using a singleton holdout model where each relation kernel omits one selected public column. The author proves three relation-generation reductions covering different vanishing orders, discarding redundant binary derivative rows, and using injective zero-padding to make the relation matrix square without changing its right kernel. Under these reductions, an exhaustive singleton scan gives a width-64 relation-generation floor of 2 to the 112.35 power bit operations, and charging support-value enumeration and dense curve interpolation gives a conditional subtotal through interpolation of 2 to the 132.22 power for the mceliece348864 parameter set. The author notes that neither figure represents a complete key-recovery cost, since the end-to-end complexity of the full attack route depends on open questions including how many relations higher-order derivative recovery requires and the success probability of binary kernel solving, and explicitly frames the paper as a living costing document to be updated as evidence improves.
