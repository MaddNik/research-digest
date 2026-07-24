---
title: "Hybrid hash function based on the DLP and SIS problems"
date: 2026-07-24 08:12:00 +0200
categories: [PQC]
tags: [hash-function, sis-problem, ajtai-hash, provable-security]
link: https://eprint.iacr.org/2026/1459
byline: "Dimitri Koshelev and Francesc Sebe (IACR ePrint 2026/1459, Jul 17 2026)"
description: "A hybrid hash function combines the discrete logarithm problem and the lattice-based short integer solution problem to give double provable security under 128-bit security parameters with 256-bit moduli."
---

The authors present a hybrid hash function grounded simultaneously on the discrete logarithm problem and the short integer solution, or SIS, problem, describing it as folklore but little-known. They provide concrete parameters that achieve 128-bit security for the lattice-based SIS component while using 256-bit moduli. The construction generalizes the classical Pedersen hash, which relies on discrete logarithm hardness, and the classical Ajtai hash, which relies on SIS hardness, combining both into one hybrid variant. Because the function's security rests on two independent hardness assumptions, breaking it would require breaking both the discrete logarithm problem and SIS simultaneously, giving what the authors call double provable security.
