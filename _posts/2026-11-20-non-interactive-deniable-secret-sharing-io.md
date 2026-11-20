---
title: "A Note on Non-interactive Deniable Secret Sharing from Indistinguishability Obfuscation"
date: 2026-11-20 08:24:00 +0200
categories: [Cryptography]
tags: [secret-sharing, indistinguishability-obfuscation, deniability, constrained-prfs]
link: https://eprint.iacr.org/2026/2884
byline: "Shafik Nassar (IACR ePrint 2026/2884, Nov 13 2026)"
description: "Any secret sharing scheme can be upgraded into a non-interactive deniable scheme with only polylogarithmic share-size overhead using indistinguishability obfuscation and standard assumptions."
---

Deniable secret sharing, introduced by Canetti et al. at TCC 2025, protects shareholders when a subset of them is coerced into revealing their shares, by letting a set of fakers produce fake shares that are consistent with a fake secret of their choice and indistinguishable from real shares. A recent TCC 2026 paper by Amores et al. studied a non-interactive version of this setting, where each faker locally computes its fake share from only its own share, the set of fakers, and the fake secret, but their constructions either had exponentially large shares or relied on virtual black-box obfuscation. The author shows how to upgrade any secret sharing scheme, for any access structure, into a non-interactive deniable secret sharing scheme using a collusion-resistant constrained pseudorandom function with static security, which can be instantiated from polynomially secure indistinguishability obfuscation and one-way functions. The resulting transformation adds share-size overhead that is polynomial in the number of shareholders, and using indistinguishability obfuscation directly together with a somewhere-statistically-binding hash reduces that overhead to polylogarithmic. Combined with prior work on succinct computational secret sharing, this yields succinct deniable secret sharing from indistinguishability obfuscation and standard assumptions.
