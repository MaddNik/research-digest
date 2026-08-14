---
title: "AES-Based Grinding for MPC-in-the-Head Signatures"
date: 2026-08-14 08:25:00 +0200
categories: [Cryptography]
tags: [mpc-in-the-head, signature-schemes, aes]
link: https://eprint.iacr.org/2026/1625
byline: "Matthieu Rivain (IACR ePrint 2026/1625, Aug 6 2026)"
description: "An AES-based proof-of-work grinding technique, rather than a hash-based one, is formalized to shorten MPC-in-the-head signature schemes such as FAEST, MQOM, and SDitH."
---

MPC-in-the-head signature schemes can be shortened by requiring the prover to find a challenge meeting a bit-constraint via computational grinding, which raises attacker cost from roughly one over epsilon to two to the power w over epsilon hash evaluations, where epsilon is the soundness error and w is the bit constraint. This paper formalizes such grinding schemes with protocol-agnostic security definitions and proposes an AES-based construction using two cipher calls per grinding iteration, replacing the usual reliance on Keccak. In the ideal cipher and random oracle models, the author proves that an adversary making Q_E cipher queries succeeds with probability bounded by four-thirds times epsilon times Q_E divided by two to the power w, and shows the construction generalizes to more cipher calls to push the constant factor toward one. The technique targets concrete efficiency gains for the NIST post-quantum signature candidates FAEST, MQOM, and SDitH.
