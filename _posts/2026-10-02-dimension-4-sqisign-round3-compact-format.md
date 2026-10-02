---
title: "Dimension-4 SQIsign at Round-3 Parameters: Sizes and Costs of the Compact Format"
date: 2026-10-02 08:13:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-cryptography, theta-model, rust-implementation]
link: https://eprint.iacr.org/2026/2221
byline: "Dustin Ray (IACR ePrint 2026/2221, Sep 26 2026)"
description: "Porting SQIsignHD's dimension-4 response to SQIsign's round-3 primes yields a 226-byte key-plus-signature combination, the smallest the author is aware of among isogeny or post-quantum signature schemes at those parameters."
---

SQIsign holds the smallest known combined key-and-signature size among post-quantum signatures, but its dimension-2 signature carries an auxiliary curve whose only purpose is making the response computable in dimension 2, a curve that SQIsignHD's dimension-4 response avoids entirely. The author ports this dimension-4 construction to the round-3 SQIsign primes, which replaced the round-2 primes in September 2026 after attacks by Wesolowski and others, implementing it in a Rust port of the SQIsign reference code and measuring it alongside the reference's own assembly build in one session. At NIST level I, the dimension-4 signature comes to 142 bytes against 200 bytes for the specification's format, with an 84-byte public key, giving 226 bytes for key and signature together, which the author describes as the smallest level-I combination known among isogeny schemes and post-quantum signatures alike at parameters that survive those attacks. The price is verification cost: the dimension-4 verifier runs 9.9 times slower than the dimension-2 verifier of the same code, 120.3 against 12.2 megacycles. Because the dimension-4 parameters published with SQIsignHD were derived for its authors' own primes, the paper states explicitly which parameter choices are SQIsignHD's and which are newly derived for the round-3 primes.
