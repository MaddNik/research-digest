---
title: "DUFT: Device-Unique Feedback Traversal for Entropy-Estimated Response Extraction and Mutual Authentication using SRAM PUFs"
date: 2026-11-13 08:33:00 +0200
categories: [Hardware Security]
tags: [puf, sram, authentication, embedded-devices]
link: https://arxiv.org/abs/2611.15958
byline: "Syed Talha Imam, Amna Zafar, Arslan Munir (arXiv:2611.15958, Nov 11 2026)"
description: "DUFT is a seed-based feedback mechanism that extends SRAM PUFs beyond simple key generation to a lightweight challenge-response authentication protocol for resource-constrained embedded devices."
---

Static random access memory (SRAM) physical unclonable functions are a promising technology for random number generation and key generation, but for challenge-response-based authentication they have been sidelined because of their limited challenge space. The authors develop a seed-based, round-iterated feedback mechanism called Device-Unique Feedback Traversal, or DUFT, in which the feedback chain is driven by a device's unstable and stable bit positions in its stability mask against the address, creating a unique traversal, with a device-key hashed from the unique SRAM-PUF array also folded into each round to keep the chain secret. By empirically estimating the physical SRAM source's entropy and error rate, DUFT calculates the number of feedback rounds needed to reach a target amount of min-entropy, reaching 128 bits of estimated min-entropy on the authors' reference hardware, with the number of rounds scaling directly with the measured source entropy so that security can be increased for weaker sources at the cost of running time. Using this feedback-traversal wrapper over SRAM PUFs to obtain a measured response, the authors propose an extremely lightweight authentication and key-encapsulation protocol for resource-constrained embedded devices, and they realize and evaluate DUFT end to end on physical IoT and embedded hardware, including a discrete-SRAM node pair running the complete protocol and an embedded-SRAM microcontroller running the mechanism alone.
