---
title: "LightShark: Actively Secure Machine-Learning Inference Based on Lightweight Authenticated Distributed Comparison Function"
date: 2026-07-24 08:22:00 +0200
categories: [Cryptography]
tags: [secure-two-party-computation, distributed-comparison-function, active-security, ml-inference]
link: https://eprint.iacr.org/2026/1487
byline: "Chenkai Zeng et al. (IACR ePrint 2026/1487, Jul 21 2026)"
description: "An actively secure two party MPC protocol for machine learning inference built on a lighter weight authenticated distributed comparison function than prior work."
---

The paper builds on the Shark protocol from IEEE S&P 2025 for secure two party inference and introduces the first actively secure variant of a Grotto style distributed comparison function. This new authenticated construction reduces the key sizes required compared to classic distributed comparison function implementations. The resulting LightShark framework supports common machine learning operations such as ReLU, spline approximation, and truncation, and is evaluated on models including VGG-16, GPT, and BERT. The authors report LightShark is 1.49 to 2.69 times faster than Shark and cuts communication cost by 66.7 percent for BERT-base inference, with the largest gains on larger language models.
