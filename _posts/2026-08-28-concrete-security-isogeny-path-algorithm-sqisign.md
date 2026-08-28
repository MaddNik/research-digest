---
title: "Concrete Security Assessment of Isogeny-based Cryptography with the new Isogeny-Path algorithm"
date: 2026-08-28 08:10:00 +0200
categories: [PQC]
tags: [isogeny-based-cryptography, sqisign, concrete-security, quantum-cryptanalysis]
link: https://eprint.iacr.org/2026/1821
byline: "Maher Mamah (IACR ePrint 2026/1821, Aug 27 2026)"
description: "A concrete cost analysis finds that Wesolowski's recent asymptotic improvement to the isogeny-path algorithm does not translate into a comparable reduction in the practical security of SQIsign and related schemes."
---

Wesolowski recently proposed a heuristic algorithm solving the supersingular isogeny-path problem in time and memory scaling as the cube root of the field characteristic p, an asymptotic improvement over the prior square-root complexity, but its concrete impact on schemes like SQIsign was unclear due to hidden superpolynomial overhead and exponential memory requirements. This paper assesses the concrete cost of that attack, studies its time-memory tradeoffs, and investigates van Oorschot-Wiener optimizations, finding that over practical memory ranges neither the optimized full-list attack nor its variants outperform the previous state-of-the-art low-memory algorithm for computing supersingular endomorphism rings. The author further studies quantum claw-finding improvements, showing that Grover search can remove the large memory requirement but offers little running-time improvement, while Tani's algorithm gives a stronger gate-memory tradeoff at the cost of substantial coherent quantum memory. Overall, the results indicate that the asymptotic improvement does not directly translate into a comparable reduction in concrete security for isogeny-based cryptography.
