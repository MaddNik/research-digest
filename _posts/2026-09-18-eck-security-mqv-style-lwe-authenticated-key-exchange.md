---
title: "On the eCK Security of MQV-Style LWE-Based Authenticated Key Exchange"
date: 2026-09-18 08:14:00 +0200
categories: [PQC]
tags: [lwe, authenticated-key-exchange, signal-leakage-attack, cryptanalysis]
link: https://eprint.iacr.org/2026/2017
byline: "Ruoyu Ding et al. (IACR ePrint 2026/2017, Sep 14 2026, ASIACRYPT 2026)"
description: "New signal leakage attacks recover the static secret key from two LWE-based authenticated key exchange protocols designed to resist such attacks, settling a long-standing open question about one of them."
---

Designing authenticated key exchange directly from the Learning with Errors assumption, rather than through generic constructions, remains a hard open problem in post-quantum cryptography, partly because the reconciliation mechanisms these protocols need can leak extra information to active adversaries under key reuse. Earlier signal leakage attacks by Bindel et al. and Qin et al. failed against protocols hardened with dedicated countermeasures, leaving open whether such hardened protocols were actually secure. This paper targets the MQV-style AKE protocol of Zhang et al. from EUROCRYPT 2015, known as ZZDSD-AKE, and resolves the long-standing open question of whether it achieves security under the strong extended Canetti-Krawczyk (eCK) model, showing with a geometric-perspective attack exploiting ephemeral key compromise that it does not. The authors extend the same methodology to the GDLL-KE protocol of Gao et al., which uses a randomized noise countermeasure against key reuse, and show that this countermeasure also fails to eliminate secret-dependent leakage. Their implementations recover the secret key using roughly 1,700 queries against ZZDSD-AKE and 180 queries against GDLL-KE, indicating that MQV-style structures and simple randomization countermeasures are not sufficient to secure LWE-based authenticated key exchange against active attackers.
