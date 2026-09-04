---
title: "Arithmetic-to-Boolean Conversion in ALU with O(1) Bootstrapping via Overflow Cancellation"
date: 2026-09-04 08:15:00 +0200
categories: [FHE]
tags: [ckks, functional-bootstrapping, arithmetic-logic-unit, triangle-encoding]
link: https://eprint.iacr.org/2026/1840
byline: "Xuan Shen et al. (IACR ePrint 2026/1840, Aug 31 2026)"
description: "A shared-overflow-cancellation technique converts an encrypted machine word from triangle-encoded CKKS arithmetic to Boolean form using only two sequential functional bootstraps, independent of the word length."
---

Triangle encoding gives a CKKS-based representation for leveled word arithmetic on an arithmetic logic unit that mixes word-level arithmetic with bit-level logic, but its existing arithmetic-to-Boolean conversion recovers only one window per bootstrapping, so converting an l-bit message needed a number of sequential functional bootstraps proportional to l. This paper first extends triangle encoding from binary to general digit bases so a larger base shortens each triangle word and packs more words per ciphertext, then introduces shared-overflow cancellation, in which a period-D functional bootstrap evaluates remainders at all selected positions simultaneously while the matching quotients are recovered by affine arithmetic, and taking the difference between the current remainder and the preceding quotient cancels a shared overflow coefficient exactly. A second multi-value functional bootstrap jointly resolves carry behavior, and because the carry transfer rules compose associatively, parallel carry propagation resolves all carries with only O(log base 2 of l) leveled multiplication depth. The optimized conversion therefore needs just two sequential functional-bootstrap stages per input ciphertext regardless of word length, and preliminary measurements in an OpenFHE implementation for 64-, 128-, and 256-bit words indicate estimated latency speedups of 3.32 to 8.12 times and amortized speedups of 5.20 to 11.32 times over the prior Gao-Zheng scheme, though the authors note the full benchmark of the optimized version is not yet complete.
