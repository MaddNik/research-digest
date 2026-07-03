---
title: "LIB-TRAP: Standard Cell Library Hardware Trojan Risk Assessment and Prevention"
date: 2026-07-03 08:29:00 +0200
categories: [Hardware Security]
tags: [hardware-trojans, supply-chain-security, standard-cell-libraries, ic-design]
link: https://arxiv.org/abs/2607.01526
byline: "Dharavath et al. (arXiv:2607.01526, Wed 01 Jul 2026)"
description: "Standard cell libraries used in chip design and fabrication can themselves be maliciously modified to conceal hardware trojans from designers using normal design tools."
---

This work examines a supply-chain security risk at the foundational level of integrated circuit design, the standard cell libraries that define the basic logic building blocks used by every chip. The authors adopt a threat model in which the standard cells themselves are untrusted, and they show that malicious versions of these libraries can be constructed using established, ordinary design tools. They converted two existing libraries, a 32 nanometer SAED library and the Sky130 nanometer library, into compromised versions capable of hiding hardware trojans from circuit designers. To validate the risk, they synthesized three benchmark circuits, an AES-128 encryption core, an Ethernet controller, and a WISHBONE direct memory access engine, using both the legitimate and the compromised libraries across the two technology nodes. They then extracted design metrics such as cell count, circuit area, and power consumption parameters to assess how feasible it is to detect the tampering from these measurements alone.
