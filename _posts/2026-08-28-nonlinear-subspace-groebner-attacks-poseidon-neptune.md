---
title: "Beyond Linear Subspace Trails: Nonlinear Subspaces for Gröbner Basis Attacks on Poseidon/Poseidon2 and Neptune"
date: 2026-08-28 08:26:00 +0200
categories: [Cryptography]
tags: [poseidon, zero-knowledge-friendly-hashes, groebner-basis, algebraic-cryptanalysis]
link: https://eprint.iacr.org/2026/1792
byline: "Enyan Li et al. (IACR ePrint 2026/1792, Aug 24 2026)"
description: "Extending linear subspace trails to nonlinear subspaces lets Groebner basis attacks reach roughly twice as many internal partial rounds of the zero-knowledge-friendly hash functions Poseidon, Poseidon2, and Neptune."
---

Poseidon, Poseidon2, and Neptune are prominent hash primitives for zero-knowledge proof systems, and Groebner basis methods are a central tool for evaluating their resistance to algebraic attacks, with prior work showing that linear subspace trails can reduce the algebraic degree of partial rounds in constrained-input-constrained-output problems. This paper extends the linear subspace trail framework to nonlinear subspaces by introducing a parametric Macaulay matrix method that transforms the search for degree-reducing algebraic constraints into solving a parametric system, allowing the construction of longer nonlinear subspace trails that suppress degree growth over more internal partial rounds. For a given number of extra constraints, the authors show the nonlinear subspace trail can cover up to twice as many internal rounds as the previous linear subspace trail, and they further propose subspace modeling variants that avoid variable substitution by imposing constraints directly on high-degree intermediate states. On Poseidon/Poseidon2 and Neptune instances proposed at ToSC 2025, their nonlinear subspace model analyzes approximately twice as many internal partial rounds as the linear model under the same complexity and cost assumptions, and for several concrete instances it reaches or exceeds the designers' recommended round counts.
