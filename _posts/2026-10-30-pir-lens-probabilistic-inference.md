---
title: "PIR through the Lens of Probabilistic Inference"
date: 2026-10-30 08:25:00 +0200
categories: [Cryptography]
tags: [private-information-retrieval, probabilistic-inference, fine-grained-complexity, information-theoretic-security]
link: https://eprint.iacr.org/2026/2669
byline: "Dana Dachman-Soled (IACR ePrint 2026/2669, Oct 28 2026)"
description: "A new connection between information-theoretic private information retrieval and probabilistic inference shows that efficient exact inference algorithms directly speed up server computation for structured database classes while matching conditional lower bounds rule out general speedups."
---

Classic information-theoretic private information retrieval protocols achieve sublinear client computation and communication with a constant number of servers, but every server must still perform computation linear in the database size, and this paper asks for which classes of structured databases that server computation can be reduced while keeping the original communication and privacy guarantees. The main contribution is showing that the computation each server performs in both the classic Chor et al. protocol and the recursive Ambainis protocol can be viewed as computing a marginal probability of a product distribution, formalized through a new notion called inference complexity. Using this connection, the author obtains improved server computation for read-once arithmetic formulas, graphical models of bounded treewidth, functions with low communication complexity, and functions with sparse Fourier representations, all while preserving the original protocols' communication complexity, client computation, and server count. The paper complements these algorithms with a conditional lower bound showing that, assuming a randomized strong exponential time hypothesis for circuits, no uniform algorithm can achieve substantially sublinear server computation across all polynomial-size Boolean circuits.
