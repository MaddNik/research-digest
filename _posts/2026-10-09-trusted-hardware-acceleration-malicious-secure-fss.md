---
title: "Trusted Hardware Acceleration for Malicious-Secure Function Secret Sharing"
date: 2026-10-09 08:35:00 +0200
categories: [Hardware Security]
tags: [function-secret-sharing, trusted-hardware, gpu-acceleration]
link: https://arxiv.org/abs/2610.04818
byline: "Yujie Xue et al. (arXiv:2610.04818, Oct 3 2026)"
description: "VIGOR-DFA upgrades a trusted GPU-integrated distributed function accelerator for function secret sharing from semi-honest to malicious security, cutting per-query authenticated material by tens of gigabytes."
---

Function secret sharing underlies two-party private inference and private information retrieval, with cost dominated by generating, moving, and evaluating distributed point function keys, and a prior trusted GPU-integrated distributed function accelerator (DFA) removed key movement by generating and consuming keys locally but tolerated only semi-honest adversaries. The authors present VIGOR-DFA, which protects the chain from authorized input to authorized output release using three mechanisms: a fresh authentication epilogue using three field multiplications per output, a freeze-before-challenge check of every opening with multiple independent MAC lanes, and a role-bound one-time resource ledger with a release guard placed beside the GPU L2 cache. They prove stand-alone static malicious security with abort in a protected-module model, with statistical error below about 2 to the negative 148 for up to 2 to the 32 checked batches. Against malicious function-secret-sharing protocols modeled after the Shark protocol family, VIGOR-DFA removes tens to hundreds of gigabytes of per-query offline authenticated material and lowers LAN latency by 10.1 to 14.0 times and energy by 3.0 to 3.9 times, at a cost of 2.5 to 3.5 times the latency of the semi-honest accelerator and 0.145 square millimeters of extra area at 7 nanometers.
