---
title: "Triple Cryptanalysis of Isogeny-Based VRFs from Asiacrypt 2025"
date: 2026-08-07 08:03:00 +0200
categories: [PQC]
tags: [isogeny, verifiable-random-function, cryptanalysis]
link: https://eprint.iacr.org/2026/1623
byline: "Yi-Fu Lai, Yu Yu, and Xiaogang Zhou (IACR ePrint 2026/1623, Aug 5 2026)"
description: "Three distinct attacks break the uniqueness and secret-key security of an isogeny-based verifiable random function construction presented at Asiacrypt 2025."
---

This paper reports three separate attacks against a verifiable random function (VRF) scheme built from isogenies that was proposed at Asiacrypt 2025. The first attack exploits an inconsistency in how the public key is represented, which allows an adversary to produce multiple valid outputs for the same input and thereby breaks the scheme's uniqueness guarantee. The second attack leverages information about curve coefficients to recover the secret key, requiring about 1536 queries and roughly 30 minutes of computation according to the authors. A third attack targets a related group-action-based VRF construction, demonstrating a one-query attack with high success probability. Taken together, the results show that the isogeny-based VRF construction from Asiacrypt 2025 fails to meet its claimed security properties.
