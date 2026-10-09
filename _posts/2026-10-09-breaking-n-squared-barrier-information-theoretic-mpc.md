---
title: "Breaking the n^2 Barrier: Information-Theoretic MPC with Sub-Quadratic Communication"
date: 2026-10-09 08:29:00 +0200
categories: [Cryptography]
tags: [secure-multiparty-computation, information-theoretic-security, communication-complexity]
link: https://eprint.iacr.org/2026/2311
byline: "Alexander Bienstock, Yuval Efron, and Kevin Yeo (IACR ePrint 2026/2311, Oct 2 2026)"
description: "The first information-theoretic MPC protocol with sub-quadratic-in-n communication for a wide range of small circuits removes the additive n-squared cost that has dominated prior honest-majority protocols."
---

Secure multiparty computation across n parties aims to let them jointly compute a function so that an adversary controlling t corrupted parties learns nothing beyond the output, and while recent information-theoretic honest-majority protocols have driven communication for large circuits down close to the circuit size, all such protocols have still required an additive n-squared communication cost independent of circuit size, which dominates for small circuits. For corruption threshold t less than roughly n over 2, the authors present an information-theoretic MPC protocol secure against adaptive and malicious adversaries with sub-quadratic communication for a wide range of circuits, including those with a sublinear number of input parties and circuit size and depth bounded in terms of n, for example circuits of size o(n to the 3/4) with o(n to the 3/4) input parties. This is, to their knowledge, the first information-theoretic MPC protocol with communication below n-squared for such circuit classes, achieved via new techniques for randomness generation, player virtualization, and output reconstruction that exploit the sublinear number of input parties. The authors also prove a matching impossibility result, showing that sub-quadratic communication MPC is impossible against adversaries with stronger-than-standard adaptive rushing capabilities, even for constant-size circuits.
