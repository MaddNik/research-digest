---
title: "Thresholding Post-Quantum Signatures"
date: 2026-08-28 08:15:00 +0200
categories: [PQC]
tags: [threshold-signatures, post-quantum-cryptography, survey, multi-party-computation]
link: https://arxiv.org/abs/2608.26792
byline: "Francesco De Sclavis et al. (arXiv:2608.26792, Aug 27 2026)"
description: "This survey classifies existing techniques for building T-out-of-N threshold signatures from post-quantum signature paradigms, motivated by a recent NIST call for threshold schemes."
---

Threshold signature schemes distribute the signing process among T parties out of N, but the authors note that current threshold applications are dominated by pre-quantum signatures, which are efficient but not secure against quantum adversaries. This paper investigates existing post-quantum signatures across a range of paradigms, including lattice problems, one-way hash functions, cryptographic group actions, isogenies, and multivariate systems, and proposes a classification, organized by paradigm, of the tools used to build T-out-of-N schemes from each type of digital signature. The survey also covers general approaches to thresholding based on fully homomorphic encryption, multi-party computation, or zero-knowledge proofs. The work is presented as motivated in part by a recent NIST call for threshold cryptography submissions.
