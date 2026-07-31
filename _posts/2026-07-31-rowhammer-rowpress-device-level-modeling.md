---
title: "Demystifying DRAM Read Disturbance: Bridging the Gap Between Experimental Characterization and Device-Level Modeling of RowHammer and RowPress Phenomena"
date: 2026-07-31 08:25:00 +0200
categories: [Hardware Security]
tags: [rowhammer, dram-security, fault-modeling]
link: https://arxiv.org/abs/2607.28233
byline: "Haocong Luo et al. (arXiv:2607.28233, Jul 30 2026)"
description: "A device-level TCAD modeling study reconciles physical mechanisms of RowHammer and RowPress DRAM read-disturbance bitflips with prior experimental characterization results."
---

RowHammer and RowPress are DRAM read-disturbance phenomena where accessing one row causes unintended bitflips in other rows, a well-known basis for privilege-escalation and cross-tenant attacks. This paper identifies gaps between existing device-level physical models and empirical bitflip observations across three metrics: bitflip direction, bitflip count, and the minimum aggressor-row activation count that triggers first bitflips. The authors run a comprehensive set of TCAD simulations that reproduce experimentally observed phenomena and use the results to update the understood device-level error mechanisms. They also identify which simulation parameters most affect whether simulated results match real-chip characterization. The work is meant to ground future characterization methodologies and mitigation design for DRAM read disturbance.
