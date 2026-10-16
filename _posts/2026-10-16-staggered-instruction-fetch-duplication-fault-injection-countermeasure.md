---
title: "Staggered Instruction-Fetch Duplication: A Lightweight Processor-Level Countermeasure Against Fault Injection"
date: 2026-10-16 08:34:00 +0200
categories: [Hardware Security]
tags: [fault-injection, countermeasure, risc-v, fpga]
link: https://eprint.iacr.org/2026/2440
byline: "Shoei Nashimoto et al. (IACR ePrint 2026/2440, Oct 10 2026, ASP-DAC)"
description: "Staggered Instruction-Fetch Duplication detects fault injection attempts on an embedded RISC-V processor by fetching each instruction twice on a staggered schedule, without duplicating the whole processor."
---

Fault attacks exploit transient hardware faults to bypass software-level security checks in embedded processors, and while processor-level redundancy can detect such faults, duplicating the entire processor is too costly for resource-constrained devices. This paper proposes Staggered Instruction-Fetch Duplication, a lightweight countermeasure that fetches each instruction twice in consecutive cycles while fetching two different instructions in every fetch cycle, detecting inconsistent fetch results without full processor duplication, compiler support, or dedicated cryptographic hardware. The authors implement the technique on a custom RV32I processor and evaluate it on an Artix-7 FPGA under clock fault injection and electromagnetic fault injection, finding that it increases slice utilization by 15.0 percent and execution time by 16.3 percent while reducing the attack success rate from 0.86 percent to below 0.01 percent under clock fault injection and from 0.32 percent to 0.13 percent under electromagnetic fault injection. It also explicitly detects 73.18 percent of clock fault injection attempts and 11.44 percent of electromagnetic fault injection attempts, showing that many fault effects can be converted into explicit detections at low hardware cost. The work is published at ASP-DAC.
