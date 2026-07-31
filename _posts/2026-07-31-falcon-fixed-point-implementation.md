---
title: "Toward a Secure Fixed-Point Implementation of the Falcon Signature Scheme"
date: 2026-07-31 08:08:00 +0200
categories: [PQC]
tags: [falcon, fixed-point-arithmetic, implementation-security, signature-scheme]
link: https://eprint.iacr.org/2026/1531
byline: "Daniel De Almeida Braga et al. (IACR ePrint 2026/1531, Jul 26 2026)"
description: "This paper develops a fixed-point arithmetic version of Falcon's signing procedure to avoid the implementation pitfalls of floating point."
---

Falcon achieves the smallest signature sizes among NIST's standardized post-quantum schemes but depends on floating-point arithmetic, which is difficult to implement securely and portably. The authors provide a boundedness analysis showing intermediate signing variables depend on four quantities fixed at key generation, and propose a modified key generation step that rejects fewer than 50 percent of keys via validation thresholds. They also give a precision analysis using Renyi divergence arguments to prove security under empirically derived error bounds. Their resulting C implementation runs about twice as slow as the original floating-point Falcon, but roughly an order of magnitude faster than emulated floating-point implementations.
