---
title: "More Salt, Please: A Simple Compiler for Post-Quantum Strong aPAKE"
date: 2026-11-13 08:14:00 +0200
categories: [PQC]
tags: [pake, password-authentication, precomputation-resistance]
link: https://eprint.iacr.org/2026/2798
byline: "William Riccardo Duro et al. (IACR ePrint 2026/2798, Nov 6 2026)"
description: "A new password-file ratchet adds precomputation resistance to existing PAKE-to-aPAKE compilers, yielding a ready-to-deploy post-quantum strong asymmetric PAKE without costly post-quantum oblivious pseudorandom functions."
---

Resistance to precomputation attacks is a central security goal in password-based cryptography because it drastically increases the runtime of brute-force attacks on breached password hashes, and strong asymmetric password-authenticated key exchange, or saPAKE, enforces this resistance and is already standardized by the IRTF and deployed at scale. The authors note that no practical, easy-to-deploy saPAKE yet withstands quantum attackers, since current constructions rely on rate-limiting tools such as oblivious pseudorandom functions, whose post-quantum versions are significantly more costly and complex than their discrete-log based counterparts. Starting from the known compilers from PAKE to aPAKE by Gentry-MacKenzie-Ramzan and by Liu-Lyu-Han, the authors propose a password file ratchet that adds precomputation resistance to these compilers by continuously updating the password file through a simple salted hash. Combined with existing practical post-quantum PAKEs, this yields a ready-to-deploy post-quantum strong aPAKE, at the cost of a server state that changes over time.
