---
title: "Multiparty Computation with Minimal Overhead without Circuit Transformation"
date: 2026-11-20 08:19:00 +0200
categories: [Cryptography]
tags: [secure-multiparty-computation, honest-majority, share-packing]
link: https://eprint.iacr.org/2026/2891
byline: "Aditya Hegde, Phuoc Van Long Pham, Mingyuan Wang (IACR ePrint 2026/2891, Nov 13 2026, CRYPTO 2026)"
description: "A new honest-majority MPC protocol achieves near-ideal overhead for general circuits over much smaller prime fields than prior share-unpacking protocols, without any circuit transformation step."
---

A central goal in secure multiparty computation is to minimize the gap between the total work performed by all parties and the cost of plain, insecure circuit evaluation. In the honest-majority setting, an ideal overhead that is essentially constant is known to be achievable, but all prior protocols over prime fields reaching that goal for general circuits relied on share-packing techniques that require expensive circuit transformation steps to impose repetitive structure on the circuit. The only exception, a share-unpacking protocol by Garg, Jain, Mukherjee, and Wang at CRYPTO 2024, avoided circuit transformation but only works when the underlying field size is exponential in the square of the number of parties. The authors present the first MPC protocol with essentially constant overhead for any prime field, or more generally any integer ring, whose size only needs to be exponential in the number of parties rather than in its square. Technically, they extend the share-unpacking approach of Garg et al. with a new approach to linear randomness extraction over integers, which they note may be of independent interest.
