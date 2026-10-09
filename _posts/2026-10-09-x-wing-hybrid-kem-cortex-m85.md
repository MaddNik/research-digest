---
title: "X-Wing on Cortex-M85: Architecture-Aware Integration and End-to-End Evaluation"
date: 2026-10-09 08:14:00 +0200
categories: [PQC]
tags: [hybrid-kem, ml-kem, cortex-m85, embedded-implementation]
link: https://eprint.iacr.org/2026/2352
byline: "Do-Yun Park and Hwa-Jeong Seo (IACR ePrint 2026/2352, Oct 5 2026)"
description: "An architecture-aware Cortex-M85 implementation of the X-Wing hybrid KEM, combining ML-KEM-768 and X25519, cuts cycle counts by double digit percentages across key generation, encapsulation, and decapsulation."
---

X-Wing combines ML-KEM-768 and X25519 for hybrid post-quantum key establishment, and this paper adapts the coefficient representation and storage order of an M-profile Vector Extension NTT to the existing ML-KEM path while optimizing data-format transformations and X25519 arithmetic, preserving compatibility with draft-10 of the specification. The authors also exploit the fact that the two X25519 computations performed during encapsulation can share an inversion. Across ten paired comparisons from five independent reflashes of one EK-RA8M1 board, their eight-technique integrated implementation achieves minimum cycle reductions of 18.61 percent for key generation, 18.89 percent for encapsulation, 12.25 percent for decapsulation reusing an expanded key, and 15.22 percent for decapsulation including seed expansion, at the cost of 35,692 bytes of additional nonvolatile storage. They separately report a corrected variant that addresses identified secret-sign-dependent operand-address selections, though some key-varying timing signals remain only partly resolved, so no whole-program constant-time guarantee is claimed for the corrected version.
