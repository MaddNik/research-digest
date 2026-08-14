---
title: "A Torus-Structured Generalisation of NTRU: the NTC Assumption, its Cryptanalysis, and a Compact KEM"
date: 2026-08-14 08:08:00 +0200
categories: [PQC]
tags: [ntru-generalization, torus-assumption, kem, key-size-comparison]
link: https://eprint.iacr.org/2026/1642
byline: "Sidoine Djimnaibeye et al. (IACR ePrint 2026/1642, Aug 9 2026)"
description: "A new Noisy Torus Conjugation hardness assumption generalizes NTRU to higher-rank matrix rings and yields a compact key encapsulation mechanism with keys close to Kyber's size."
---

The paper defines the Noisy Torus Conjugation (NTC) assumption, in which a short secret confined to a non-split maximal torus of GL_k(R_q) acts by conjugation on a uniform matrix, generalizing classical NTRU (where k equals 1) to the case where k is greater than or equal to 2. The authors argue this generalization yields more favorable lattice geometry than standard NTRU. Building on NTC, they construct a key encapsulation mechanism with a tight security reduction to the underlying assumption. They report that at NIST security categories 1, 3, and 5 their public keys are only about 1.08 to 1.16 times the size of Kyber's. The authors are explicit about which claims are proven versus heuristic and which aspects remain open, and they include cryptanalysis of the new assumption.
