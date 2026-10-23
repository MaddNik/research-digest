---
title: "Circular Dragon: Optimal Adaptively Secure Distributed Randomness/Key Generation and Parallel Broadcast"
date: 2026-10-23 08:25:00 +0200
categories: [Cryptography]
tags: [distributed-key-generation, byzantine-agreement, adaptive-security]
link: https://eprint.iacr.org/2026/2534
byline: "Hanwen Feng et al. (IACR ePrint 2026/2534, Oct 20 2026)"
description: "A new strongly adaptive common coin protocol achieves optimal resilience with near-quadratic communication and logarithmic rounds in synchronous networks, and yields the first strongly adaptive parallel broadcast with sub-cubic communication and sub-linear rounds without a trusted dealer."
---

The authors present the first strongly adaptive common coin protocol, under PKI setup in the random oracle and algebraic group models with no trusted dealer, that achieves optimal resilience t less than n/2 in synchronous networks together with near-optimal asymptotics: near-quadratic communication of O(kappa lambda n squared log n) and logarithmic rounds of O(kappa log n), where lambda and kappa are the computational and statistical security parameters, with no reliance on memory erasure. The core of the construction is a special-purpose distributed key generation protocol producing a secret in an elliptic-curve group, which the authors call Circular Dragon, extending the prior Dragon method for sub-cubic-communication distributed key generation by further reducing round complexity from linear to logarithmic. The common coin immediately yields the first strongly adaptive, optimally resilient Byzantine Agreement with sub-cubic communication and sub-linear rounds without a trusted dealer, and the authors give two further applications: a strongly adaptive parallel broadcast protocol with near-quadratic communication and logarithmic rounds, improving on existing sub-cubic solutions that require at least linear rounds, and a strongly adaptive general-purpose distributed key generation protocol for field-element secrets that improves the round complexity of a prior construction from O(n) to O(kappa log n).
