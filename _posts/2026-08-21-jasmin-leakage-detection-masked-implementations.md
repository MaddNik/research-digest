---
title: "Toward Secure Compilation: Leakage Detection for Masked Implementations in Jasmin"
date: 2026-08-21 08:24:00 +0200
categories: [Hardware Security]
tags: [masking, jasmin, compiler-security, leakage-detection]
link: https://eprint.iacr.org/2026/1696
byline: "Nicolai Schmitt et al. (IACR ePrint 2026/1696, Aug 15 2026)"
description: "A compiler-integrated leakage detection pass for the Jasmin language catches masking flaws introduced during instruction selection and register allocation."
---

The authors observe that algorithmically correct masked implementations can still leak on real hardware once a compiler performs instruction selection, register allocation, and stack allocation, because these passes can inadvertently combine shares. They propose a leakage detection mechanism placed before register and stack allocation in Jasmin's compiler pipeline, using a configurable microarchitecture-oriented model that tracks interactions among shares, secret data, random masks, and public values rather than relying on power-trace simulation. The method was validated on 60 test cases covering different classes of leakage sources introduced by compilation. The authors present it as a foundation for future automated leakage-removal passes in the compiler.
