---
title: "Censorship-Resistant Sealed-Bid Auctions on Blockchains"
date: 2026-06-19 08:11:00 +0200
categories: [Cryptography]
tags: [blockchain, zero-knowledge]
link: https://arxiv.org/abs/2606.14939
byline: "Orestis Alpos et al. (arXiv:2606.14939, Jun 12 2026)"
description: "A sealed-bid auction protocol for blockchains that hides bids until reveal and resists proposer-level censorship using zero-knowledge proofs."
---

This paper addresses fairness problems in blockchain auctions, where a single consensus
proposer per block can manipulate which bids are visible or included. The protocol
establishes four properties: hiding bid details until reveal, counting timely honest bids
while rejecting late adversarial ones, preventing costless bid withdrawal, and charging
on-chain fees only to winners. The design combines a timestamping oracle using 2 times
f_ts plus 1 validators with a censorship-resistant inclusion mechanism. It relies on two
zero-knowledge proofs: an eligibility proof of deposit membership and an auction proof
binding bids to a specific auction. A Rust and arkworks implementation generates auction
proofs in about 13 milliseconds and verifies in under 1 millisecond, scaling to Merkle
trees of 2 to the 32 bidders.
