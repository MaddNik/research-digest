---
title: "Qlapoti+ and More: Optimizing Isogeny-based Signatures"
date: 2026-08-14 08:12:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-signatures, performance-optimization]
link: https://eprint.iacr.org/2026/1640
byline: "Yi-Fu Lai (IACR ePrint 2026/1640, Aug 8 2026)"
description: "New optimizations to the Qlapoti procedure underlying SQIsign-style isogeny signatures speed key generation and signing by roughly 1.5 to 4.5 times."
---

Qlapoti is a core procedure used in contemporary isogeny-based signature schemes such as the NIST Round 2 SQIsign candidate. This paper introduces optimization techniques for Qlapoti that accelerate the procedure by approximately 1.5 to 4.5 times, with the exact gain depending on the parameter set and implementation. The improvements apply across all NIST security levels for both key generation and signing operations in SQIsign. The author additionally develops specialized optimizations for the PRISM isogeny-based construction, showing comparable speedups at multiple security levels benchmarked on a Broadwell processor environment.
