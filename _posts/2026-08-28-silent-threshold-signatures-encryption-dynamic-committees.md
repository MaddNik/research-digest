---
title: "Practical Silent Threshold Signatures and Silent Threshold Encryption for Dynamic Committees"
date: 2026-08-28 08:23:00 +0200
categories: [Cryptography]
tags: [threshold-signatures, silent-setup, dynamic-committees, polynomial-commitments]
link: https://eprint.iacr.org/2026/1820
byline: "Yifei He et al. (IACR ePrint 2026/1820, Aug 27 2026)"
description: "New silent threshold signature and encryption schemes for dynamic committees make aggregation cost depend only on the small active committee size rather than the full system size N."
---

Silent threshold signatures and encryption enable threshold cryptography without an interactive distributed key generation phase, but modern systems like Ethereum rely on small, dynamically changing committees of size n much less than N for efficiency, and the only prior construction for this dynamic setting, Dyna-hinTS, still requires an aggregation time of O(N log N) per epoch. The authors redesign the Dyna-hinTS framework by replacing its Plonk-style SNARKs with linear pairing checks and a new polynomial commitment for representing the committee, reducing aggregation time to O(n log squared n), and introduce the first silent threshold encryption scheme for dynamic committees with matching efficiency. They also optimize the silent setup phase common to prior schemes, cutting each party's one-time hint generation cost from O(N squared) to O(N). In a Rust implementation with N equal to 2 to the 20th power and n equal to 2 to the 10th power, per-party hint generation takes 197 seconds and signature aggregation takes 0.153 seconds, more than 1900 times faster than Dyna-hinTS, while aggregated signature size, verification key size, and verification time remain constant. The work is published at ACM CCS 2026.
