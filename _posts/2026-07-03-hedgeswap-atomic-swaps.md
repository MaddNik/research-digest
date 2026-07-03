---
title: "HedgeSwap: Universal Hedged Atomic Swaps Against Griefing Attacks"
date: 2026-07-03 08:24:00 +0200
categories: [Cryptography]
tags: [atomic-swaps, adaptor-signatures, cross-chain, griefing-attacks]
link: https://eprint.iacr.org/2026/1252
byline: "Hou et al. (IACR ePrint 2026/1252, Sat 27 Jun 2026)"
description: "HedgeSwap is a cross-chain atomic swap protocol that compensates honest parties with a premium when a deviating counterparty aborts, defeating griefing attacks in prior universal swap designs."
---

Universal atomic swaps replace hashed timelock contracts with adaptor signatures and verifiable timed discrete logarithms, enabling cross-chain cryptocurrency exchanges that need only basic signature verification from the underlying blockchains, but they remain vulnerable to griefing attacks in which a deviating party aborts the swap to lock a compliant party's assets for a long time. The authors show that a naive attempt to lift contract-based griefing defenses into the universal setting runs into two new problems: timeout race attacks and a timeout overlap dilemma caused by multiple overlapping refund periods. HedgeSwap solves both problems by eliminating the premium timeout entirely and instead using a hard relation to refund the premium, compensating the compliant party with a premium if its asset is locked but not redeemed. For high-value swaps where the parties' acceptable premium ranges do not overlap, the paper also proposes a round-based variant with a premium migration mechanism that iteratively raises the premium until agreement is reached.
