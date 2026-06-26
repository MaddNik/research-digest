---
title: "GumSwap: Griefing-Free Universal Multi-Party Atomic Swaps"
date: 2026-06-17 08:30:00 +0200
categories: [Cryptography]
tags: [blockchain, cryptography]
link: https://eprint.iacr.org/2026/1253
byline: "Dongkun Hou et al. (IACR ePrint 2026/1253, Jun 14 2026)"
description: "A universal multi-party cross-chain swap protocol that defends against griefing by compensating compliant parties whose assets are locked but not redeemed."
---

Universal multi-party swaps enable secure cross-chain cryptocurrency exchanges
across multiple blockchains while requiring only signature verification from the
underlying chains, but existing protocols remain vulnerable to griefing attacks
where a deviating party aborts to lock a compliant party's assets for a long period.
The authors observe that directly lifting existing griefing-free solutions to the
universal setting faces three challenges: a timeout race attack from the absence of
an upper bound on transaction validity, a premium escape attack from multiple
simultaneously valid refund transactions, and a topological limitation restricting
support to a special class of strongly connected digraphs. GumSwap guarantees that a
compliant party receives a premium if its asset is locked but not redeemed. To
address the first two attacks it imposes minimum timeout intervals for principal and
premium timeouts and introduces an asset migration mechanism ensuring at most one
refund transaction is valid in any interval. Given the topological limitations, it
further designs a novel premium distribution mechanism.
