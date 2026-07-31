---
title: "SPARC: Automated Root-Cause Analysis of Pre-Silicon Power Side-Channel Leakage in the Processor Design Flow"
date: 2026-07-31 08:30:00 +0200
categories: [Hardware Security]
tags: [power-side-channel, pre-silicon-verification, risc-v]
link: https://arxiv.org/abs/2607.23218
byline: "Andrija Neskovic et al. (arXiv:2607.23218, Jul 25 2026)"
description: "SPARC is an automated pre-silicon framework using macro-cell-level information flow tracking to detect power side-channel leakage in processor RTL and trace it to specific hardware signals and software instructions."
---

Power side-channel leakage arises from architectural and microarchitectural artifacts in a processor and threatens the confidentiality of cryptographic software running on it, making pre-silicon evaluation important before a chip is fabricated. Prior frameworks either scale poorly in simulation or cannot attribute detected leakage back to the responsible hardware signals and software instructions, limiting root-cause analysis. SPARC addresses this with macro-cell-level information flow tracking augmented by shadow logic that tags switching activity tied to secret-dependent data, then applies statistical leakage tests to isolated activity while mapping flagged signals back to the software instructions that caused them. The authors validate SPARC on multiple open-source RISC-V CPUs, 32-bit and 64-bit, in-order and out-of-order, running masked and unmasked AES and ML-KEM Kyber-512 workloads. SPARC recovers previously known leakage sources as a sanity check, identifies new microarchitectural leakage sources, and achieves an 8 times per-trace simulation speedup over prior comparable approaches.
