---
title: "Analyzing Compiler-induced Constant-time Violations with Compiler at Scale"
date: 2026-10-30 08:33:00 +0200
categories: [Hardware Security]
tags: [constant-time, compiler-optimization, timing-side-channel, llvm]
link: https://eprint.iacr.org/2026/2653
byline: "Jing Liu et al. (IACR ePrint 2026/2653, Oct 26 2026, IEEE S&P 2027)"
description: "CTGREP applies differential analysis across the entire compilation chain of seven cryptographic libraries, three Clang versions, and six target platforms, finding compiler-induced constant-time violations and fixing 48 cases with library developers."
---

Constant-time programming is a de facto standard for cryptographic libraries to prevent timing side-channel attacks, but compiler optimizations can silently break constant-time source code during compilation, and prior analysis approaches examine only a single compilation point, either the final binary or one intermediate representation, leaving them unable to fully explain where, how, and under which compiler configurations violations arise. This paper introduces CTGREP, a compiler-based framework that answers all three questions by applying differential analysis across the entire compilation chain rather than a single stage. Applying CTGREP to seven complete cryptographic libraries across three Clang versions, six target platforms, and thousands of compiler configurations, the authors systematically detect compiler-induced constant-time violations in the wild and collaborate with library developers to address 48 cases, identifying seven new problematic LLVM passes and bypassing and improving the state-of-the-art compiler-flag-based mitigation. The authors also quantify how compiler version, target platform, and optimization configuration each affect the rate of violations, aiming to complement the community's ongoing hardening efforts.
