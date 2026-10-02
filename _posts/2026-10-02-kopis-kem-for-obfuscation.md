---
title: "Kopis: A KEM for Obfuscation"
date: 2026-10-02 08:32:00 +0200
categories: [Cryptography]
tags: [pake, mlwr, obfuscated-key-exchange, drop-in-replacement]
link: https://eprint.iacr.org/2026/2268
byline: "Andrea Basso and Michael Rosenberg (IACR ePrint 2026/2268, Sep 30 2026)"
description: "Kopis is a Module Learning-with-Rounding KEM whose public keys and ciphertexts already look like uniform bytestrings, making it a cleaner drop-in replacement for ML-KEM inside PAKE and obfuscated key exchange."
---

Password-authenticated key exchange and obfuscated key exchange protocols, used in settings from passport access control to Tor's censorship evasion, are typically built on a KEM whose public keys and ciphertexts get obfuscated on the wire by adding a random mask or applying an ideal cipher, and many post-quantum proposals plan to instantiate this with ML-KEM, NIST's standardized lattice-based KEM. The authors argue ML-KEM is a poor fit for these protocols because its algebraic structure means obfuscating its values requires custom, constant-time, standardized procedures for hash-to-vector, matrix expansion, serialization, and randomized ciphertext decompression, and no such procedures exist today. They observe that these barriers disappear if the KEM's algebraic structure is removed, that is, if ML-KEM is swapped for a KEM whose public keys and ciphertexts already look uniform as bytestrings. Kopis is their Module Learning-with-Rounding KEM with exactly that property, intended as a drop-in replacement for ML-KEM in size, speed, and security, and built nearly identically to Saber, a NIST PQC finalist, so it inherits Saber's years of cryptanalysis. The authors demonstrate Kopis's security properties for use in various PAKE and obfuscated-key-exchange schemes and provide a formally verified Rust implementation with portable, AVX2, and NEON backends plus a C implementation for Cortex-M4, benchmarking it as comparable to, and often faster than, the fastest known ML-KEM implementations.
