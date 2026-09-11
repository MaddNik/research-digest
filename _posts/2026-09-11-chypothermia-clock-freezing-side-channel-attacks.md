---
title: "Chypothermia: Clock Freezing for Static Side-channel Attacks"
date: 2026-09-11 08:26:00 +0200
categories: [Hardware Security]
tags: [static-side-channel, clock-freezing, fpga-security, root-of-trust]
link: https://arxiv.org/abs/2609.11442
byline: "Fatemeh Khojasteh Dana et al. (arXiv:2609.11442, Sep 10 2026)"
description: "Cooling a chip to cryogenic temperatures disables its clock and voltage sensors without any electrical tampering, letting an attack called Chypothermia halt the clock for static side-channel attacks while evading OpenTitan's clock-anomaly detection."
---

Static side-channel attacks exploit halted-clock conditions to extract secrets, and defenses typically monitor for abnormal clock behavior to trigger clearing of sensitive data. The authors show that exposing a chip to cryogenic temperatures interferes with the on-chip mixed-signal components responsible for signal sensing and generation, and use this to build Chypothermia, an attack that disables the target clock sensor, clock generation circuit, and voltage sensors without any electrical tampering, while preserving the secret data. Because cooling alone is slow and often insufficient against systems with thermal anomaly sensors, the authors combine Chypothermia with the previously published Chypnosis attack, showing the combination can halt the clock within a moderately low-temperature range while evading detection. They implement the attack on multiple FPGA and system-on-chip platforms, including OpenTitan's alert handler with its state-of-the-art clock sensor, demonstrating that it evades detection and prevents key zeroization, and they introduce and validate an FPGA-compatible self-heating sensor as a countermeasure.
