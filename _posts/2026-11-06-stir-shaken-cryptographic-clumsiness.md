---
title: "STIR/SHAKEN: A Cocktail of Cryptographic Clumsiness"
date: 2026-11-06 08:21:00 +0200
categories: [Cryptography]
tags: [stir-shaken, telephony-security, pki, call-authentication]
link: https://eprint.iacr.org/2026/2772
byline: "Josh Brown, Matthew Hardeman, and Paul Grubbs (IACR ePrint 2026/2772, Nov 4 2026)"
description: "A security and privacy analysis of the US telephone authentication standard STIR/SHAKEN finds a noncompliant certificate PKI, a header-malleability flaw, and large-scale new metadata leakage."
---

STIR/SHAKEN is the cryptographic suite mandated by the US government in 2019 to combat caller-ID spoofing and fraudulent robocalls, in which providers sign assertions about caller identity and metadata in call headers. This paper asks whether STIR/SHAKEN meets its security goals and at what cost, finding that a year of observed production certificates shows a PKI riddled with noncompliance, with nearly half of valid certificates violating the specification, that a provider can block later verification by taking its certificate offline, and that a header-malleability flaw, verified in real test calls, can make a spoofed caller ID display as verified on some phones. The deployment has also created new privacy harms: signed call metadata is now cryptographically non-repudiable proof that a call took place, and because roughly half of the 29 surveyed providers outsource signing and verification to a handful of dominant vendors, sensitive call metadata leaks to off-path third parties, one of which was later acquired by a major US credit bureau. The authors propose fixes including adopting certificate transparency for the PKI, a backwards-compatible key-discovery mechanism using SIP error messages, and replacing STIR/SHAKEN's signatures with asymmetric message franking, for which they design the first blind signing protocol to keep metadata deniable even from outsourced signers.
