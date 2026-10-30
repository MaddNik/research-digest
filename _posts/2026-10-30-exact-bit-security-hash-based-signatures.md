---
title: "The Exact Bit Security of Hash-Based Signatures"
date: 2026-10-30 08:12:00 +0200
categories: [PQC]
tags: [hash-based-signatures, xmss, slh-dsa, formal-verification]
link: https://eprint.iacr.org/2026/2626
byline: "Mikhail Kudinov, Benedikt Wagner, and Emile Wambsgans (IACR ePrint 2026/2626, Oct 24 2026)"
description: "A Lean4-formalized security analysis of 128-bit XMSS and SLH-DSA shows that the exact bit security figure depends heavily on how an adversary's computational work is accounted for, ranging from 122 to 127 bits for strong unforgeability."
---

This paper formally analyzes the security of hash-based signatures in Lean4, focusing on how different conventions for accounting an adversary's work change the resulting notion of bit security. Studying two instances of XMSS with 128-bit digests, the authors find that most accounting modes yield 127 bits of security for strong unforgeability, but the most conservative convention, which counts only the adversary's direct random oracle queries, yields only 122 bits. These bounds are proven in the random oracle model without computational hardness assumptions, and the authors provide matching attacks showing the bounds are tight, along with a proof of a tight 127-bit bound of strong unforgeability for SLH-DSA-128s. The work is motivated by recent autoresearch competitions and aims to help designers of future cryptographic challenges choose a bit-security notion that accurately reflects their accounting needs.
