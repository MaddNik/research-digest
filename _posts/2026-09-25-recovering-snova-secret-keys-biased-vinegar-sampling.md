---
title: "Recovering SNOVA Secret Keys from Biased Vinegar Sampling"
date: 2026-09-25 08:08:00 +0200
categories: [PQC]
tags: [snova, multivariate-cryptography, key-recovery, lpn]
link: https://eprint.iacr.org/2026/2154
byline: "Ward Beullens and Basil Hess (IACR ePrint 2026/2154, Sep 22 2026)"
description: "A subtle sampling bias in Round-3 SNOVA leaks enough secret-key information to recover keys for several parameter sets using millions of signatures."
---

The authors show that the Round-3 SNOVA signer samples vinegar variables by reducing uniform byte strings modulo a power of q, and that the resulting bias leaks secret-key information for the six odd-characteristic alternative parameter sets. Even though the leakage is small, with the most leaky variables leaking at most 0.086 bits of information, it still enables efficient key-recovery attacks that the authors demonstrate in practice. Key recovery becomes a q-ary LPN problem of dimension o times l with a known, full-support error distribution, and a naive algorithm already needs far fewer operations than the claimed security level for the six affected parameter sets. Using standard LPN machinery, BKW reduction with Fourier hypothesis testing, the authors recover the secret key for four parameter sets using between 9 and 180 million signatures and at most 16 minutes of wall-clock time. Sampling the vinegar variables uniformly instead would prevent the attack entirely.
