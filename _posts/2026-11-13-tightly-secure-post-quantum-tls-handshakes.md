---
title: "Tightly Secure and Modular Post-Quantum TLS Handshakes"
date: 2026-11-13 08:10:00 +0200
categories: [PQC]
tags: [tls, kemtls, tight-security, lwe]
link: https://eprint.iacr.org/2026/2864
byline: "Biming Zhou et al. (IACR ePrint 2026/2864, Nov 11 2026, ASIACRYPT 2026)"
description: "A new unified reduction framework gives the first almost-tightly secure constructions of post-quantum TLS 1.3 and KEMTLS under the LWE assumption."
---

In the post-quantum migration of the TLS 1.3 handshake, classical Diffie-Hellman key exchange is replaced with a post-quantum key encapsulation mechanism, and KEMTLS further replaces signature-based authentication with KEM-based authentication, but all existing analyses of these protocols incur at least quadratic reduction losses in the number of sessions. The authors present the first unified, tight, and modular reduction framework for post-quantum TLS 1.3 in the standard model and KEMTLS in the random oracle model. The framework tightly reduces the security of these protocols to three core components: the security of the underlying ephemeral KEM, the multi-user pseudorandom function security of HKDF for TLS 1.3, and either the signature scheme's unforgeability for TLS 1.3 or the static KEM's security for KEMTLS. The authors also establish the first concrete multi-user pseudorandom function bounds for HMAC and HKDF in the quantum-accessible random oracle model. Instantiating the framework with tightly secure LWE-based KEM and signature schemes yields the first almost-tightly secure constructions of post-quantum TLS 1.3 and KEMTLS under the LWE assumption, and the framework shows that a weaker security notion for the ephemeral KEM already suffices, enabling simpler instantiations. The paper appears as a minor revision of an IACR publication at ASIACRYPT 2026.
