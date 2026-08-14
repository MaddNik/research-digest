---
title: "How to use Polynomially-Hard iO: Turing Machine Obfuscation and More"
date: 2026-08-14 08:27:00 +0200
categories: [Cryptography]
tags: [indistinguishability-obfuscation, turing-machine-obfuscation, function-secret-sharing]
link: https://eprint.iacr.org/2026/1636
byline: "Jesko Dujmovic et al. (IACR ePrint 2026/1636, Aug 8 2026)"
description: "Turing machine obfuscation with unbounded input length is constructed for the first time from only polynomially-hard indistinguishability obfuscation, removing a prior reliance on subexponential hardness."
---

The authors revisit PViO, a form of indistinguishability obfuscation for Turing machines that provides security for pairs of machines whose functional equivalence is provable in Cook's Theory PV. Their main result is the first construction of this primitive from only polynomially-hard general-purpose indistinguishability obfuscation, rather than the subexponentially-hard indistinguishability obfuscation required by earlier work. The construction introduces a new adaptation of punctured programming combined with function secret sharing that lets the reduction program an entire input domain simultaneously instead of one input at a time. They show this technique also yields unleveled fully homomorphic encryption and adaptively-sound succinct arguments without needing complexity leveraging in either construction.
