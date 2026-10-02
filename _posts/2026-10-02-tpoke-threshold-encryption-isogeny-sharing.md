---
title: "TPOKÉ: Threshold Public-Key Encryption from POKÉ via Isogeny Sharing"
date: 2026-10-02 08:16:00 +0200
categories: [PQC]
tags: [isogeny-cryptography, threshold-encryption, poke, secret-sharing]
link: https://eprint.iacr.org/2026/2243
byline: "Toshiki Takatera, Hiroshi Onuki, and Tsuyoshi Takagi (IACR ePrint 2026/2243, Sep 28 2026)"
description: "Two new threshold variants of the POKÉ isogeny encryption scheme avoid repeating shared isogeny computations, roughly halving ciphertext size compared with running n independent POKÉ instances."
---

POKÉ, introduced by Basso and Maino, is one of the most efficient isogeny-based public-key encryption schemes, and the generic way to make it a (t,n)-threshold scheme is to run n independent POKÉ instances and secret-share the message, but this multiplies both public-key and ciphertext sizes by roughly n. The authors present S-TPOKÉ, a POKÉ-based threshold construction for any threshold from 1 to n, and Ch-TPOKÉ, an (n,n) variant that arranges the parties' secret isogenies differently, with both avoiding the repeated isogeny computation that otherwise appears in every independent POKÉ instance. Compared with the trivial construction, the schemes cut the number of degree-3-to-the-b isogenies computed during encryption from 2n to n plus 1 and roughly halve ciphertext size for large n. S-TPOKÉ, the main construction, has the dealer sample n independent secret isogenies while encryption samples one sender-side secret isogeny shared across the parties, and the authors prove it achieves SIM-CPA security under static corruption in the random oracle model from new S-C-POKE assumptions; Ch-TPOKÉ instead chains the parties' secret isogenies and achieves only the strictly weaker SIM-CPA security under static maximal corruption. The paper also gives asymptotic parameter choices for a target security level and closed-form expressions for public-key, ciphertext, and partial-decryption sizes.
