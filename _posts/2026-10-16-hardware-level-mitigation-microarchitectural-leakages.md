---
title: "Hardware-Level Mitigation of Micro-Architectural Leakages in Embedded Processors"
date: 2026-10-16 08:36:00 +0200
categories: [Hardware Security]
tags: [micro-architectural-leakage, masking, rtl-design, fpga]
link: https://eprint.iacr.org/2026/2478
byline: "Niels Wieser et al. (IACR ePrint 2026/2478, Oct 14 2026, TCHES 2027)"
description: "Register-transfer-level changes to a general-purpose processor remove the hardware root causes of micro-architectural leakage, letting masked cryptographic software run securely without security-aware compilers."
---

Cryptographic software is essential for meeting fast-evolving security requirements despite running slower than dedicated hardware accelerators, but side-channel analysis complicates its secure execution because the masking countermeasure's provable security guarantees are often undermined by the processor's micro-architecture. Prior responses have adapted formal adversary models to account for micro-architectural leakage under generic but overly conservative hardware assumptions, which forces compilers to produce less performant software, or have assumed a precisely specified hardware leakage behavior in a hardware-software co-design that reduces but does not eliminate the overhead. This work instead aims to eliminate micro-architectural leakage at its source, proposing architectural changes to general-purpose processors at the register-transfer level that remove the root causes of such leakage. The authors formally prove the security of each countermeasure individually, integrate them into the Ibex processor, and evaluate the whole design through tool-assisted leakage assessment of the full netlist plus physical experiments on an FPGA, showing that masked software can run securely under the Robust but Relaxed d-probing model without complex security-aware compilers or hardware-specific software workarounds. The work is published in TCHES 2027.
