---
title: "CPU-Auth: Device Fingerprinting for Authentication via DVFS Side-Channel"
date: 2026-10-09 08:37:00 +0200
categories: [Hardware Security]
tags: [device-fingerprinting, dvfs, side-channel]
link: https://arxiv.org/abs/2610.10766
byline: "Ryan Swift (arXiv:2610.10766, Oct 7 2026)"
description: "CPU-Auth turns remotely measurable variations in a device's Dynamic Voltage and Frequency Scaling behavior, observed from within a browser, into a hardware-based authentication fingerprint."
---

Weak secondary authentication factors such as SMS codes, biometrics, and third-party tokens each carry notable flaws, including insecurity, reliance on sensitive personal data, or dependence on external providers. This work explores CPU-Auth, an authentication mechanism based on unique variations in the physical characteristics of a device's CPU, specifically the behavior of its Dynamic Voltage and Frequency Scaling (DVFS) governor, which can be measured remotely from within a browser. By leveraging these unique CPU properties, the authors establish a hardware-based device fingerprint usable as an authentication factor. The approach is evaluated on over 50,000 data traces using both distance-based and deep learning methods, as part of a larger research project whose results reported here reflect only this group's contribution.
