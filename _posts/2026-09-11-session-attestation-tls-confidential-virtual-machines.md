---
title: "Session Attestation for Unmodified TLS Services in Confidential Virtual Machines"
date: 2026-09-11 08:32:00 +0200
categories: [Hardware Security]
tags: [confidential-computing, remote-attestation, tls, amd-sev]
link: https://arxiv.org/abs/2609.09668
byline: "Qi Gu et al. (arXiv:2609.09668, Sep 9 2026)"
description: "SessionLatch adds TEE session attestation to unmodified TLS services running in confidential virtual machines by observing the server's ephemeral public key, cutting short-upload latency by over 23 percent compared to a prior proxy-based approach."
---

Confidential virtual machines make it easy to move existing services into trusted execution environments, but attesting their network connections usually requires modifying applications, TLS implementations, or certificates. The authors present SessionLatch, which provides session attestation while preserving the application, TLS implementation, and certificates unchanged, based on the insight that a trusted observation of the server's locally generated ephemeral public key, combined with standard TLS key confirmation, establishes the TEE endpoint guarantee without accessing TLS secrets. The attestation logic moves into the operating system: a temporary latch holds client-encrypted records while evidence exchange overlaps the application's TLS handshake, then removes itself after verification, and the same construction supports mutual attestation by overlapping evidence generation at both endpoints. Implemented for Linux and Windows and evaluated with real Hygon CSV attestation, SessionLatch reduces short-upload mean latency by 63.1 percent and 23.0 percent relative to the prior TNG proxy approach in interleaved Linux and Windows experiments.
