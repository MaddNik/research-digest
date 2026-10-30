---
title: "Shor's algorithm compiled on cat qubits: 22 593 qubits for RSA-2048 in 3.14 days"
date: 2026-10-30 08:09:00 +0200
categories: [PQC]
tags: [shors-algorithm, cat-qubits, resource-estimation, quantum-cryptanalysis]
link: https://eprint.iacr.org/2026/2665
byline: "Axel Pappalardo et al. (IACR ePrint 2026/2665, Oct 28 2026)"
description: "An end-to-end resource estimate compiles Shor's algorithm down to physical cat-qubit operations and chip layouts, finding that factoring RSA-2048 needs about 23,000 cat qubits and 3.14 days under stated noise assumptions."
---

This paper presents an end-to-end resource estimation of Shor's algorithm on superconducting cat qubits, going from the algorithm's mathematical description all the way to allocation and scheduling of physical qubits on a chip layout. The authors compile the dominant subroutines for RSA, ECDLP, and FFDLP variants of Shor's algorithm down to physical-qubit operations on two cat-qubit architectures, one based on repetition cat codes and one on LDPC cat codes, introducing new gate designs along the way. Assuming a 1 microsecond error-correction cycle, a 10 microsecond reaction time, and circuit-level phase-flip noise with no bit-flips, the authors estimate that factoring RSA-2048 requires about 23,000 cat qubits and 3.14 days. Reusing the compiled operations, they estimate that solving ECDLP on secp256k1 requires at most 30,000 cat qubits and 1 hour, and that an FFDLP-512 benchmark requires about 6,700 cat qubits and 21 minutes, with a space-time tradeoff allowing RSA-2048 in 1.25 hours using about 611,000 cat qubits. Relaxing the no-bit-flip assumption to a bit-flip time of about one hour, by adding a distance-3 bit-flip error-correcting concatenation layer, raises the RSA-2048 cost to about 45,000 cat qubits.
