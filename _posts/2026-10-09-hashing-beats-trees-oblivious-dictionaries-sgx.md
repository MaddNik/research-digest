---
title: "Hashing Beats Trees: Practical Oblivious Dictionaries in SGX"
date: 2026-10-09 08:38:00 +0200
categories: [Hardware Security]
tags: [intel-sgx, oblivious-ram, oblivious-hash-tables]
link: https://eprint.iacr.org/2026/2397
byline: "Erik-Oliver Blass and Travis Mayberry (IACR ePrint 2026/2397, Oct 7 2026)"
description: "Replacing oblivious AVL trees with oblivious probabilistic hash tables over Path ORAM speeds up oblivious dictionary lookups in Intel SGX enclaves by up to 20 times."
---

Oblivious RAM hides both the contents of outsourced data and the access pattern to it, but it offers only a restrictive array-based interface, and building an efficient oblivious dictionary on top of it has been a major obstacle, since the state-of-the-art layers an oblivious AVL tree over ORAM that forces every operation to traverse a full root-to-leaf path at a cost of Theta(log n) ORAM accesses. The authors show this trade-off is suboptimal, particularly inside a trusted execution environment like SGX, where a small amount of client memory can reduce the position map recursion depth to three levels or less, making probabilistic hash tables, with their small constant number of accesses, preferable to path traversal. They implement and analyze oblivious probabilistic hash tables over Path ORAM using several strategies, including chaining, power-of-two-choices, stash-less cuckoo, and de-amortized cuckoo hashing, and because running these inside a secure enclave requires strict concrete maximum cost limits that prior literature does not provide, they derive concrete padding parameters bounding the hash table rebuild probability to at most 2 to the negative 40 via large-scale simulation. In an SGX deployment, their constructions outperform oblivious trees by up to 20 times for lookups and 12 times for inserts.
