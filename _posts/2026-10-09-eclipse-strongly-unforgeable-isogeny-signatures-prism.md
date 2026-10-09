---
title: "ECLIPSE: Strongly Unforgeable Isogeny Signatures from the Prime-Degree Variant of PRISM"
date: 2026-10-09 08:13:00 +0200
categories: [PQC]
tags: [isogeny-signatures, sqisign, strong-unforgeability]
link: https://eprint.iacr.org/2026/2312
byline: "Dustin Ray (IACR ePrint 2026/2312, Oct 2 2026)"
description: "ECLIPSE provides the first implementation of the prime-degree PRISM signature variant, giving SQIsign-family signatures that bind the auxiliary isogeny the hash otherwise leaves unbound."
---

ECLIPSE implements the prime-degree signature construction that the PRISM authors described alongside their salted scheme, addressing a gap where a two-dimensional isogeny signature carries an auxiliary isogeny that the hash does not bind, which the SQIsign round-3 specification says prevents strong unforgeability. The prime-degree variant has no such auxiliary isogeny but had been published without parameters, code, or a running verifier, so this paper supplies the first implementation on the SQIsign round-3 primes, including a verifier, a canonical wire format, and two independent implementations that accept each other's signatures. The authors show that a MIKE key pair at the level I prime can double as an ECLIPSE key pair without modifying MIKE's code, making this the first shared key pair in the SQIsign family besides the CSIDH and CSI-FiSh group-action precedent. Signatures are 206 bytes at NIST level I, within 15 bytes of SQIsign at every matched state, and in one benchmark against the SQIsign reference assembly build, ECLIPSE signs 2.6 times faster while verification costs about twice as much; a formal strong-unforgeability proof is left to future work.
