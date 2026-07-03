---
title: "Revisiting the Quantum Indifferentiability of Merkle-Damgard: Proof Limitations and Optimal Consistency"
date: 2026-07-03 08:12:00 +0200
categories: [PQC]
tags: [quantum-indifferentiability, merkle-damgard, hash-functions, provable-security]
link: https://eprint.iacr.org/2026/1347
byline: "Guo et al. (IACR ePrint 2026/1347, Tue 30 Jun 2026)"
description: "A new modular quantum game-playing framework fixes part of a broken proof of Merkle-Damgard's quantum indifferentiability and shows a fundamental gap remains in the rest."
---

The quantum indifferentiability of the Merkle-Damgard hash-function domain extender is a foundational problem for post-quantum cryptography, made more urgent after critical flaws were reportedly identified in existing consistency proofs for the construction. This paper generalizes the compressed oracle proof technique into a modular quantum game-playing framework for systems built from random functions, applying it to the two games such proofs reduce to: an indistinguishability game and a consistency game. On the positive side, the authors develop an error-propagation technique to track coherence penalties and bad sampling branches in the consistency game, yielding a tight consistency bound of O(q_s to the power 3 over 2, divided by 2 to the power n over 2), matching the optimal complexity of generic quantum collision attacks. On the negative side, using the same framework they identify a fundamental obstruction in the indistinguishability game, present even in the original proof it builds on, in which under sequential adaptive queries the simulated quantum state inevitably leaks into a bad-database subspace. This gives a lower bound on the resulting oracle deviation and clarifies why a full quantum indifferentiability proof needs additional ideas.
