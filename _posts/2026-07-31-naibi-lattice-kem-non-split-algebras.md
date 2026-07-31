---
title: "NAIBI: Binding Reconciliation KEMs and Ephemeral Key Agreement over Non-Split Commutative Algebras"
date: 2026-07-31 08:11:00 +0200
categories: [PQC]
tags: [lattice, module-lwe, key-encapsulation, key-agreement]
link: https://eprint.iacr.org/2026/1525
byline: "Sidoine Djimnaibeye et al. (IACR ePrint 2026/1525, Jul 25 2026)"
description: "NAIBI-Full is a new lattice-based key encapsulation mechanism combined with forward-secure ephemeral key-agreement protocols built over non-split commutative algebras."
---

The scheme uses the regular representation of non-split commutative algebras constructed over polynomial rings, where each participant shares a full matrix combining a generic public element with a structured secret. This construction exploits algebraic commutativity to minimize noise growth and achieve exact key agreement through error-correcting techniques. Its hardness rests on a single, well-characterized assumption the authors call structured-secret Module-LWE. The system claims IND-CCA2 security and offers two forward-secure ephemeral protocols with a provable binding guarantee against malicious keys, deliberately excluding static-static deployment modes to avoid key-mismatch vulnerabilities seen in related schemes, and targets NIST security categories 1, 3, and 5.
