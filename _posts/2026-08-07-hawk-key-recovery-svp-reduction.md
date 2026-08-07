---
title: "HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1"
date: 2026-08-07 08:01:00 +0200
categories: [PQC]
tags: [lattice, signature-scheme, hawk]
link: https://eprint.iacr.org/2026/1593
byline: "Zygimantas Straznickas and Stephen A. Weis (IACR ePrint 2026/1593, Aug 3 2026)"
description: "An unconditional polynomial-time reduction shows HAWK-n key recovery can be solved via shortest-vector-problem oracle calls in dimension n/2+1, sharply cutting the scheme's estimated security."
---

This paper presents a deterministic, unconditional polynomial-time reduction from key recovery in the HAWK lattice signature scheme to calls to a shortest vector problem (SVP) oracle operating in dimension n divided by 2, plus 1. The reduction exploits a nontrivial automorphism of the key lattice, arising from the Galois involution that sends the root of unity to its negation, which can itself be recovered as a shortest vector of a public rank-n lattice. In the gate-count security model, the authors report that the attack reduces the estimated key-recovery cost of HAWK-512 from 2 to the 150th power down to 2 to the 108th power, and HAWK-1024 from 2 to the 288th power down to 2 to the 182nd power. They also provide a practical implementation that recovers a full HAWK-256 secret key in a few hours on a single server. The authors note the method does not apply to the related Falcon scheme, and that certain conductor values are not affected by the attack.
