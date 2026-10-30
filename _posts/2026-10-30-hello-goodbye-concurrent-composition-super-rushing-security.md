---
title: "HELLO, GOODBYE: Concurrent General Composition From Super-Rushing Security"
date: 2026-10-30 08:30:00 +0200
categories: [Cryptography]
tags: [multiparty-computation, concurrent-composition, super-rushing-security, round-complexity]
link: https://eprint.iacr.org/2026/2651
byline: "Anirudh Chandramouli (IACR ePrint 2026/2651, Oct 26 2026)"
description: "Adding just two synchronization rounds, a start round and an end round, compiles any R-round protocol secure against super-rushing adversaries into one secure under concurrent general composition in R+2 rounds, halving the overhead of a classic 2006 compiler."
---

A seminal 2006 result by Kushilevitz, Lindell, and Rabin showed that any standalone-secure synchronous multiparty computation protocol can be compiled to be secure under concurrent general composition by adding a synchronization step after every round, at least doubling the round complexity. This paper shows that for protocols secure against the stronger notion of super-rushing adversaries, introduced in 2025 work by Asharov, Chandramouli, Cohen, and Ishai, only two synchronization rounds are needed in total. Specifically, for an R-round protocol with a black-box, straight-line simulator that is secure against super-rushing adversaries, adding a single start synchronization round and a single end synchronization round yields security under concurrent general composition with selective abort in R+2 rounds, with no loss in the security reduction, and using a broadcast channel for the end round upgrades the guarantee to unanimous abort. The author further extends the compilers to the dishonest-majority setting with trusted setups such as a common reference string, under the conditions that each execution uses its own stateless copy of the setup and that the underlying protocol is secure against super-rushing adversaries with adaptive inputs, and shows that this adaptive-input requirement cannot be relaxed to standard security in the setup-hybrid model.
