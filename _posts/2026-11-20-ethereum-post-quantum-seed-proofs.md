---
title: "Correctable Enrollment and One-Transaction Seed Proofs for Ethereum's Post-Quantum Transition"
date: 2026-11-20 08:11:00 +0200
categories: [PQC]
tags: [blockchain, zero-knowledge-proofs, hash-based-signatures, migration]
link: https://arxiv.org/abs/2611.25663
byline: "Xin Jin et al. (arXiv:2611.25663, Nov 19 2026)"
description: "A proposed Ethereum migration lets owners enroll post-quantum keys cheaply before ECDSA retirement and recover frozen accounts afterward with a single-transaction zero-knowledge seed proof."
---

A quantum computer running Shor's algorithm could extract the private key of every Ethereum account whose public key has been published, and the authors note that accounts already exposed by their own transactions hold 54.6 percent of execution-layer ETH, so migration cannot wait for visible thefts. They design a scheme in which owners enroll post-quantum keys cheaply using their existing signatures before ECDSA is retired at a scheduled time, while a zero-knowledge proof of a wallet's BIP-39 seed can correct any enrollment until a later common deadline, and accounts nobody enrolled stay frozen but recoverable by seed proof indefinitely. Each proof binds the new key, a nonce, and a fee cap so neither a paying sponsor nor a reordering block builder can redirect or replay it, and validators switch to hash-based keys first at a finalized checkpoint. The authors implement the design in go-ethereum and a Lean consensus client, producing a three-layer recursive hash-based STARK seed proof of about 190 kilobytes that fits one transaction, verifies in 38 milliseconds, and takes a median of 111 seconds to generate on a laptop. In a ten-node simulation with mainnet-derived accounts, the 4.45 million accounts holding at least 0.1 ETH would migrate in 29.4 days if all enroll before ECDSA retirement, or 235 days if all instead recover afterward in batches of four.
