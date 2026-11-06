---
title: "Short Collisions Separate Sponge from Merkle-Damgård"
date: 2026-11-06 08:22:00 +0200
categories: [Cryptography]
tags: [hash-functions, sponge-construction, merkle-damgard, preprocessing-attacks]
link: https://eprint.iacr.org/2026/2695
byline: "Ashrujit Ghoshal (IACR ePrint 2026/2695, Oct 30 2026)"
description: "A new separation shows that three-block messages suffice for a constant-probability preprocessing attack on sponge-based hashing, while Merkle-Damgård resists any comparably short attack."
---

This paper studies short collisions in salted Merkle-Damgård and Sponge hash constructions under the query-bounded preprocessing model, where an adversary makes some queries before a random salt is revealed and more queries afterward, then must output two colliding messages of bounded length. The main result is a separation between the two constructions: under matched salt, block, and output sizes and comparable query budgets, there is an attack that finds a Sponge collision with constant probability using only three-block messages, while every Merkle-Damgård adversary limited to a similarly short message length succeeds with vanishing probability. The Merkle-Damgård upper bound uses a graph argument distinguishing collisions already present in the preprocessing transcript from those reachable by a short computation after the salt is sampled, extending prior analysis beyond the one- and two-block case. The Sponge-side attack uses inverse permutation queries to make one precomputed collision useful across many different capacities, and the authors show that allowing longer messages gives no further asymptotic advantage, since the optimal Sponge preprocessing attack is already achieved with at most three blocks.
