---
title: "Revisiting Simple Power Analysis of Polynomial Multiplication in the HQC Implementation"
date: 2026-09-11 08:10:00 +0200
categories: [PQC]
tags: [hqc, side-channel, power-analysis, code-based-cryptography]
link: https://eprint.iacr.org/2026/1906
byline: "Trevor Yap et al. (IACR ePrint 2026/1906, Sep 7 2026)"
description: "A simple power analysis attack still recovers secret bits from the updated bitwise schoolbook multiplication in the HQC reference implementation, despite it replacing an earlier vulnerable lookup-table design."
---

HQC is a code-based post-quantum key encapsulation mechanism recently selected for NIST standardization, making the security of its implementations important. The authors revisit the side-channel resistance of the latest HQC reference implementation, focusing on the polynomial multiplication routine used during decryption. While a prior simple power analysis (SPA) attack targeted a lookup-table-based multiplication, the updated implementation instead uses a bitwise schoolbook multiplication. The authors show that this updated schoolbook_mul function still shows clear, visually distinguishable power consumption variations that depend on secret data, allowing an attacker to recover individual bits of the secret polynomial. They propose a zero-cost mitigation that swaps operand roles so the mask computation depends only on public data, eliminating the leakage while preserving performance.
