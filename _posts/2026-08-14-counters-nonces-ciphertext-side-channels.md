---
title: "Counters and Nonces for Mitigating Ciphertext Side Channels"
date: 2026-08-14 08:28:00 +0200
categories: [Hardware Security]
tags: [ciphertext-side-channel, memory-encryption, confidential-computing]
link: https://eprint.iacr.org/2026/1632
byline: "Moritz Peters et al. (IACR ePrint 2026/1632, Aug 7 2026)"
description: "Storing small random nonces or counters in spare ECC memory bits closes a known ciphertext side channel in deterministic memory encryption used by systems like AMD SEV, at about 2 percent overhead."
---

Deterministic memory encryption, as used in confidential-computing systems such as AMD SEV, is vulnerable to a known ciphertext side channel where an attacker who can observe changes in encrypted memory over time can recover sensitive information without breaking the cipher itself. The authors propose storing small random nonces or counters in spare ECC memory bits to add freshness to each encryption, closing this channel. Their design offers several operating points trading security guarantees against performance overhead, with a baseline protection level achievable using small random nonces. The scheme also integrates with memory integrity and tagging mechanisms already present in these systems. Reported overall performance overhead is approximately 2 percent, which the authors argue makes the mitigation practical for real deployments.
