---
title: "Quotienting Redundant Tables: Practical Master-Key Recovery from WBSLT White-Box AES"
date: 2026-11-06 08:26:00 +0200
categories: [Cryptography]
tags: [white-box-cryptography, aes, key-extraction, lookup-tables]
link: https://eprint.iacr.org/2026/2729
byline: "Jiseok Bang and Seungkwang Lee (IACR ePrint 2026/2729, Nov 3 2026)"
description: "A table-quotienting technique breaks WBSLT, a recently published white-box AES design, recovering the master key from its public lookup tables in a median of 146 queries."
---

White-box AES implementations try to hide a secret key inside public lookup tables even when the attacker can see and manipulate the entire implementation. This paper shows that enlarging a lookup table's address space does not hide a smaller internal selector when the complete public table factors through a core with distinct rows and distinct columns, a condition the authors demonstrate holds in WBSLT, a white-box AES design presented at NDSS 2026 that had claimed resistance to several structural attacks. In WBSLT's released generator, the joint output of each group of four first-round TypeII tables has an exact 16 by 16 quotient of its 64 by 64 address space, and mapping its row and column classes to observed addresses recovers the original nibble partition of each AES input byte; two 16-point restrictions of each keyed AES S-box, extracted under the generator's linear input decoder, then identify its embedded key byte. Using only public tables and traces of chosen encoded inputs, the authors recover every key in 200 general WBSLT instances that had passed 200,000 reference AES tests, needing a median of 146 and at most 221 inputs, and they confirm the same vulnerability in the released optimized C source, with only a one-line functional repair resisting the attack. An adjacent-round adaptation also recovers 20 out of 20 exact keys without reconstructing the nibble partition, using fewer live trace queries than the first-round route.
