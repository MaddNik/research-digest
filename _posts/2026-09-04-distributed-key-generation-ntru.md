---
title: "Distributed Key Generation for NTRU"
date: 2026-09-04 08:07:00 +0200
categories: [PQC]
tags: [ntru, threshold-encryption, distributed-key-generation, lattice-based]
link: https://eprint.iacr.org/2026/1854
byline: "Patrick Hough et al. (IACR ePrint 2026/1854, Sep 1 2026)"
description: "The first dedicated distributed key generation protocol for NTRU lets multiple parties jointly produce an NTRU public key with a multiplicatively shared secret key, enabling threshold NTRU encryption."
---

NTRU-based encryption has compact keys and ciphertexts and admits non-interactive distributed decryption, making it attractive for threshold encryption, threshold fully homomorphic encryption, threshold signatures, and electronic voting, but all known protocols assumed a trusted dealer holding the secret key. Because the public NTRU key is a nonlinear function of the secret, the distributed key generation techniques built for LWE-based schemes do not apply, and generic multiparty computation is too expensive. The authors present the first dedicated distributed key generation protocol for NTRU, in which each party publishes an NTRU sample defining a joint public key with a multiplicatively shared secret key, and a multiplicative-to-additive conversion produces the additive sharing needed for non-interactive decryption. The protocol runs in a few rounds and is actively secure with abort, and its core multiplicative-to-additive conversion is instantiated with two efficient lattice-based constructions, one from additively homomorphic NTRU encryption and one from homomorphic secret sharing. The authors use the protocol to build and prove secure a threshold variant of NTRU-Encrypt with concrete parameters, and the paper is set to appear at CANS 2026.
