---
title: "SPECTER: Covert Data Exfiltration from Air-Gapped Systems via USB Power Modulation"
date: 2026-10-23 08:33:00 +0200
categories: [Hardware Security]
tags: [covert-channel, air-gapped-systems, usb, exfiltration]
link: https://arxiv.org/abs/2610.28401
byline: "Hyeongjun Choi et al. (arXiv:2610.28401, Oct 20 2026)"
description: "SPECTER demonstrates a post-compromise covert channel that exfiltrates data from air-gapped systems by modulating USB power-management states, recoverable via smartphone charging indicators, visible peripheral behavior, or near-field RF reception."
---

The authors present SPECTER, a post-compromise covert channel that uses host-side USB power control to exfiltrate information from air-gapped and network-segregated systems. A transmitter with administrative privileges encodes bits through USB power-management or device-state operations rather than placing the payload in USB data transfers, and the resulting signals can be recovered through three alternative receiver paths based on smartphone charging states, visible peripheral behavior, and near-field RF activity. Experiments on Windows 10 and Ubuntu 22.04 demonstrate the channel on commodity hardware, achieving charging-state signaling at 0.2 to 0.25 bits per second across Android and iOS devices and peripheral-state signaling at 1.0 bit per second using a USB mouse on Windows, with RF reception demonstrated using a software-defined radio and a loop antenna in direct contact with the USB cable. The authors note that channel availability and observable side effects depend on host configuration, connected device, and receiver path, and they argue the results motivate treating USB power-management and device-state events as security-relevant telemetry for low-rate exfiltration of short secrets.
