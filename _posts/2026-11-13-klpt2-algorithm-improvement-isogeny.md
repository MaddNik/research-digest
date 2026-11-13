---
title: "An improvement to the KLPT2 algorithm"
date: 2026-11-13 08:11:00 +0200
categories: [PQC]
tags: [isogeny-cryptography, higher-dimensional-isogenies, klpt]
link: https://eprint.iacr.org/2026/2862
byline: "Abel Laval (IACR ePrint 2026/2862, Nov 10 2026)"
description: "A short note tweaks the KLPT2 algorithm used in higher-dimensional isogeny cryptography to shrink its output size bound."
---

This short note presents a tweak to the KLPT2 algorithm, a tool used in higher-dimensional isogeny-based cryptography, that reduces the size of its output from an order of p to the power of 15.5 to an order of p to the power of about 14.5. The author then shows that a recent improvement to the related KLPT algorithm by Nakagawa, Yoshizumi, and Onuki is compatible with the Hermitian module splitting approach used in this work. Combining the two improvements further lowers the reduced degree bound to an order of p to the power of about 14. The result is a concrete algorithmic improvement to a building block used in isogeny-based signature and encryption schemes that rely on higher-dimensional isogeny computations.
