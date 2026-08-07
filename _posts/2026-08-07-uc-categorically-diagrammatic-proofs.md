---
title: "UC, Categorically: Rigorous Diagrammatic Proofs"
date: 2026-08-07 08:16:00 +0200
categories: [Cryptography]
tags: [universal-composability, formal-methods, category-theory]
link: https://eprint.iacr.org/2026/1605
byline: "Pooya Farshim et al. (IACR ePrint 2026/1605, Aug 4 2026)"
description: "A category-theoretic reformulation of Canetti's Universal Composability framework that allows composition proofs to be verified graphically via string diagrams while remaining formally rigorous."
---

The paper applies category theory, specifically string diagrams, to give a graphical yet rigorous treatment of the Universal Composability (UC) framework for systems with a static number of parties and sessions. The composition theorem can be checked visually through a short sequence of diagrams while still being translatable into equations suitable for formal verification. The categorical framing also generalizes UC beyond interactive Turing machines to other computation models, such as quantum computation or domain-specific languages, and allows the adversary to be modeled as a computational network rather than a single machine, while the authors prove this variant is equivalent in expressiveness to standard UC. Along the way they identify and correct minor technical oversights in the standard formulation of simple UC.
