---
title: "Power side-channel leakage distinguishers on LESSv2.0: Exploiting sparse columns in Gaussian Elimination"
date: 2026-08-07 08:27:00 +0200
categories: [Hardware Security]
tags: [side-channel, post-quantum, power-analysis]
link: https://eprint.iacr.org/2026/1601
byline: "Maciej Czuprynko et al. (IACR ePrint 2026/1601, Aug 4 2026)"
description: "Researchers demonstrate the first passive power side-channel attack on LESSv2.0, a NIST post-quantum signature candidate, by exploiting leakage from sparse versus dense column handling during Gaussian elimination."
---

LESSv2.0 is a second-round candidate in NIST's additional post-quantum digital signature call. The authors show that its core Gaussian elimination step leaks information depending on whether a column being processed is sparse or dense, and that this leakage persists even in constant-time implementations. The attack distinguishes zero-valued computations from random ones and uses correlation-based key recovery, requiring between 300 and 2357 observed signatures depending on the parameter set. The large number of traces needed reflects that the targeted information is inherently noisy even without measurement noise. The authors evaluate first-order masking, shuffling, and blinding as candidate countermeasures and confirm the presence of leakage on a physical target, including masked implementations.
