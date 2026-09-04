---
title: "Universally Composable Hybrid PAKE Secure Against Harvest-Now-Decrypt-Later Attacks"
date: 2026-09-04 08:12:00 +0200
categories: [PQC]
tags: [pake, harvest-now-decrypt-later, hybrid-key-exchange, universal-composability]
link: https://eprint.iacr.org/2026/1832
byline: "Yasmine Vazirinejad et al. (IACR ePrint 2026/1832, Aug 29 2026)"
description: "A hybrid password-authenticated key exchange protocol encapsulates a classical PAKE inside a post-quantum KEM to neutralize harvest-now-decrypt-later attacks, and is proven universally composable with a 2.81 millisecond handshake."
---

Existing hybrid password-authenticated key exchange (PAKE) constructions combine a classical PAKE with a post-quantum PAKE and rely on whichever is stronger, but it is hard to know which is stronger given how immature post-quantum PAKE designs still are. This paper instead proposes encapsulating a classical PAKE, specifically J-PAKE, inside a standard post-quantum key encapsulation mechanism, a modular separation that avoids the fragility of post-quantum password handling while neutralizing harvest-now-decrypt-later attacks from a quantum adversary that is currently only passive. The compiler works with any two-pass or three-pass PAKE, and the authors prove their concrete J-PAKE-plus-KEM instantiation is universally composable under the parallel composition framework of Lyu and Liu from EUROCRYPT 2025, achieving session key security and post-quantum forward secrecy under a strengthened harvest-now-decrypt-later threat model that even grants the quantum adversary the plaintext password. An implementation shows the complete handshake executes in 2.81 milliseconds, and the construction needs no ideal cipher, constant-time hash-to-curve, or trusted setup assumptions, relying only on standardized, widely deployed primitives.
