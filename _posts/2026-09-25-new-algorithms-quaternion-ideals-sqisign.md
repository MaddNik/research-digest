---
title: "New algorithms for quaternion ideals in SQIsign"
date: 2026-09-25 08:09:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-cryptography, deuring-correspondence, nist-signatures]
link: https://eprint.iacr.org/2026/2153
byline: "Antonin Leroux and Sina Schaeffler (IACR ePrint 2026/2153, Sep 22 2026)"
description: "New quaternion-ideal algorithms shrink the integer sizes needed inside SQIsign's isogeny computations, letting the NIST submission drop its GMP dependency."
---

Many isogeny-based schemes rely on the Deuring correspondence and therefore require computations with quaternion ideals. This paper generalizes recent results on the inert representation of quaternion ideals, yielding a normalized representation and simple, efficient algorithms for the case where the prime characteristic p is congruent to 3 modulo 4. The main benefit is that the size of the integers involved is easy to bound and smaller than in prior work, yielding a concrete bound of O(p to the 4th power) in the worst case, an improvement of at least a factor of O(p squared) over previous known bounds. The new algorithms are used in the latest update of SQIsign's implementation submitted to the third round of the NIST call for additional post-quantum signatures, where the low integer bounds allowed removing a dependency on the GMP library in favor of a custom fixed-size integer library without performance overhead. The authors note the algorithms apply beyond SQIsign to any isogeny-based protocol relying on the Deuring correspondence, such as the PRISM signature scheme.
