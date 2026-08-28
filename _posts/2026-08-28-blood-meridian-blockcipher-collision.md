---
title: "Blood MERIDIAN: a blockcipher that is not a blockcipher"
date: 2026-08-28 08:24:00 +0200
categories: [Cryptography]
tags: [block-cipher, cryptanalysis, collision-attack, lightweight-cryptography]
link: https://eprint.iacr.org/2026/1818
byline: "JP Aumasson (IACR ePrint 2026/1818, Aug 27 2026)"
description: "An explicit collision shows that the MERIDIAN lightweight blockcipher's Directional Substitution layer is not injective, breaking its claimed blockcipher and PRP security for every key."
---

MERIDIAN is a 128-bit blockcipher proposed as a lightweight alternative to AES. The author demonstrates that its Directional Substitution layer is not injective by giving an explicit collision, which produces a full 12-round collision for every key. As a consequence, no keyed instance of MERIDIAN is a permutation, so no decryption function can invert encryption on all plaintexts, meaning the cipher's blockcipher and pseudorandom permutation security claims both fail. The author additionally identifies a one-round differential that exceeds the designers' claimed bound by a factor of 13.37.
