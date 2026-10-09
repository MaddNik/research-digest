---
title: "Round Optimal MPC With Provable Cheater Identification"
date: 2026-10-09 08:26:00 +0200
categories: [Cryptography]
tags: [secure-multiparty-computation, round-complexity, identifiable-abort]
link: https://eprint.iacr.org/2026/2393
byline: "Yashvanth Kondi et al. (IACR ePrint 2026/2393, Oct 7 2026)"
description: "The authors settle the round complexity of secure multiparty computation with provable identifiable selective abort for almost all corruption thresholds, giving matching two- and three-round protocols."
---

Secure multiparty computation with provable identifiable selective abort (PISA) guarantees that every honest party either obtains the output or a certificate that convinces an external auditor that a specific party cheated, and crucially honest parties need not agree on which outcome they get, unlike the classical notion of identifiable abort, which requires unanimity and typically needs broadcast. Prior work showed that PISA, unlike identifiable abort, can be built over point-to-point channels alone, is feasible exactly when guaranteed output delivery is feasible, and achieved six rounds in that setting. This paper settles the round complexity of PISA for nearly all corruption thresholds t relative to the number of parties n, proving that two rounds are impossible for t at least n over 3 even with arbitrary setup and computational assumptions, giving a three-round protocol for any t less than n over 2 that is therefore round-optimal for the middle range of thresholds, and giving a two-round protocol for t less than n over 4. The two-round construction introduces a new primitive called one-or-nothing secret sharing with omissions.
