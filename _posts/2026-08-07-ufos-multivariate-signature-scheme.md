---
title: "UFOs: A Very Efficient Multivariate Public Key Signature Scheme"
date: 2026-08-07 08:04:00 +0200
categories: [PQC]
tags: [multivariate, signature-scheme, uov]
link: https://eprint.iacr.org/2026/1607
byline: "Gilles Macario-Rat (IACR ePrint 2026/1607, Aug 4 2026)"
description: "UFOs is a new multivariate signature scheme in the Unbalanced Oil and Vinegar family that uses structured Frobenius-type quadratic forms to achieve a compressed public key while keeping UOV's efficient signing procedure."
---

The paper introduces UFOs, a public-key signature scheme belonging to the Unbalanced Oil and Vinegar (UOV) family of multivariate cryptographic constructions. Instead of using generic random quadratic polynomials as in standard UOV, UFOs employs a structured subclass of quadratic forms based on a Frobenius-type construction, which the author states yields a compressed representation of the public key while retaining the efficient signing procedure characteristic of UOV schemes. The paper covers the full key generation, signing, and verification algorithms for the scheme. It also discusses the scheme's resistance to algebraic and key-recovery style attacks and reports implementation metrics describing performance and key or signature size parameters, positioning UFOs as a compact alternative within the multivariate signature landscape currently under scrutiny in post-quantum standardization efforts.
