---
title: "Firebolt: Fast, Lightweight, Malicious Non-Interactive Vector-OLE"
date: 2026-10-23 08:23:00 +0200
categories: [Cryptography]
tags: [vector-ole, threshold-ecdsa, mpc]
link: https://eprint.iacr.org/2026/2549
byline: "Michael Adjedj et al. (IACR ePrint 2026/2549, Oct 20 2026, Asiacrypt 2026)"
description: "Firebolt is a maliciously-secure, non-interactive vector oblivious linear evaluation protocol built on Paillier-based VOLE that needs only 535 bytes of communication and about 5 milliseconds of computation per party per VOLE entry."
---

The authors introduce Firebolt, a new maliciously-secure vector oblivious linear evaluation (VOLE) protocol building on a recent semi-honest Paillier-based non-interactive VOLE construction. Firebolt is non-interactive, letting the sender adaptively reveal entries of the VOLE using a single message to the receiver, and achieves low communication of 535 bytes per VOLE entry and low computation of around 5 milliseconds per party on a single thread. The protocol is designed as a drop-in replacement for the less efficient VOLE constructions used in a variety of threshold schemes, which the authors demonstrate by devising a new concurrently-secure two-round two-party ECDSA protocol that significantly improves over the prior state of the art. Along the way, the paper introduces new strategies for proving shortness of plaintexts in Paillier ciphertexts or integer commitments, and a modular framework for building threshold ECDSA in a VOLE-hybrid model with concurrent security without requiring a typically less efficient UC-secure VOLE, contributions the authors note are of independent interest.
