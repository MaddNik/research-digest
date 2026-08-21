---
title: "DTRU: A Versatile, Compact, Simple, and Robust NTRU KEM with Double E8 Encoding"
date: 2026-08-21 08:10:00 +0200
categories: [PQC]
tags: [ntru, kem, chinese-standardization, lattice-encoding]
link: https://eprint.iacr.org/2026/1701
byline: "Hengchuan Zou et al. (IACR ePrint 2026/1701, Aug 16 2026)"
description: "A new NTRU-based KEM using double E8 lattice-code encoding, designed to meet China's 2025 post-quantum cryptography standardization requirements."
---

DTRU is presented as a lattice-based key encapsulation mechanism motivated by China's 2025 cryptographic standardization mandate for post-quantum schemes. Its central technique is described as double E8 encoding, which builds 16-dimensional lattice codes from the E8 lattice with low decoding complexity. The scheme is designed to support multiple underlying ring structures, including power-of-two cyclotomic rings and rings based on large-Galois-group prime-degree fields, so that it can meet 128-bit, 256-bit, and 512-bit security targets. The authors emphasize simplicity of implementation for resource-constrained devices and avoid additional coefficient compression steps used in some competing schemes. They report bandwidth improvements of 49 to 52 percent over NTRU-HRSS and claim better size and speed than Kyber across the platforms tested.
