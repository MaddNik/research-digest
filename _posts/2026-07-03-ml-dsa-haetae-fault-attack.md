---
title: "Public Coefficient Matters: A Practical Differential Fault Attack on ML-DSA and HAETAE"
date: 2026-07-03 08:26:00 +0200
categories: [Hardware Security]
tags: [fault-injection, ml-dsa, haetae, side-channel]
link: https://eprint.iacr.org/2026/1344
byline: "Shin et al. (IACR ePrint 2026/1344, Tue 30 Jun 2026)"
description: "A single-fault attack on the challenge sampling step of ML-DSA and HAETAE recovers the secret key well enough to forge signatures."
---

The paper targets the challenge sampling procedure of deterministic ML-DSA, the NIST-standardized signature scheme, and HAETAE, a KpqC-selected scheme, arguing this step is an overlooked practical attack surface compared to prior fault attacks that targeted signing-time intermediate values. The authors show that a single faulted signature suffices to recover the secret key needed to forge signatures, and report this as the first fault attack that achieves secret-key recovery on HAETAE. Notably, their ML-DSA attack model does not require direct access to faulted challenge values; instead it identifies intended fault injections using only public information, distinguishing them from unintended fault outcomes. Both simulation and practical fault injection were used for evaluation, reaching a 100 percent identification rate for intended faults, and the authors also propose a countermeasure for the vulnerability they identify.
