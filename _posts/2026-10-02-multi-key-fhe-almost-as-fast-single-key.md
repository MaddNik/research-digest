---
title: "Multi-Key FHE Almost as Fast as Single-Key FHE"
date: 2026-10-02 08:17:00 +0200
categories: [FHE]
tags: [multi-key-fhe, gsw, bfv, key-aggregation]
link: https://eprint.iacr.org/2026/2195
byline: "Abtin Afshar and Rishab Goyal (IACR ePrint 2026/2195, Sep 26 2026)"
description: "A new multi-key FHE construction makes homomorphic evaluation cost independent of the number of users for the first time, inserting a public preprocessing step between encryption and evaluation."
---

Multi-key fully homomorphic encryption lets a circuit be evaluated over ciphertexts encrypted under independently generated keys, but known constructions expand every ciphertext under the concatenation of all participating secret keys, so both ciphertext size and per-gate running time grow with the number of users N, something Lopez-Alt, Tromer, and Vaikuntanathan asked be avoided when they introduced MKFHE over a decade ago. The authors construct the first MKFHE scheme whose homomorphic evaluation cost asymptotically matches single-key FHE, while users still generate keys and encrypt independently and the participating set is chosen only after encryption, by inserting a public, deterministic, non-interactive preprocessing phase between encryption and evaluation that aggregates the selected public keys and converts each independently encrypted input into a short single-key ciphertext under a virtual key equal to the sum of participating secret keys. Evaluation then runs on ordinary single-key ciphertexts, so every wire ciphertext, every gate, and the decryptable output become independent of N. The authors give two instantiations, a leveled GSW-based scheme from standard LWE and a leveled BFV-based scheme from circular Ring-LWE, both retaining single-round distributed decryption with statistically simulatable partial decryptions even though the published key material still grows with N. A Go implementation of the ring-based construction shows multiplication 275.13 and 45.50 times faster than the CDKS and KKLSS baselines for 32 users, with ciphertexts 16.5 times smaller than both.
