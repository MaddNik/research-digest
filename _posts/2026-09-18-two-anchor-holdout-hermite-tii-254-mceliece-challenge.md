---
title: "Two-Anchor Holdout/Hermite: Solving the TII-254 McEliece Key Recovery Challenge"
date: 2026-09-18 08:11:00 +0200
categories: [PQC]
tags: [mceliece, code-based-cryptography, key-recovery, cryptanalysis]
link: https://eprint.iacr.org/2026/1986
byline: "Markku-Juhani O. Saarinen (IACR ePrint 2026/1986, Sep 11 2026)"
description: "A researcher solved the TII-254 McEliece key recovery challenge, the hardest McEliece challenge broken so far under the original 2^254 brute-force metric."
---

The author reports solving the TII-254 McEliece key recovery challenge, currently the hardest solved challenge under the original brute-force metric of 2^254 operations, whose parameters (m, t, n) = (8, 12, 223) define a binary [223, 127] code specified by a full-rank 96 by 223 parity-check matrix. The method is presented as a thirteen-step process that separates heuristic from non-heuristic choices. At a high level, the attack computes two complete 121-dimensional relation kernels conditioned at distinct public coordinates, combines them to isolate a certified 80-dimensional pair core, removes a 64-dimensional common nuisance space, and identifies the remaining 16 dimensions as an F_(2^8) projective-line geometry, yielding all 87 visible locators before a deterministic completion search recovers the full support and polynomial. The two final Krylov sequences alone consumed 27.2 GPU-hours on NVIDIA GH200 hardware, excluding GPU reconstruction and CPU processing. The author provides a self-contained artifact with compact recovery inputs, code, an independent key verifier, and Lean proofs of the reusable linear-algebraic steps.
