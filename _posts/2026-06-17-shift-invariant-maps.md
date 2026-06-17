---
title: "A family of invertible shift-invariant maps with strong arithmetic properties"
date: 2026-06-17 08:29:00 +0200
categories: [Cryptography]
tags: [symmetric-crypto, boolean-functions, primitives, nonlinear-layers]
link: https://eprint.iacr.org/2026/1249
byline: "Xiao-Xin Zhao et al. (IACR ePrint 2026/1249, Jun 12 2026)"
description: "A new family of shift-invariant maps generalizing the chi-map, characterized via an isomorphism to polynomial quotient rings that fully determines invertibility and cycle structure."
---

Shift-invariant maps are used to design nonlinear layers in many symmetric
cryptographic schemes, such as the chi-map in Keccak. This paper studies
shift-invariant maps on the n-dimensional binary vector space whose defining
functions come from a family of n-variable Boolean functions induced by a
bifix-free sequence, denoted Omega. The authors show that Omega forms a commutative
monoid under composition, and that its unit group is isomorphic to the unit group of
an explicit quotient ring of the binary polynomial ring, with the precise form
depending on whether the sequence length divides n. This isomorphism transforms
function composition into polynomial multiplication in a well-understood quotient
ring. As an application they analyze a specific map that includes the chi-map and
several other previously studied maps, showing it is invertible if and only if the
sequence length does not divide n, and they fully characterize its inverse and cycle
structure when it is invertible. The construction generalizes earlier works by
Kriepke et al. and Lyu et al.
