---
title: "BMuSig-L: Blind Multi-Signature from Lattice"
date: 2026-11-20 08:09:00 +0200
categories: [PQC]
tags: [lattice-cryptography, blind-signatures, multi-signatures, zero-knowledge]
link: https://eprint.iacr.org/2026/2894
byline: "Anirban Chakraborty et al. (IACR ePrint 2026/2894, Nov 14 2026)"
description: "BMuSig-L is a two-round, concurrently secure lattice-based blind multi-signature scheme built on the MuSig-L multi-signature and the Fuchsbauer-Wolf blind signature."
---

Blind signatures hide a message from the signer and prevent linking the resulting signature to its signing session, while multi-signatures let a group of signers jointly produce a single signature on a message. Blind multi-signatures, introduced by Karantaidou et al. at AsiaCCS 2024, combine both properties so that a group of signers can jointly sign a message without learning it and without being able to link the final signature to the session. The authors present BMuSig-L, a lattice-based, two-round, concurrently secure blind multi-signature scheme, building on the lattice-based multi-signature scheme MuSig-L from CRYPTO 2022 and the concurrently secure blind signature of Fuchsbauer and Wolf from CRYPTO 2024, which uses non-interactive zero-knowledge arguments and public-key encryption. They prove BMuSig-L is one-more unforgeable under the unforgeability of MuSig-L, the computational soundness of the underlying zero-knowledge proof system, and the knowledge soundness of the argument system employed, and they provide a prototype implementation evaluating signature size and verification time.
