---
title: "Robust ECDSA Threshold Signing at Scale"
date: 2026-10-16 08:24:00 +0200
categories: [Cryptography]
tags: [threshold-ecdsa, secret-sharing, zero-knowledge-proofs, blockchain-bridging]
link: https://eprint.iacr.org/2026/2493
byline: "Carsten Baum and Anders Dalskov (IACR ePrint 2026/2493, Oct 15 2026)"
description: "A scalable and robust threshold ECDSA signing protocol for up to a third dishonest signers batches its preprocessing and combines established secret-sharing and zero-knowledge techniques to handle large numbers of parties."
---

This work presents an efficient, scalable, and robust threshold ECDSA signing protocol for the setting where the number of corrupt parties t is at most one third of the total number of signers n, making it suitable for applications such as bridging consensus from one blockchain to another. The construction allows batch-computing pre-processing material ahead of time for efficient online signing, rather than redoing expensive setup work for every signature. While based on established ideas for verifiable secret sharing, the protocol is optimized to scale efficiently in both computation and communication as the number of signers grows, combining efficient batching techniques for sharing, randomness extraction, and share opening from prior distributed computing literature with recent advances in efficient zero-knowledge proofs. The authors implement and experimentally evaluate the protocol, showing it remains practical for a large number of parties.
