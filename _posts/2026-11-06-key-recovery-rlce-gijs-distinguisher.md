---
title: "Key Recovery Against RLCE via the GIJS Distinguisher"
date: 2026-11-06 08:15:00 +0200
categories: [PQC]
tags: [rlce, code-based-cryptography, cryptanalysis, key-recovery]
link: https://eprint.iacr.org/2026/2716
byline: "Jacob Alperin-Sheriff (IACR ePrint 2026/2716, Nov 1 2026)"
description: "A new experimental attack breaks the RLCE code-based cryptosystem at a parameter regime previously believed secure, recovering a 128-bit key in about three hours."
---

This paper presents an experimental cryptanalysis of the RLCE code-based cryptosystem at the w equals n minus k parameter regime, which had previously been considered secure. The attack relies on the recent Ghoshal-Ishai-Jain-Sun, or GIJS, distinguisher, applied by shortening the public key at random positions and running the distinguisher with every column held out in turn to identify twin pairs based on how they appear across trials. Three such pairs are then unmixed using a root-finding cascade, after which the Sidelnikov-Shestakov algorithm applied to the resulting pure matrix recovers the secret key. The author experimentally verifies the attack by breaking the 128-bit security instance in 30.5 core-hours, roughly three hours of wall-clock time on a standard higher-end laptop.
