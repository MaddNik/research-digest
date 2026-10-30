---
title: "Beyond the Event Horizon of Keccak, Extending the Observation from 2011 and applications"
date: 2026-10-30 08:24:00 +0200
categories: [Cryptography]
tags: [keccak, sha-3, second-preimage, multicollisions]
link: https://eprint.iacr.org/2026/2671
byline: "Danilo Gligoroski (IACR ePrint 2026/2671, Oct 28 2026)"
description: "New theorems generalize a 2011 observation about Keccak capacity cycles into cheap collisions, a search-independent multicollision construction, and new unkeyed protocols with tunable, feasible hardness parameters, verified with full-round examples and Lean 4 proofs."
---

In 2011, the author observed that a single path in the Keccak sponge from a state with all-zero capacity bits back to such a state yields an infinite family of second preimages for any message of at least one full rate block, at a cost of about 2 to the c/2, which is infeasible for SHA3-256. This paper proves three new theorems extending that observation: a two-block meet-in-the-middle loop from any capacity value back to itself gives the same unlimited second-preimage family at similar cost, this extends to k-block loops and cycles of the capacity map, and a bridge-amplified multicollision construction yields equal-length Joux-style 2 to the k multicollisions from just one inner collision and one connector, which the author believes is the first such construction for generic sponges with search cost independent of k. The theorems are proven and the stated algebraic results machine-checked in Lean 4, with verified full-round examples given on reduced Keccak permutations. The second part of the paper proposes novel protocols exploiting the asymmetry between minting and forging these Keccak bridges, including proof-of-work with hardness-adaptive capacity, dual-capacity commitments, and a self-enforcing bounty market for reduced-round security, though the author notes these applications are design proposals whose end-to-end security remains open.
