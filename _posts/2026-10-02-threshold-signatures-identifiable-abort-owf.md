---
title: "Threshold Signatures with Identifiable Abort from One-way Functions"
date: 2026-10-02 08:26:00 +0200
categories: [Cryptography]
tags: [threshold-signatures, one-time-signatures, merkle-trees, universal-composability]
link: https://eprint.iacr.org/2026/2238
byline: "Mojtaba Fadavi, David Jao, and Samuel Jaques (IACR ePrint 2026/2238, Sep 27 2026)"
description: "A threshold one-time signature scheme built from Lamport signatures and Shamir sharing extends to multi-message signing via multi-layer Merkle trees, with identifiable abort guaranteed through a bulletin-board consensus step."
---

A (T,N)-threshold signature scheme distributes a signing key among N participants so that any T of them can jointly produce a valid signature while fewer than T cannot. The authors first build a threshold one-time signature scheme with identifiable abort from a variant of the Lamport one-time signature combined with Shamir secret sharing, letting authorized participants jointly reconstruct signatures from partial signatures, then extend it to multiple messages using multi-layer Merkle trees. Because one-time signatures require participants to agree on both the message and the one-time key index to avoid unsafe key reuse, the scheme uses a bulletin-board mechanism to reach that consensus, requiring only one message from the bulletin board to each signer and one response from each signer, plus whatever extra communication the board needs to agree, giving a four-round signing protocol under a simple majority-vote board. Subject to this coordination constraint, the construction inherits Universal Composability unforgeability with identifiable abort, non-UC robustness, and a bulletin-board mechanism that is itself UC-secure given an honest super-majority and robust when the central aggregator is honest.
