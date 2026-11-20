---
title: "Concrete Quantum Circuit Implementations and Resource Estimates for the Quantum 3 and 4-Sieves"
date: 2026-11-20 08:10:00 +0200
categories: [PQC]
tags: [lattice-cryptanalysis, shortest-vector-problem, quantum-circuits, resource-estimation]
link: https://eprint.iacr.org/2026/2895
byline: "MohamadAli Khajeian (IACR ePrint 2026/2895, Nov 14 2026)"
description: "The first concrete reversible quantum circuits for the quantum 3-sieve and 4-sieve algorithms for the shortest vector problem come with validated resource estimates at cryptographic dimensions."
---

Chailloux and Loyer introduced quantum 3-sieve and 4-sieve algorithms for the shortest vector problem in 2023 with asymptotic analyses, but no concrete circuit implementation had been worked out. This paper presents the first complete reversible circuits for both algorithms, designing inner-product predicates with signed symmetric squaring across three circuit architectures optimized for low qubit count, balance, or low depth. The circuits are validated with exact sparse state-vector simulations that match an independent mathematical model to a precision of 10 to the minus 13. The author shows that the original amplitude-amplification oracle fails once the inner Grover searches become approximate, and corrects it so the full configuration can be tested. Applying the same arithmetic techniques to the previously published two-sieve oracle reduces its T-count by a factor of 9.4 to 14 and its T-depth by more than three orders of magnitude, and the paper provides exact per-call logical resource estimates for the core predicates at cryptographic dimensions relevant to lattice-based cryptography.
