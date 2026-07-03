---
title: "A Differentiated Approach for Post-Quantum DNSSEC"
date: 2026-07-03 08:11:00 +0200
categories: [PQC]
tags: [dnssec, deployment, uov, hybrid-schemes]
link: https://eprint.iacr.org/2026/1332
byline: "Espie et al. (IACR ePrint 2026/1332, Sun 28 Jun 2026)"
description: "Assigning different post-quantum signature algorithms to DNSSEC's zone-signing and key-signing key roles expands which PQC schemes can actually be deployed within DNS size limits."
---

Post-quantum signature algorithms challenge DNSSEC migration because their larger keys and signatures exceed DNS-over-UDP transport limits, forcing TCP fallback even for relatively compact schemes. The paper proposes differentiated algorithm selection, using distinct signature algorithms for the Zone Signing Key and Key Signing Key roles, which the authors say expands the space of deployable configurations beyond what a single undifferentiated algorithm choice allows. As an example, they note that UOV, despite having 128-byte signatures, has 43 kilobyte keys that push DNSKEY responses over the 64 kilobyte DNS limit under undifferentiated selection, but becomes viable when paired with a compact-key KSK. The paper also evaluates hybrid post-quantum and traditional schemes via signature concatenation in a single RRSIG record. Using a containerized testbed validated against AFNIC's .fr TLD data covering 4.2 million domains, the authors measure response sizes, resolution latency, TCP fallback rates, and signing performance across 18 configurations, reporting 1.28 to 1.52 times latency overhead for differentiated configurations relative to classical ECDSA, and 7 to 19 percent overhead for hybrid concatenation.
