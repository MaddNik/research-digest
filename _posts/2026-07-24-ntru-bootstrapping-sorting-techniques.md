---
title: "Faster NTRU-based Bootstrapping with Extended and Sorting-based Techniques"
date: 2026-07-24 08:14:00 +0200
categories: [FHE]
tags: [ntru, bootstrapping, multi-key, sorting-techniques]
link: https://eprint.iacr.org/2026/1447
byline: "Jingwei Feng et al. (IACR ePrint 2026/1447, Jul 16 2026)"
description: "The paper improves NTRU-based fully homomorphic encryption bootstrapping by removing a modulus divisibility constraint and cutting redundant computation with sorting-based techniques."
---

The authors target NTRU-based bootstrapping for fully homomorphic encryption and apply extended techniques to remove the limitation that the modulus q must divide 2 times N, which lets bootstrapping use smaller ring dimensions with larger moduli. They introduce sorting-based methods to eliminate redundant computations during bootstrapping and extend the approach to multi-key settings. Their implementation reports roughly a 1.82 times speedup over prior work. They also report reduced memory requirements tied to their sorting parameter. The work is positioned as a practical efficiency improvement for NTRU-based FHE bootstrapping rather than a new scheme.
