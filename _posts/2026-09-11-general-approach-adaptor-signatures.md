---
title: "A General Approach to Adaptor Signatures"
date: 2026-09-11 08:22:00 +0200
categories: [Cryptography]
tags: [adaptor-signatures, blockchain, homomorphic-encryption, fair-exchange]
link: https://eprint.iacr.org/2026/1889
byline: "Nico Dottling et al. (IACR ePrint 2026/1889, Sep 4 2026)"
description: "A new framework builds adaptor signatures for arbitrary NP relations and a broad range of signature schemes, extending the previously narrow reach of adaptor signatures used for blockchain atomic swaps."
---

Adaptor signatures are a contract-minimal mechanism for fair exchange on blockchains, enabling atomic swaps and conditional payments, but existing schemes are limited to narrow classes of NP relations, such as discrete logarithm secrets, and specific signature schemes. The authors present a framework supporting arbitrary NP relations and a broad range of signature schemes, via two general compilers. The first lifts adaptor signatures from structured languages to general NP languages using degree-2 homomorphic encryption, and the second transforms any signature scheme with a subliminal channel, such as Schnorr, ECDSA, CL, BBS, or salted BLS and RSA, into an adaptor signature for general NP languages using circuit-private fully homomorphic encryption. Both constructions achieve a new property the authors call statement truth privacy, ensuring a buyer learns nothing about the underlying statement, not even whether it is true, unless the exchange protocol completes successfully.
