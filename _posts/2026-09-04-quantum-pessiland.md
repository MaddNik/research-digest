---
title: "Quantum Pessiland"
date: 2026-09-04 08:25:00 +0200
categories: [Cryptography]
tags: [quantum-cryptography, one-way-functions, complexity-theory, efi-pairs]
link: https://eprint.iacr.org/2026/1834
byline: "Boyang Chen et al. (IACR ePrint 2026/1834, Aug 30 2026)"
description: "The authors construct a quantum oracle and a classical oracle relative to which average-case hardness holds but even quantum cryptographic primitives such as EFI pairs and one-way puzzles do not exist, establishing a quantum analogue of Impagliazzo's Pessiland."
---

Pessiland, in Impagliazzo's classification, is a world where NP is hard on average yet one-way functions do not exist, leaving almost no classical cryptography since nearly every classical primitive implies one-way functions. Because quantum cryptography can exist even without one-way functions, this paper asks whether there is a quantum analogue of Pessiland where NP is hard on average but even quantum cryptography fails to exist, and answers yes: the authors show there is a quantum oracle relative to which UP intersect coUP is hard on average against quantum polynomial-time algorithms with quantum advice, yet auxiliary-input EFI pairs do not exist. They also exhibit a classical oracle with the analogous average-case hardness of UP intersect coUP under which classically-secure auxiliary-input one-way puzzles do not exist, and since almost all quantum cryptographic primitives imply EFI pairs or one-way puzzles, these results mean there is almost no quantum cryptography relative to either oracle. Relative to the classical oracle the authors further show SampBQP equals SampBPP, so there is no sampling-based quantum advantage in Quantum Pessiland, and because their average-case hardness result implies a complexity-theoretic separation, it also gives a partial negative answer to an open problem about constructing one-way puzzles from that separation alone.
