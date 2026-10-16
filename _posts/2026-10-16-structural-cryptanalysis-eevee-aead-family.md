---
title: "Structural Cryptanalysis of the Eevee AEAD Family"
date: 2026-10-16 08:23:00 +0200
categories: [Cryptography]
tags: [aead, forgery-attack, nonce-misuse, authenticated-encryption]
link: https://eprint.iacr.org/2026/2496
byline: "Shuping Mao et al. (IACR ePrint 2026/2496, Oct 15 2026)"
description: "Cryptanalysis finds structural flaws in the Eevee family of AEAD modes proposed at CCS 2023, breaking both its online and nonce-misuse security claims with practical distinguishers and forgeries."
---

Eevee is a family of three authenticated-encryption-with-associated-data modes, named Umbreon, Jolteon, and Espeon, proposed at CCS 2023 for IoT-to-cloud secure computation. This paper analyzes structural flaws in the algorithms of the full-version specification and in the proof steps underlying their online authenticated-encryption claims, presenting an associated-data-free, two-encryption prefix distinguisher with advantage close to certainty in the ideal-forkcipher model that contradicts the specified online ideal object. Independently, the separable associated-data transform yields a four-encryption nonce-misuse distinguisher with similarly high advantage, a deterministic associated-data-only forgery, and nonempty-message forgeries obtained from cross-domain state differences, contradicting the advertised nonce-misuse bounds of Umbreon and Espeon. Under nonce-respecting queries, one two-block Jolteon encryption permits a fresh one-block forgery with the same tag, while Espeon's short-message path permits arbitrary associated-data substitution. The authors trace these counterexamples to failures of online-prefix consistency, conditional transcript distributions, domain separation, and checksum freshness in the original proof, concluding that the central failures concern the mode design itself and cannot be fixed solely by correcting implementation encodings.
