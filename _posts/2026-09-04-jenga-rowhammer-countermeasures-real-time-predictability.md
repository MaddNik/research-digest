---
title: "JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability"
date: 2026-09-04 08:29:00 +0200
categories: [Hardware Security]
tags: [rowhammer, ddr5, real-time-systems, wcet]
link: https://arxiv.org/abs/2609.01077
byline: "Valentin Abgrall et al. (arXiv:2609.01077, Sep 1 2026)"
description: "JENGA shows an attacker-controlled task can manipulate a DDR5 Per-Row-Activation-Counter RowHammer countermeasure to delay a victim real-time task up to 200 percent beyond its expected worst-case execution time."
---

Safety-critical real-time systems must satisfy both time predictability, typically verified through worst-case execution time (WCET) analysis, and security, but DRAM-based platforms are increasingly sensitive to the RowHammer read-disturbance vulnerability, which has driven adoption of hardware and software countermeasures whose impact is usually evaluated only in terms of average-case performance rather than the worst-case behavior that matters for real-time systems. Using the Per-Row-Activation-Counter (PRAC) countermeasure standardized for recent DDR5 memories as a case study, the authors show that it can introduce significant timing variations, and they introduce JENGA, an attack in which an attacker-controlled task manipulates the internal state of the RowHammer countermeasure to increase a victim real-time task's execution time beyond its expected WCET. Implemented and evaluated in a gem5 and Ramulator 2.0 simulation environment against TACLeBench workloads, JENGA is shown to delay tasks by up to 200 percent of their WCET, invalidating the timing-safety assumptions those systems rely on. To address this, the authors derive a safe analytical bound that accounts for mitigation-induced delays in WCET analysis for DRAM systems protected by hardware counter-based countermeasures such as PRAC-N, and the paper is set to appear at the 47th IEEE Real-Time Systems Symposium (RTSS) 2026.
