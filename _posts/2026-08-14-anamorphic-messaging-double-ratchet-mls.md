---
title: "Anamorphic Messaging: Analyzing the Double Ratchet, Triple Ratchet, PQ3, and MLS"
date: 2026-08-14 08:21:00 +0200
categories: [Cryptography]
tags: [anamorphic-encryption, secure-messaging, ratchet-protocols]
link: https://eprint.iacr.org/2026/1638
byline: "Hien Chu et al. (IACR ePrint 2026/1638, Aug 8 2026)"
description: "An analysis of how much covert, anamorphic communication capacity can be hidden inside real-world secure messaging protocols without breaking their forward secrecy guarantees."
---

Motivated by scenarios where authorities compel disclosure of encryption keys, the authors study whether users can embed hidden messages inside standard secure-messaging protocols that remain undetectable even to an adversary who later learns the hidden state. They formalize a model based on continuously updated double states that preserves forward security for the covert channel. They then apply this model to four real protocols: Signal's Double Ratchet and Triple Ratchet, Apple's PQ3, and the two-party variant of the Messaging Layer Security (MLS) standard. Despite the protocols' complexity, they find the available anamorphic embedding capacity is quite limited and protocol-dependent: 16 bits per epoch for Double Ratchet, 176 bits for Triple Ratchet, 256 bits for PQ3, and 688 bits for MLS.
