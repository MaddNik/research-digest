---
title: "Phase-Hiding Programmable Bootstrapping with Online Client Assistance"
date: 2026-11-20 08:14:00 +0200
categories: [FHE]
tags: [tfhe, programmable-bootstrapping, client-assisted-computation, private-lookup-tables]
link: https://eprint.iacr.org/2026/2892
byline: "Xingke Chai (IACR ePrint 2026/2892, Nov 14 2026)"
description: "A client-assisted phase-hiding bootstrapping protocol replaces TFHE's blind rotation with a precomputed phase-token lookup, cutting measured refresh time substantially relative to TFHE-rs."
---

Programmable bootstrapping in TFHE normally uses a bootstrapping key to control a sequence of external products during blind rotation, which costs computation and introduces and propagates error. The author introduces Phase-Hiding Programmable Bootstrapping, in which the key-holding client precomputes single-use phase tokens encrypting randomly shifted monomials and assists the server online through phase sharing and a small garbled circuit that computes a masked rotation correction, letting the server align a token for lookup instead of running blind rotation driven by the bootstrapping key. Using the aligned monomial, the server evaluates private lookup tables and can retain ciphertexts for further computation while releasing only prescribed terminal plaintexts to the client. A projection independent of the table values reduces token preparation and transmission costs, and the paper derives numerical failure-probability bounds under a stated finite-precision model. On a four-bit workload matched to a TFHE-rs baseline, mean local refresh time with pre-core key switching drops from 18.392 milliseconds to 3.713 milliseconds, a 79.8 percent reduction, with estimated refresh-stage times 46.3 to 80.1 percent lower than the baseline across the examined modes and network scenarios.
