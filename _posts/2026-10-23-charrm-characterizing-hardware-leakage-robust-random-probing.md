---
title: "CHARRM - Characterizing Hardware Leakage in the Robust Random Probing Model"
date: 2026-10-23 08:29:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, masking, random-probing-model, formal-verification]
link: https://eprint.iacr.org/2026/2552
byline: "Armand Schinkel and Pascal Sasdrich (IACR ePrint 2026/2552, Oct 20 2026)"
description: "CHARRM is an automated verification methodology for masked hardware circuits in the robust random probing model that for the first time allows exact verification of larger, composed circuit structures than the prior state-of-the-art tool IronMask."
---

Masking is a widely used countermeasure against passive side-channel analysis, but its practical application is often complex and prone to errors, which motivates automated security verification tools. The authors present CHARRM, a comprehensive methodology for efficient security verification in the (g, t, c)-robust (p, epsilon)-random probing model, advancing the concept of leakage characteristics to account for robust probe extension schemes across arbitrary circuit structures and enabling efficient computation of leakage probability bounds for glitch-extended and transition-extended robust probing scenarios. By linking the leakage characteristic to the Set of Input Shares function, the authors extend their verification methodology to established composability notions, and their automated reasoning framework demonstrates practicality and superior performance and accuracy on larger circuits compared with IronMask, the state-of-the-art competitor. For the first time, the method allows exact verification of larger, composed circuit structures, validated by corresponding case studies, advancing automated hardware security verification for masked cryptographic implementations against side-channel analysis in the presence of transient physical effects.
