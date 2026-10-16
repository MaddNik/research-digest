---
title: "Cube Attacks with Elimination Strategy: Key Recovery Attacks on Trivium"
date: 2026-10-16 08:25:00 +0200
categories: [Cryptography]
tags: [cube-attack, trivium, stream-cipher, monomial-prediction]
link: https://eprint.iacr.org/2026/2460
byline: "Haoran Li et al. (IACR ePrint 2026/2460, Oct 13 2026, TOSC 2025)"
description: "A new cube attack framework with an elimination strategy sets the best known practical and theoretical key recovery attacks on the Trivium stream cipher, reaching 855 rounds."
---

This paper introduces cube attacks with elimination strategy, a framework whose core idea is to find specific key conditions and cubes whose superpolies under those conditions can be computed efficiently, so that recovering the conditional superpolies lets an attacker solve the resulting equation system and retrieve key information, extending the attack to a larger key space when enough such conditions exist. To make this practical the authors propose a nested coefficient solver combining variable substitution and symbolic computation, a conditional monomial prediction technique for fast conditional superpoly recovery, and an automated cube search algorithm that combines numeric mapping with monomial prediction to generate large numbers of good cubes. Applied to Trivium, the techniques yield a practical key recovery attack on 840 rounds with complexity below 2 to the power 55 and a 77.8 percent success rate, a practical attack on 845 rounds with complexity below 2 to the power 56 and 98.1 percent success rate for most keys, and a theoretical weak-key attack reaching 855 rounds for 2 to the power 74 keys. The authors state these are the best known practical and theoretical attacks on Trivium, improving the number of rounds reached by 13 for practical attacks and 4 for theoretical attacks over prior results; the paper is a minor revision of a TOSC 2025 publication.
