---
title: "Rethinking Zero-Knowledge TLS: Proof of Protocol Execution and the Reclaim Protocol"
date: 2026-10-02 08:29:00 +0200
categories: [Cryptography]
tags: [zktls, zero-knowledge, universal-composability, authenticated-encryption]
link: https://eprint.iacr.org/2026/2187
byline: "Andrey Bozhko and Kirill Kutsenok (IACR ePrint 2026/2187, Sep 26 2026)"
description: "A new transport-agnostic security definition for zkTLS, together with the Reclaim Protocol that realizes it, attests to a 1.2 megabyte web response in 7.28 seconds on a lower-mid-range phone."
---

In a zkTLS protocol, a user proves to a third party some property of data obtained from an online service over TLS without revealing anything beyond that property, but every existing scheme comes with its own bespoke security model, so the schemes are never proven secure against one common definition. The authors trace this to a level mismatch: existing models are stated at the level of TLS itself and so reflect how each construction happens to handle it, even though TLS is only the transport and a zkTLS proof is really about the application-layer protocol running over it. They introduce the first transport-agnostic security model for zkTLS, stated purely at the application layer and naming neither TLS nor any particular construction, calling the resulting notion Zero-Knowledge Proof of Protocol Execution, which captures what it means for a party that executed an arbitrary two-party protocol with a counterparty to prove in zero knowledge that its private input and the reply it received satisfy a chosen property and that the reply genuinely came from a real execution rather than being fabricated. They formalize this as a Universal Composability ideal functionality, then introduce the Reclaim Protocol, a zkTLS scheme that realizes it under a deployment-aligned trust model and already underlies a production system, built on a new three-party authenticated-encryption primitive called Distributed-AEAD. On a lower-mid-range phone, Reclaim attests to a 1200 kilobyte response in 7.28 seconds, two orders of magnitude beyond any response size previously benchmarked for zkTLS.
