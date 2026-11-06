---
title: "Shoot on (Core)Sight: Re-enabling Secure Debug on the RP2350 with Photon-Emission Microscopy and Laser Fault Injection"
date: 2026-11-06 08:28:00 +0200
categories: [Hardware Security]
tags: [fault-injection, laser-attack, secure-debug, microcontroller]
link: https://arxiv.org/abs/2611.06386
byline: "Antoine Plin (arXiv:2611.06386, Nov 4 2026)"
description: "Photon-emission microscopy guided laser fault injection re-enables secure debug access on the RP2350 microcontroller, recovering a 128-bit test secret after a rescue reset."
---

This paper demonstrates that fault-resistant storage of a security policy does not guarantee that the policy is enforced in a fault-resistant way. The authors target the RP2350A4 microcontroller, using differential photon-emission microscopy to narrow down the physical area for laser scanning and then laser fault injection to find two sites where precisely timed pulses set the DEBUGEN bits that enable Secure debug on core 1. An online attack sequence that relies only on Serial Wire Debug feedback restores sustained debug access after the fault, and following a rescue reset, the sequence successfully recovers a 128-bit test secret. The reset reloads the secret's runtime page lock from a stored policy that permits Secure reads and prevents user firmware from tightening that lock, so the vulnerability persists across resets. The work illustrates how photon-emission microscopy can be combined with laser fault injection to defeat secure debug mechanisms even when the underlying policy data itself is properly protected.
