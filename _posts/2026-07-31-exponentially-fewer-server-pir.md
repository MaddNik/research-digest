---
title: "Exponentially Fewer-Server PIR from Sparser S-Decoding Polynomials"
date: 2026-07-31 08:22:00 +0200
categories: [Cryptography]
tags: [private-information-retrieval, foundations, coding-theory]
link: https://eprint.iacr.org/2026/1515
byline: "Aparna Gupte et al. (IACR ePrint 2026/1515, Jul 24 2026)"
description: "Under a number-theoretic conjecture, a new construction gives an s-server private information retrieval protocol with much lower communication for a given number of servers than previously known constructions."
---

The paper improves multi-server private information retrieval, showing that for any constant s there is an s-server protocol on an n-bit database with communication scaling as exp(O((log n) to the power 1/s times (log log n) to the power 1 minus 1/s)), whereas prior constructions achieving the same communication needed exponentially more servers, 2 to the power O(s). The result relies on a number-theoretic conjecture implied by either the generalized repunit conjecture or Schinzel's hypothesis H, and builds on the matching-vector-family and S-decoding-polynomial framework originally due to Efremenko and later refined by Ghasemi, Kopparty, and Sudan. The core technical contribution constructs S-decoding polynomials with minimal nonzero coefficients, resolving an open problem posed by Ghasemi and Kopparty, and the authors validate the construction empirically and make it unconditional for s up to 15.
