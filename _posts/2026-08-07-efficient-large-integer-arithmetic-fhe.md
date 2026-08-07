---
title: "Efficient Large-Integer Arithmetic for FHE"
date: 2026-08-07 08:25:00 +0200
categories: [FHE]
tags: [rns, library-comparison, bfv]
link: https://eprint.iacr.org/2026/1608
byline: "Ahmad Al Badawi et al. (IACR ePrint 2026/1608, Aug 4 2026)"
description: "A survey of how large-integer residue number system arithmetic is implemented across major FHE libraries for the BFV, BGV, and CKKS schemes."
---

This paper reviews how residue number system techniques for large-integer arithmetic have evolved inside RLWE-based FHE libraries. It contrasts two main computational strategies: the integer-only approach of Bajard, Eynard, Hasan, and Zucca, which tolerates approximation overflows and corrects them afterward using auxiliary redundant moduli, against the floating-point approach of Halevi, Polyakov, and Shoup. The authors examine how basis extension and scaling operations, which are fundamental building blocks for the BFV, BGV, and CKKS schemes, are implemented across libraries including HElib, SEAL, PALISADE and OpenFHE, HEAAN, and Lattigo. They also discuss recent innovations such as reduced-error scaling and composite scaling that improve numerical precision specifically for CKKS. The paper further explores emerging positional number representations as potential alternatives to current residue-number-system methods.
