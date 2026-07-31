---
title: "Just-in-Time-OPRFs and a Modular Framework for Fast Private Set Intersection"
date: 2026-07-31 08:21:00 +0200
categories: [Cryptography]
tags: [private-set-intersection, oprf, oblivious-transfer]
link: https://eprint.iacr.org/2026/1532
byline: "Mihir Bellare et al. (IACR ePrint 2026/1532, Jul 26 2026)"
description: "A newly defined primitive, the Just-In-Time OPRF, gives a unified, concretely secure way to derive fast private set intersection protocols from oblivious transfer or vector oblivious linear evaluation."
---

The paper gives a modular framework for private set intersection built around a newly defined primitive called a Just-In-Time OPRF. It shows how to obtain private set intersection generically from any Just-In-Time OPRF and how to build Just-In-Time OPRFs from either oblivious transfer or vector oblivious linear evaluation, recovering known private set intersection protocols from the literature as special cases of this single framework. Unlike much prior work, the analysis is concrete rather than asymptotic, giving explicit bounds so practitioners can pick parameters to hit a target security level, for example 128 bits, in practice. The authors report that this concrete-security lens surfaces meaningful differences between oblivious-transfer-based and vector-oblivious-linear-evaluation-based private set intersection that asymptotic analysis obscures, and argue the framework opens the door to new protocols by constructing new Just-In-Time OPRFs.
