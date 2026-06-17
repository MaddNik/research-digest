---
title: "Stickel-type key exchange with hidden subspaces"
date: 2026-06-17 08:27:00 +0200
categories: [Cryptography]
tags: [cryptanalysis, key-exchange, non-commutative, protocols]
link: https://eprint.iacr.org/2026/1257
byline: "Fintan Costello et al. (IACR ePrint 2026/1257, Jun 14 2026)"
description: "A polynomial-time break of all Stickel-type matrix key-exchange schemes using public subspaces, plus a new scheme that hides the subspaces by conjugation."
---

Stickel-type key exchange schemes use two-sided multiplication of n by n matrices
over a prime field, where the matrices are drawn from public subspaces with a
particular commuting structure. The authors give a witness-finding cryptanalysis
covering Stickel's original proposal, Shpilrain's polynomial extension, Nager's
algebraic extension, and more generally all Stickel-type approaches using public
subspaces over matrix algebra in finite fields, showing that all such schemes can
be broken in polynomial time. They then describe a new key establishment scheme
using two-sided matrix multiplication in which the commuting subspaces used to form
the key are hidden via conjugation by private terms, blocking this specific
public-subspace analysis. The witness-finding problem in the new scheme has a direct
reduction from a standard NP-hard problem, Edmonds' problem. This positions the
proposal as resistant to the attack technique that defeats the prior public-subspace
constructions.
