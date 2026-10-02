---
title: "Incrementally Verifiable Computation without Extraction"
date: 2026-10-02 08:30:00 +0200
categories: [Cryptography]
tags: [incrementally-verifiable-computation, indistinguishability-obfuscation, succinct-proofs, crypto-2026]
link: https://eprint.iacr.org/2026/2219
byline: "Abhishek Jain, Surya Mathialagan, and Brent Waters (IACR ePrint 2026/2219, Sep 25 2026, CRYPTO 2026)"
description: "A new indistinguishability-obfuscation-based approach gives the first fully succinct incrementally verifiable computation scheme that avoids extraction-based security proofs entirely."
---

Incrementally verifiable computation, introduced by Valiant at TCC '08, lets someone iteratively prove that a starting configuration reaches a final one through many repeated applications of a possibly non-deterministic machine, and a scheme is fully succinct if its proof size stays independent of both the number of steps and the size of intermediate configurations. The authors develop a new approach to incrementally verifiable computation based on indistinguishability obfuscation that avoids the extraction-based security analyses central to every prior construction. Assuming subexponential hardness of indistinguishability obfuscation and one-way functions, they construct an adaptively sound, fully succinct incrementally verifiable computation scheme for deterministic computations, the first such scheme that does not rely on algebraic assumptions. Under the same assumptions they also obtain a fully succinct two-hop incrementally verifiable computation scheme for NP with non-adaptive soundness, letting one prove that a configuration reaches a final one through a specific intermediate configuration, which the authors describe as the first NP incrementally verifiable computation scheme achieving full succinctness. The constructions rest on a new connection the authors draw between incrementally verifiable computation and secret sharing for s-t connectivity in graphs, and the paper appears as a major revision of a CRYPTO 2026 publication.
