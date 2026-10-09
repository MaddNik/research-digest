---
title: "Improved Local Leakage Resilience of Shamir Secret Sharing and Worst-Case Optimal Polynomial Intersection"
date: 2026-10-09 08:24:00 +0200
categories: [Cryptography]
tags: [secret-sharing, leakage-resilience, quantum-algorithms]
link: https://arxiv.org/abs/2610.12357
byline: "Yihang Sun and Mary Wootters (arXiv:2610.12357, Oct 8 2026)"
description: "New results break the long-standing one-half barrier for local leakage resilience of Shamir secret sharing and give an improved quantum algorithm for the related optimal polynomial intersection problem."
---

The paper studies two related problems for polynomials of degree less than k over a prime-order finite field: local leakage resilience (LLR) of Shamir secret sharing, which asks how much an adversary can learn about a secret from a few leaked bits per share, and worst-case optimal polynomial intersection (OPI), which asks for a low-degree polynomial agreeing with as many of several input lists as possible. Leveraging a recently discovered connection between the two problems, the authors show that for a constant rate R equal to k over n at least one-half minus a small constant, Shamir secret sharing is one-bit locally leakage resilient, meaning only a negligible amount about the secret can be learned; this is the first result to break the long-standing "one-half barrier" for LLR, improving on a previous bound requiring R at least 0.668. For OPI, they give a quantum algorithm that finds a polynomial agreeing with close to the semicircle-law fraction of input lists in expectation, improving prior algorithmic and existential results, and they adapt a known hardness result to OPI directly, giving an unconditional separation between quantum and classical hardness of OPI relative to a membership oracle over large fields.
