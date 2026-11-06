---
title: "HqcLethe: Streaming HQC Encapsulation for Tiny Stateless Servers"
date: 2026-11-06 08:09:00 +0200
categories: [PQC]
tags: [hqc, kem, stateless-protocols, formal-verification]
link: https://eprint.iacr.org/2026/2767
byline: "Wind Wong and Klaus v. Gleissenthall (IACR ePrint 2026/2767, Nov 4 2026)"
description: "HqcLethe streams HQC key encapsulation one packet at a time so stateless servers can resist both memory-exhaustion attacks and the loss of code-based cryptographic diversity."
---

Stateless post-quantum key exchanges such as post-quantum WireGuard have combined a lattice KEM with the code-based Classic McEliece scheme for cryptographic diversity, but recent attacks have led Germany's BSI to advise against McEliece, leaving these protocols reliant on lattice assumptions alone. HQC, the code-based KEM selected by NIST, could restore that diversity, but its keys do not fit in a single network packet, so a stateless server would otherwise need to buffer multi-packet handshakes and risk memory-exhaustion attacks. This paper presents HqcLethe, a stateless key exchange that streams an HQC encapsulation in packet-sized pieces by using the Chinese remainder theorem to split the underlying cyclic polynomial multiplication into independent, masked remainders, one per packet. The authors formally verify that the scheme reveals no more than an ordinary HQC ciphertext, using Rocq with SSProve for the masking proof and ProVerif for session secrecy, server authentication, and forward secrecy. Client puzzles bound CPU exhaustion, while the packet-streaming design removes the memory-exhaustion attack surface entirely.
