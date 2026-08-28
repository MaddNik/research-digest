---
title: "Separating Quantum Indistinguishability Obfuscation from Falsifiable Assumptions"
date: 2026-08-28 08:29:00 +0200
categories: [Cryptography]
tags: [quantum-obfuscation, witness-encryption, black-box-separation, qma]
link: https://eprint.iacr.org/2026/1800
byline: "Mohammed Barhoush et al. (IACR ePrint 2026/1800, Aug 25 2026)"
description: "This work shows that witness encryption for QMA, and hence quantum indistinguishability obfuscation for null circuits, cannot be based on falsifiable cryptographic assumptions via a restricted but broad class of quantum black-box reductions."
---

Quantum indistinguishability obfuscation aims to make a quantum circuit unintelligible while preserving its functionality, and serves as a foundational primitive for applications such as witness encryption for QMA, non-interactive zero-knowledge for QMA, and attribute-based encryption for BQP, but constructing it from standard assumptions has remained a major open problem. The authors prove that the security of witness encryption for QMA cannot be based on any falsifiable cryptographic assumption via a restricted class of quantum black-box reductions, and since quantum indistinguishability obfuscation for null quantum circuits implies witness encryption for QMA, this also separates null quantum indistinguishability obfuscation from falsifiable assumptions. Because almost all standard cryptographic assumptions are falsifiable, the result presents a barrier to basing quantum indistinguishability obfuscation on standard assumptions. The ruled-out reductions are restricted to querying the adversary classically, non-adaptively, at the same security parameter, and only on honestly generated ciphertexts, and the impossibility applies only to witness encryption with classical ciphertexts, so it does not rule out obfuscators whose output is a quantum state, relying on the existence of a QMA-QCIP[2] gap problem.
