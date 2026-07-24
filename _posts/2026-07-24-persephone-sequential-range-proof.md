---
title: "PERSEPHONE: Zero-Knowledge Multiplicative Non-Negative Proof for Sequential Private Range Verification"
date: 2026-07-24 08:18:00 +0200
categories: [Cryptography]
tags: [range-proof, private-payments, sequential-verification, zk-proofs]
link: https://eprint.iacr.org/2026/1477
byline: "Ivan Tjuawinata et al. (IACR ePrint 2026/1477, Jul 20 2026)"
description: "A zero-knowledge protocol that proves a sequence of values stays within sequentially linked private bounds in one pass instead of checking each range independently."
---

The paper targets financial transaction systems where a payment amount must be checked against a wallet balance that itself depends on prior private values in a chain. Instead of running a separate zero-knowledge range proof for each linked value, PERSEPHONE proves a chain of multiplicative non-negative relations together. The authors report about a 3 times performance improvement over prior sequential range verification approaches. They show the scheme keeps transaction processing under a 400 millisecond threshold in realistic payment scenarios. The work targets privacy preserving payment and wallet balance verification use cases.
