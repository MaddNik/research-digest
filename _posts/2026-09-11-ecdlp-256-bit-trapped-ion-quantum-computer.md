---
title: "Computing 256-bit elliptic curve discrete logarithms in 26 days on a fault-tolerant trapped-ion quantum computer with 20,000 qubits"
date: 2026-09-11 08:08:00 +0200
categories: [PQC]
tags: [ecdlp, shors-algorithm, trapped-ion, quantum-threat]
link: https://eprint.iacr.org/2026/1916
byline: "Thomas Haner et al. (IACR ePrint 2026/1916, Sep 8 2026)"
description: "IonQ researchers estimate that a fault-tolerant trapped-ion quantum computer using their Walking Cat Architecture could solve the 256-bit ECDLP on secp256k1 in about 26 days using under 20,000 physical qubits."
---

Building on their previously proposed Walking Cat Architecture for trapped-ion quantum computing, the authors present optimized circuits for solving the 256-bit elliptic curve discrete logarithm problem (ECDLP) on secp256k1, the curve used by Bitcoin and other blockchain systems, via Shor's algorithm. Their logical circuit uses about 1450 qubits and 40 million Toffoli gates, with a fast CCZ magic-state factory and depth-one CCZ state injection that cut CCZ gate execution time by a factor of 31. Additional optimizations, including a more efficient loss correction protocol and recycling of ancilla qubits, reduce the physical qubit overhead. Combining all improvements, the authors estimate that their architecture could solve the ECDLP on secp256k1 in about 25.7 days using 19,397 physical qubits with an estimated success probability of 63 percent, a concrete data point for assessing the timeline of the quantum threat to elliptic curve cryptography.
