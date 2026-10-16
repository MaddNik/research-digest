---
title: "A Hybrid BP-SAT Attack on MILENAGE: Combining the Complementary Strengths of Algebraic and Soft-Analytical Side-Channel Attacks"
date: 2026-10-16 08:35:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, milenage, belief-propagation, sat-solver]
link: https://eprint.iacr.org/2026/2487
byline: "Elena Dubrova et al. (IACR ePrint 2026/2487, Oct 14 2026)"
description: "Combining belief propagation with a SAT solver raises single-trace key recovery success on the AES-based MILENAGE SIM authentication algorithm to 93.8 percent, beating either technique alone."
---

Profiled side-channel attacks combine noisy leakage predictions with the mathematical relations of a target algorithm to recover secrets from few observations, and two established approaches are algebraic side-channel analysis, which encodes leakage and algorithmic relations as a Boolean satisfiability problem, and soft-analytical side-channel analysis, which performs belief propagation over a factor graph. The authors evaluate both on the AES-based MILENAGE authentication algorithm used on USIM cards, targeting the subscriber key and the operator-specific secret from a single trace, using neural networks to predict posterior distributions over AES S-box output bytes that feed both solvers. The belief-propagation approach recovers both secrets in 87.7 percent of attacks but converges to an incorrect operator secret in 6.1 percent of cases despite recovering the subscriber key correctly, while the SAT-based approach enforces global consistency and resolves this ambiguity but succeeds in only 34 percent of attacks within a one-hour timeout. Combining the two into a hybrid attack, where belief propagation refines the neural network predictions before they reach the SAT solver, recovers both secrets in 93.8 percent of single-trace attacks with a higher success rate and lower average runtime than either method alone. The authors also propose a masking countermeasure, based on an independent per-device secret for each AES round key, and confirm empirically that it reduces the attacker's advantage to zero bits and defeats the hybrid attack in all evaluated cases.
