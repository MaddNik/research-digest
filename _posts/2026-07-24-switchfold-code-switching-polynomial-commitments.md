---
title: "SwitchFold: Code-Agnostic Succinct Polynomial Commitments via Recursive Code Switching"
date: 2026-07-24 08:21:00 +0200
categories: [Cryptography]
tags: [polynomial-commitments, code-switching, succinct-proofs, brakedown]
link: https://eprint.iacr.org/2026/1489
byline: "Mingshu Cong et al. (IACR ePrint 2026/1489, Jul 21 2026)"
description: "A hash based multilinear polynomial commitment scheme that recursively switches between error correcting codes to shrink proof size while keeping the prover linear time."
---

The paper presents a generic hash based multilinear polynomial commitment scheme intended to work across different underlying error correcting codes. Its main technique recursively applies a code switching step that reduces a multilinear extension claim under one code to a smaller claim under a shorter code. The resulting SwitchFold construction keeps prover time linear in the input size while achieving polylogarithmic proof size and verification time. When instantiated with Brakedown codes, producing a variant called BrakeFold, the authors report 3.5 times smaller proof size and 20.6 times faster verification than plain Brakedown at billion coefficient scale with 100 bit security, while matching the succinctness of BaseFold with faster proving.
