---
title: "Differential Cryptanalysis of SPEEDY: Revised Security Evaluation and Improved Key Recovery Attack"
date: 2026-11-06 08:24:00 +0200
categories: [Cryptography]
tags: [speedy-cipher, differential-cryptanalysis, low-latency-ciphers, key-recovery]
link: https://eprint.iacr.org/2026/2746
byline: "Xinwei Yu et al. (IACR ePrint 2026/2746, Nov 3 2026)"
description: "A structural-restriction-free search method finds better differential characteristics for the low-latency SPEEDY block cipher and disproves some of its designers' original security claims."
---

SPEEDY is a family of low-latency block ciphers whose designers evaluated resistance to differential cryptanalysis using restricted assumptions about how differences propagate through its S-boxes. This paper introduces a search method that imposes no prior structural restrictions on allowed differential characteristics, instead using computational pruning to keep the search tractable while conservatively evaluating the pruned region. By decomposing a round characteristic into a core trail extended independently at both ends, and by reusing short-round trails through hash-map concatenation to build longer ones without expensive MILP models, the authors narrow the minimum number of active S-boxes for 4 rounds from a previously reported 35 to a range of 33 to 34, finding a 34-active-S-box characteristic outside the previous search space. They obtain the highest-probability differential characteristics known for 2 through 5 rounds, including characteristics for 2, 3, and 4 rounds that disprove the designers' original branch-number-based security claims. Using a quasidifferential framework on these characteristics, they also improve a prior key recovery attack on SPEEDY-7-192, yielding the best known attack with data complexity 2 to the 173.48 power and time complexity 2 to the 173.69 power encryptions.
