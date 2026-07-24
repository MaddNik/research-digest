---
title: "Side-Channel Attacks Revisited - an Optimization Problem Perspective: Bootstrapping and Space Reduction"
date: 2026-07-24 08:24:00 +0200
categories: [Hardware Security]
tags: [masking, xor-leakage, profiled-attack, ascon]
link: https://eprint.iacr.org/2026/1468
byline: "Erez Tamir et al. (IACR ePrint 2026/1468, Jul 22 2026)"
description: "The paper shows that standalone XOR gates in masked hardware, long assumed benign, leak enough asymmetric information to collapse key guessing space in profiled side-channel attacks."
---

The authors introduce Feature Estimation based Attacks (FEbA), a profiling technique that exploits asymmetric leakage patterns from XOR gates. The attack targets the sharing and refreshing phases of masking based implementations, narrowing the guessing key space without needing access to intermediate values. It is demonstrated against ASCON, GIBBON, and ACE. The authors report reducing the entropy of a 32-bit key below 1 bit using up to 20,000 traces from a standalone XOR gate alone, or below 500 traces when intermediate values are also accessible.
