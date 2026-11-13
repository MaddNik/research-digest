---
title: "Delegatable Keyed-Verification Anonymous Credentials"
date: 2026-11-13 08:26:00 +0200
categories: [Cryptography]
tags: [anonymous-credentials, delegation, pairing-free]
link: https://eprint.iacr.org/2026/2860
byline: "Omid Mirzamohammadi et al. (IACR ePrint 2026/2860, Nov 10 2026)"
description: "The paper introduces the first delegatable keyed-verification anonymous credentials, with two pairing-free constructions that let users delegate a restricted version of their credential to another user."
---

Keyed-verification anonymous credentials, or KVACs, are a variant of anonymous credentials where the issuer and verifier are the same entity or mutually trusted entities, which lets them avoid some practical burdens of publicly verifiable anonymous credentials, such as requiring bilinear pairings, making them more practical in certain settings. Delegation of credentials is a powerful feature that lets a user holding a credential delegate a restricted version of it to another user, and this paper proposes the first delegatable keyed-verification anonymous credentials, or DKVAC. The authors provide formal definitions of DKVAC, design two pairing-free DKVAC constructions with delegation capability, prove them secure, and demonstrate their practicality with implementation benchmarks. The two constructions present different trade-offs between expressiveness and performance.
