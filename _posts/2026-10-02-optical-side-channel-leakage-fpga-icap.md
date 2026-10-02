---
title: "The Achilles' Heel of Partial Reconfiguration: Optical Side-Channel Leakage on the 7-Series ICAP"
date: 2026-10-02 08:34:00 +0200
categories: [Hardware Security]
tags: [fpga-security, optical-probing, bitstream-encryption, partial-reconfiguration]
link: https://arxiv.org/abs/2610.01736
byline: "Antonio Saavedra et al. (arXiv:2610.01736, Oct 1 2026, DSD 2026)"
description: "Electro-optical probing of an AMD 7-Series FPGA's internal ICAP bus extracts plaintext configuration data during dynamic reconfiguration, defeating an AMD-proposed asymmetric bitstream encryption scheme."
---

Major FPGA manufacturers have added bitstream encryption to protect sensitive configuration data, but the authors note that for the most widely used FPGA families, several attacks against the unpatchable protection schemes hard-wired into these devices can bypass or fully break them, which is why patchable schemes are desirable. The paper presents a proof-of-concept implementation of an AMD-proposed asymmetric-key encryption scheme for bitstream protection on 7-Series FPGAs that uses partial reconfiguration from the programmable logic, analyzing its security implications and hardware overhead. The authors then propose and demonstrate an optical side-channel attack that recovers plaintext configuration data during the dynamic reconfiguration process, using photon emission microscopy and electro-optical probing to first locate and then contactlessly extract plaintext data from the ICAP interface that internally connects the programmable logic to the configuration logic. Having located the ICAP buses on an AMD XC7A200T device, they show the data on those buses can be extracted with electro-optical probing, and argue that even advanced encryption schemes built on partial reconfiguration and custom cryptographic engines remain vulnerable to optical attacks because reconfiguration is only possible through hard-wired, vulnerable configuration interfaces. The work is accepted for publication at the 29th Euromicro Conference on Digital System Design (DSD 2026).
