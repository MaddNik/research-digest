---
title: "LEASH: When LaBRADOR's Guarantees Go Astray"
date: 2026-11-20 08:22:00 +0200
categories: [Cryptography]
tags: [succinct-arguments, lattice-based-proofs, labrador, parameter-selection]
link: https://eprint.iacr.org/2026/2898
byline: "Xiang Wang, Ji Xiang (IACR ePrint 2026/2898, Nov 15 2026)"
description: "Explicit counterexamples show that LaBRADOR's concrete parameter-selection strategy can fail to preserve completeness even for valid witnesses, prompting targeted repairs to its security analysis."
---

LaBRADOR is a lattice-based succinct argument system that achieves compact proofs through recursive reductions of knowledge, a promising direction for post-quantum succinct verification, but these reductions require careful control of witness norms, relation preservation, and knowledge extraction to maintain their claimed guarantees. The authors revisit the correctness and security analysis of LaBRADOR and construct explicit counterexamples showing that its concrete parameter-selection strategy can fail to preserve completeness, even for valid binary R1CS witnesses. They further identify inconsistencies in the recursive relation transformations and inaccuracies in the probability bounds underlying LaBRADOR's knowledge extraction analysis. The paper develops targeted repairs with corresponding mathematical analyses, examining how changes to norm bounds, decomposition parameters, and challenge distributions affect the resulting security and efficiency guarantees, and the authors argue the results highlight the importance of rigorous parameterization and compositional reasoning in lattice-based succinct proof systems generally.
