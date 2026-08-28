---
title: "A Note on the Security Proof of SQIsign"
date: 2026-08-28 08:14:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-based-cryptography, security-proof, zero-knowledge]
link: https://eprint.iacr.org/2026/1775
byline: "Maher Mamah and David Jao (IACR ePrint 2026/1775, Aug 22 2026)"
description: "This note shows that SQIsign's min-entropy is optimal, tightening but not fully closing a square-root loss gap in its CRYPTO 2025 security proof."
---

Aardal et al. provided the first complete security proof of SQIsign at CRYPTO 2025, but their reduction incurs a square-root loss in the prime characteristic from a loose min-entropy bound, which the authors note renders the security proof vacuous at NIST security level I once an adversary makes 2 to the 64th power signing queries. In this note, the authors show that SQIsign's min-entropy is in fact optimal, at order 1/p, an improvement over the previous bound. While this improvement does not yield full lambda-bit security, the authors show it preserves two-thirds of the expected bit security. They trace the remaining gap to an information-theoretic loss in the zero-knowledge simulation of SQIsign, concluding that a new proof technique is needed to achieve full lambda-bit security at the scheme's current parameters.
