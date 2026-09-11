---
title: "Cryptanalysis of a knot-based key exchange"
date: 2026-09-11 08:13:00 +0200
categories: [PQC]
tags: [knot-theory, key-exchange, cryptanalysis, alternative-hard-problems]
link: https://eprint.iacr.org/2026/1898
byline: "Simon-Philipp Merz (IACR ePrint 2026/1898, Sep 5 2026)"
description: "An efficient attack breaks a proposed knot-based Diffie-Hellman key exchange for every choice of the finite type invariant used to derive the shared secret, and shows its key space is also too small."
---

The author presents an efficient attack on a knot-based Diffie-Hellman key exchange proposed by Sconza and Wildi, in which two parties exchange oriented knots, combine them under connected sum to obtain a common knot, and derive a shared secret by evaluating a finite type invariant of degree m on it. The attack maps knots into a truncated Polyak space where connected sum becomes multiplication and every element of the image is invertible, allowing the public knot to simply be divided out and bypassing the proposed countermeasures. The shared secret can be recovered from the public transcript at roughly three times the cost of running the protocol honestly. Independently of the attack, the author also shows the key space is too small for the suggested parameters, since reaching the claimed 128 bits of security would require a degree of at least 10, at which point a single invariant evaluation already costs around 2 to the 50 operations.
