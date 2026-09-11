---
title: "When Module Lattice Leaks: Horizontal Fusion Attacks on ML-DSA Implementation"
date: 2026-09-11 08:11:00 +0200
categories: [PQC]
tags: [ml-dsa, side-channel, lattice-cryptography, key-recovery]
link: https://eprint.iacr.org/2026/1904
byline: "Yuhan Zhao et al. (IACR ePrint 2026/1904, Sep 7 2026)"
description: "A new horizontal fusion attack recovers ML-DSA secret keys from as few as 4 signature traces on the unprotected implementation and up to 90 traces on a first-order masked implementation."
---

The standardization of ML-DSA has shifted attention to its practical implementation security, where non-profiling attacks were widely assumed to need large numbers of traces. The authors introduce horizontal fusion attacks that make non-profiling, few-trace key recovery practical against ML-DSA, including masked implementations. They expose a structural vulnerability in ML-DSA's matrix-vector multiplication, where row-wise reuse of the ephemeral secret vector produces multiple leakage instances of the same secret-dependent value within a single signature, and propose a variance-based weighted fusion strategy along with a fast INTT-based algebraic sieve to exploit it. The attack achieves full key recovery using only 4 traces against ML-DSA-87, the highest security parameter set, under non-profiling correlation analysis, and recovers the secret key from no more than 90 traces against a state-of-the-art first-order masked implementation, setting a new record in trace complexity for both settings.
