---
title: "A Universal Forgery Attack on the Origami Signature Scheme from the Public Key Alone"
date: 2026-10-09 08:27:00 +0200
categories: [Cryptography]
tags: [multivariate-cryptography, cryptanalysis, signature-forgery]
link: https://eprint.iacr.org/2026/2390
byline: "Hugo Louiso et al. (IACR ePrint 2026/2390, Oct 7 2026)"
description: "Origami, a multivariate signature scheme submitted to the NGCC round-1 public-key call, is shown to be a disguised Rainbow-type scheme whose structure lets an attacker forge signatures using only the public key."
---

Origami is a multivariate signature scheme submitted to the NGCC round-1 public-key call, and the authors show that its submitted bilinear construction is actually a Rainbow-type scheme whose central map is exposed, since the verification map turns out to be the layered signing map arranged in a public coordinate order. This public layered structure gives an equivalent secret key directly from the public key, allowing signature forgery at roughly the cost of a single verification, about 0.01 seconds at the Origami-128 parameter set. The attack succeeds against the unmodified reference implementation across all four parameter sets and the official test vectors, and the authors also refute the inversion assumption underlying the scheme's security proof in a bilinear independent-coefficient model. They note that the hidden local algebras Origami introduces do not prevent the attack, and instead raise a separate issue, since the specification treats constrained matrix coordinates as independent even though honest signatures actually lie in a proper subspace.
