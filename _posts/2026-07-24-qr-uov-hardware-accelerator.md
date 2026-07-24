---
title: "A High-Speed Hardware Accelerator for QR-UOV Signature Scheme"
date: 2026-07-24 08:13:00 +0200
categories: [PQC]
tags: [qr-uov, hardware-accelerator, multivariate-signatures, implementation]
link: https://eprint.iacr.org/2026/1458
byline: "Renma Sugai et al. (IACR ePrint 2026/1458, Jul 17 2026)"
description: "A hardware accelerator for the multivariate signature scheme QR-UOV performs key generation, signing, and verification in under one millisecond each at security level I."
---

The authors propose a hardware accelerator that implements all three operations of QR-UOV, a multivariate-quadratic signature scheme and NIST additional digital signature candidate, namely key generation, signature generation, and signature verification. The design uses systolic arrays and optimized matrix operation circuits to speed up the structured matrix arithmetic that QR-UOV relies on. At security level I, the accelerator achieves execution times of 0.74 milliseconds for key generation, 0.28 milliseconds for signature generation, and 0.19 milliseconds for signature verification. The work targets practical deployment of QR-UOV as an efficient hardware-based alternative to lattice-based signature schemes.
