---
title: "Quantum Discrete Logarithms on Elliptic Curves with 5n/2+o(n) Logical Qubits and O(n squared) Toffoli Gates"
date: 2026-09-18 08:13:00 +0200
categories: [PQC]
tags: [ecdlp, quantum-algorithms, quantum-cryptanalysis, elliptic-curves]
link: https://eprint.iacr.org/2026/2014
byline: "Sunghyeon Jo and Gye Jin Lee (IACR ePrint 2026/2014, Sep 14 2026)"
description: "A new quantum algorithm for the elliptic curve discrete logarithm problem needs only 5n/2 logical qubits and near-quadratic Toffoli gate counts, improving on the prior best space-efficient construction."
---

The authors give a quantum algorithm for the elliptic curve discrete logarithm problem over an n-bit prime field that uses 5n/2 + o(n) logical qubits and O(n squared) (up to log factors) Toffoli gates, improving on Luo et al.'s exact space-efficient affine construction, which used 3n + O(log n) qubits and O(n^3 / log n) Toffoli gates. The new algorithm lowers the leading qubit term from 3n to 5n/2 and reduces the Toffoli gate count to near-quadratic. A key building block is an exact in-place modular inverter using 3n/2 + o(n) logical qubits and O(n) (up to log factors) Toffoli gates, which exploits the invariant Rt + rT = p for consecutive Euclidean remainders and coefficient magnitudes to store only three of the four running values, reconstructing the fourth on demand and erasing temporary data after each update via measurement-based uncomputation in sublinear workspace. The authors then use Hua's identity to reduce the variable-square multiplications needed for affine point addition to inversions, yielding exact controlled point addition within the stated 5n/2 + o(n) qubit and near-linear Toffoli gate bounds. Because breaking elliptic curve cryptography with a quantum computer is the central motivation for post-quantum migration, tighter resource estimates like this one directly inform how urgently classical elliptic curve schemes need to be replaced.
