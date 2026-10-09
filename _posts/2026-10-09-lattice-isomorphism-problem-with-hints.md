---
title: "The Lattice Isomorphism Problem with Hints"
date: 2026-10-09 08:10:00 +0200
categories: [PQC]
tags: [hawk-signature, lattice-isomorphism-problem, side-channel-leakage]
link: https://eprint.iacr.org/2026/2381
byline: "Melissa Rossi (IACR ePrint 2026/2381, Oct 6 2026, to appear in TCHES 2027)"
description: "A new cryptanalysis framework studies how partial leakage of the Hawk signature scheme's secret, through side channels or the signature itself, erodes the security of the underlying Lattice Isomorphism Problem."
---

The Lattice Isomorphism Problem (LIP) underlies the Hawk signature scheme submitted to the second NIST call for post-quantum signatures, and this paper studies LIP security when partial information, or hints, about the secret solution is available through side-channel attacks or by design. The author embeds LIP into a shortest vector problem over a different lattice than the one used in Hawk's own specification, and introduces conversion techniques that turn hints on arbitrary linear combinations of secret key coefficients into hints usable on the target lattice. Using the LeakyLWEEstimator tool, the paper obtains concrete security estimates for Hawk in the key-recovery setting, finding that Hawk signatures carry intrinsic information that can itself serve as a source of hints, eroding the original security estimates by around 11 bits for Hawk-1024. The framework is also applied to prior side-channel analysis results on Hawk, resolving an open problem from a TCHES 2024 paper and pointing to further attack paths enabled by fault-injection techniques.
