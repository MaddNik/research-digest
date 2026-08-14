---
title: "Adaptively Secure Threshold Decryption from LWE with Polynomial Modulus"
date: 2026-08-14 08:10:00 +0200
categories: [PQC]
tags: [threshold-decryption, lwe, noise-flooding, adaptive-security]
link: https://eprint.iacr.org/2026/1626
byline: "Yuxin Zhang et al. (IACR ePrint 2026/1626, Aug 6 2026)"
description: "Three new lattice-based threshold decryption schemes are the first to combine adaptive corruption security with a polynomial-size LWE modulus."
---

Threshold decryption lets multiple key-share holders jointly decrypt a ciphertext without any single holder learning the full key, but prior lattice-based constructions could not combine adaptive corruption security with a polynomial modulus. This paper resolves that open problem with three schemes: TD0 for adaptive CPA security in asynchronous settings, TD1 for adaptive CCA security with a bounded number of queries, and TD2 for synchronous settings relying on a random oracle. The core technical tool is a refined polynomial noise-flooding technique combined with secret sharing. The authors state this is the first work to achieve non-interactive, adaptively CCA-secure, polynomial-modulus lattice-based threshold decryption at once, strengthening guarantees against adversaries who can adaptively corrupt parties during protocol execution.
