---
title: "MIKE: a fast and compact post-quantum NIKE"
date: 2026-10-09 08:11:00 +0200
categories: [PQC]
tags: [isogeny-cryptography, non-interactive-key-exchange, supersingular-curves]
link: https://eprint.iacr.org/2026/2377
byline: "Andrea Basso et al. (IACR ePrint 2026/2377, Oct 6 2026)"
description: "MIKE is a new post-quantum non-interactive key exchange whose security rests on the CDH problem for a rank-2 Hermitian module action on supersingular elliptic curves, with very compact 80-byte public keys."
---

The authors introduce MIKE, short for Module Isogeny Key Exchange, a post-quantum non-interactive key exchange (NIKE) whose security relies on the computational Diffie-Hellman problem for the rank-2 Hermitian module action on supersingular elliptic curves. At NIST security level 1, MIKE achieves very compact public keys of 80 bytes. In their constant-time C implementation on an AMD CPU running at 3.3 gigahertz, key generation takes 0.65 milliseconds and computing the shared secret, including key validation, takes 4.9 milliseconds. The combination of small keys and fast operations makes MIKE a notable addition to the isogeny-based NIKE landscape, which has historically traded off key size against computation time.
