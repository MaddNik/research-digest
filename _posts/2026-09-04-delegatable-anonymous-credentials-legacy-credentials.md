---
title: "Delegatable Anonymous Credentials from Legacy Credentials using Recursive zk-SNARKs"
date: 2026-09-04 08:22:00 +0200
categories: [Cryptography]
tags: [anonymous-credentials, zk-snarks, ecdsa, delegation]
link: https://eprint.iacr.org/2026/1855
byline: "Leandro Rometsch et al. (IACR ePrint 2026/1855, Sep 1 2026)"
description: "The first delegatable anonymous credential scheme built directly on legacy ECDSA-signed credentials such as JWTs uses recursive Plonky2 SNARKs to give constant-size, fully unlinkable credentials at every delegation depth."
---

Digital identity systems like the European Digital Identity Wallet typically rely on standardized curves and signature schemes such as ECDSA that are incompatible with the pairing-based primitives underlying most anonymous credential constructions, and while recent work retrofits anonymous-credential properties onto such legacy credentials via zero-knowledge proofs without issuer-side changes, none of it supports delegation, the ability for a user to pass on a restricted credential derived from their own while every party in the delegation chain keeps full anonymity. This paper presents the first delegatable anonymous credential (DAC) scheme built directly on top of legacy credentials, requiring no changes to issuance infrastructure and yielding constant-size credentials regardless of delegation depth, with full unlinkability along the chain and selective attribute disclosure at every level. The scheme is instantiated for JSON Web Tokens signed with ECDSA, using Plonky2 as the recursive proving backend, and contributes a secure in-circuit JWT parser that closes vulnerabilities found in prior work plus a Plonky2 extension for cyclic recursion with per-step zero-knowledge. At 64 attributes, delegation takes 1.2 seconds and verification only 3.3 milliseconds, with constant proof size across all delegation levels.
