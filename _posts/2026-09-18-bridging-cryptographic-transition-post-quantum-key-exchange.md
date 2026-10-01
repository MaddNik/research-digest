---
title: "Bridging the Cryptographic Transition: A Unified Framework for Post-Quantum Key Exchange"
date: 2026-09-18 08:12:00 +0200
categories: [PQC]
tags: [key-exchange, migration, formal-security, provable-security]
link: https://eprint.iacr.org/2026/1992
byline: "Benjamin Dowling and Bhagya Wimalasiri (IACR ePrint 2026/1992, Sep 12 2026, ACM CCS 2026)"
description: "A new formally analyzed framework aims to ease the migration of classical Internet key exchange protocols to post-quantum counterparts as major vendors set aggressive PQC migration deadlines."
---

The authors note that Google has set a 2029 internal deadline for completing its post-quantum cryptography migration, ahead of the 2035 deadline set by NIST and the US federal government for deprecating classical public-key algorithms, citing faster than expected progress in quantum hardware, quantum error correction, and resource estimates for breaking current cryptographic schemes. This tightened timeline puts pressure on Internet protocols that still rely on classical key exchange primitives for secure communication. The paper constructs a unified, formally analyzed security framework intended to ease the migration of classical key exchange constructions to their post-quantum counterparts. The work is published as a major revision at ACM CCS 2026, positioning the framework as a tool for protocol designers navigating the classical-to-post-quantum transition under real migration deadlines.
