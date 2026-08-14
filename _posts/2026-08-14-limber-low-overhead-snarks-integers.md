---
title: "Limber: Low Overhead SNARKs for Integers from Any PCS"
date: 2026-08-14 08:22:00 +0200
categories: [Cryptography]
tags: [snark, non-native-arithmetic, polynomial-commitments]
link: https://eprint.iacr.org/2026/1635
byline: "Jessica Chen et al. (IACR ePrint 2026/1635, Aug 7 2026)"
description: "Limber is a practical polynomial-commitment-based technique for proving integer arithmetic in SNARKs with minimal overhead, proving RSA arithmetic more than 67 times faster than prior circuit-based approaches."
---

Non-native arithmetic, such as representing integer operations inside a prime-field circuit, is a major source of both performance overhead and implementation bugs in SNARK systems; the authors cite that 9 of 27 tracked critical zero-knowledge bugs stemmed from non-native arithmetization. Building on the Zaratan fingerprinting recipe, which reduces an integer relation to the same relation over a randomly sampled prime field, they construct Limber, the first practical integer-mod polynomial commitment scheme with asymptotically vanishing multiplicative commitment overhead. Limber can be instantiated from any standard polynomial commitment scheme, including ones defined over small fields, and is paired with a PIOP for integer R1CS to yield a full SNARK. Their implementation proves RSA arithmetic more than 67 times faster than prior circuit-based approaches.
