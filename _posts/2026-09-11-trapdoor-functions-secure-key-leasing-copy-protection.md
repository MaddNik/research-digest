---
title: "Trapdoor Functions with Secure Key Leasing and Copy Protection"
date: 2026-09-11 08:21:00 +0200
categories: [Cryptography]
tags: [trapdoor-functions, quantum-cryptography, copy-protection, key-leasing]
link: https://eprint.iacr.org/2026/1913
byline: "Fuyuki Kitagawa et al. (IACR ePrint 2026/1913, Sep 7 2026)"
description: "New constructions bring trapdoor functions into the quantum unclonable-cryptography setting, enabling secure key leasing and copy protection, and yielding encryption schemes with reusable quantum decryption keys."
---

Inspired by the no-cloning theorem, quantum cryptographic primitives with unclonable functionality, such as secure key leasing and copy protection, have attracted significant attention, but trapdoor functions, a fundamental public-key primitive, had not been extensively studied in these settings. The authors initiate this study by defining trapdoor functions with secure key leasing (TDF-SKL), which support leasing and deleting quantum trapdoors, giving a construction without a domain sampler based on the LWE assumption and one with a domain sampler based on any standard public-key encryption scheme combined with hinting pseudorandom generators. They also define trapdoor functions with copy protection (TDF-CP), where the inversion functionality is copy protected by a quantum trapdoor, and construct one from indistinguishability obfuscation and LWE. As an application, the authors build public-key encryption with secure key leasing and single-decryptor encryption schemes whose quantum decryption keys remain reusable even after decrypting arbitrary ciphertexts, fixing a vulnerability in prior constructions where such keys could be destroyed by maliciously chosen ciphertexts.
