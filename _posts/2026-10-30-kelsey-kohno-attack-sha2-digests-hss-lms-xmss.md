---
title: "A Kelsey-Kohno Attack Variant against SHA-2 Message Digests in HSS/LMS and XMSS"
date: 2026-10-30 08:13:00 +0200
categories: [PQC]
tags: [hash-based-signatures, hss-lms, xmss, multi-target-attack]
link: https://eprint.iacr.org/2026/2635
byline: "Falko Strenzke (IACR ePrint 2026/2635, Oct 25 2026)"
description: "A multi-target second-preimage attack adapting Kelsey and Kohno's herding technique reduces the generic SHA-256 security of HSS/LMS and XMSS message hashing from 2 to the 256 to about 2 to the 166 compression function calls under NIST's signature-count bound."
---

This paper presents a multi-target second-preimage attack on the message hashing of the stateful hash-based signature schemes HSS/LMS and XMSS when instantiated with SHA-256 or truncated SHA-256/192. The attack builds on Kelsey and Kohno's herding technique, merging the chaining states that follow the per-signature prefixes of many collected signatures, level by level through state collisions, into a single chaining state from which one search can target all collected signatures at once, defeating the intended commitment to the signing key and leaf index. Under NIST's bound of 2 to the 64 signatures spread over any number of keys, the cost for SHA-256 falls from the nominal 2 to the 256 to about 2 to the 166 compression function calls for messages up to 4 gibibytes, a loss of 100 bits of security, and the SHA-256/192 parameter set loses 39 bits. Because the attack pools signatures across keys, even a single key's first signature can contribute to an ecosystem-wide exposure, though the author notes that SHAKE256-based parameter sets are not affected since the attack exploits SHA-256's narrow chaining state.
