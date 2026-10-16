---
title: "A Black-Box Compiler from Static to Dynamic SNARKs"
date: 2026-10-16 08:28:00 +0200
categories: [Cryptography]
tags: [snarks, dynamic-proofs, vector-commitments, post-quantum-security]
link: https://eprint.iacr.org/2026/2445
byline: "Anubhav Baweja and Charalampos Papamanthou (IACR ePrint 2026/2445, Oct 11 2026)"
description: "A black-box compiler turns any static SNARK and vector commitment scheme into a dynamic SNARK that updates proofs in time proportional to how much the witness changed, achieving large prover speedups over a static baseline."
---

Succinct non-interactive arguments of knowledge let a prover convince a verifier of a witness with a short proof and cheap verification, and recent work has also pushed for prover efficiency through dynamic SNARKs, which let a prover update a proof efficiently when the witness changes, for example reproving a database query after a single entry is updated. Existing dynamic SNARK constructions from Eurocrypt 2026 have limitations such as lacking post-quantum security, depending on a trusted third-party setup, or having poor concrete efficiency. This work presents a compiler that builds a dynamic SNARK for Plonkish constraints, which capture arbitrary NP computations, using only a static SNARK for NP and a vector commitment scheme as black boxes. Instantiated with a state-of-the-art hash-based SNARK and Merkle trees, the resulting dynamic SNARK is post-quantum secure in the quantum random oracle model, has a transparent setup, and achieves initial prover time proportional to the circuit size with update prover time proportional to the Hamming distance between old and new witnesses times a logarithmic-squared factor. The authors' Ligerito-based implementation achieves cumulative prover speedups of 147 times and 11.7 times over a static HyperPlonk baseline for 10,000 successive one-gate updates and 1,000 successive 128-gate updates respectively, on a circuit with about 8 million gates, including the full dynamic initialization cost.
