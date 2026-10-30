---
title: "From if to Oops: Turning a conditional into a key-recovery oracle"
date: 2026-10-30 08:36:00 +0200
categories: [Hardware Security]
tags: [fault-attack, csidh, isogeny-based-cryptography, deterministic-csidh]
link: https://arxiv.org/abs/2610.39910
byline: "Gustavo Banegas, Nia Dimitrova, and Monika Trimoska (arXiv:2610.39910, Oct 29 2026)"
description: "A fault attack that skips a single instruction at a fixed, public point in deterministic CSIDH and OSIDH-LD recovers full secret keys with one fault per execution, using at most 297 oracle queries and a demonstrated instruction skip on a ChipWhisperer-Lite."
---

Deterministic variants of CSIDH remove randomness from the group action either through implementation techniques or, in schemes such as Houben's deterministic CSIDH and OSIDH-LD, by design, which appeared to close off earlier fault attacks that targeted random point sampling. This paper shows that determinism opens a different avenue, since every secret-dependent step now occurs at a fixed, public point of every execution, letting an attacker fault the same step repeatedly. The attack forces the mask that selects which of two computational lanes computes the next isogeny to zero, for example by skipping one instruction, and whether the output changes reveals whether a secret exponent reaches a chosen threshold; a binary search over these thresholds recovers the full key with one fault per execution, at most 297 oracle queries for OSIDH-LD and 222 for deterministic CSIDH at CSIDH-512-sized keys. The authors recover full OSIDH-LD keys in a software fault simulation of the reference implementation and show on a ChipWhisperer-Lite that the targeted instruction is skipped with probability at least 0.94 at an isolated fault position, concluding that fault resistance for these schemes requires giving up determinism and proposing randomization-based countermeasures.
