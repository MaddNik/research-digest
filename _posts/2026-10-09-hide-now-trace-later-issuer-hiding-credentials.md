---
title: "Hide Now, Trace Later: Retrospective Attribution in Issuer-Hiding Credentials"
date: 2026-10-09 08:25:00 +0200
categories: [Cryptography]
tags: [anonymous-credentials, accountability, pairing-based-cryptography]
link: https://eprint.iacr.org/2026/2396
byline: "Stephan Krenn et al. (IACR ePrint 2026/2396, Oct 7 2026)"
description: "A new issuer-inspection mechanism lets an authority retrospectively single out credential presentations from a compromised issuer and time period without breaking privacy for other issuers."
---

Attribute-based credentials allow privacy-preserving authentication by proving statements about certified attributes without revealing extra information, but the verification process still reveals the issuer's identity, which can leak contextual information such as a user's nationality. Issuer-hiding credential schemes conceal the issuer during verification, but this creates an accountability gap: if an issuer is compromised, previously accepted presentations from that issuer cannot be singled out without a serious privacy violation or a heavy burden on a central inspection authority. The authors propose an issuer-inspection mechanism in which an inspection authority releases keys that let verifiers locally identify presentations from a specific compromised issuer and a defined time period, without affecting other issuers or earlier periods. They formalize the syntax and security requirements for this issuer-inspection functionality, give a generic construction from standard building blocks, and present a concrete pairing-based instantiation using Groth's randomizable structure-preserving signatures, Schnorr-style proofs, and an adaptation of Gentry's anonymous identity-based encryption, with a cost analysis indicating the scheme remains practical for realistic parameters.
