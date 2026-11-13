---
title: "TUTTI: Parallel CKKS Bootstrapping in under 3 ms on CPU"
date: 2026-11-13 08:16:00 +0200
categories: [FHE]
tags: [ckks, bootstrapping, low-latency]
link: https://eprint.iacr.org/2026/2848
byline: "Robin Kostler, Antonio Guimaraes (IACR ePrint 2026/2848, Nov 9 2026)"
description: "TUTTI is a new CKKS bootstrapping procedure whose multi-threaded latency beats TFHE when bootstrapping a single message, closing a long-standing gap between CKKS and lightweight FHE schemes."
---

The authors introduce TUTTI, a new CKKS bootstrapping procedure that outperforms previous low-latency solutions in multi-threaded latency for any number of messages and, notably, has lower latency than TFHE when bootstrapping a single message. The construction builds on the SPRU bootstrapping method, improving it with new ways of exploiting parallelism and increasing the number of bootstrapped messages, together with a refined security analysis of the block-binary secret keys used in prior work. TUTTI bootstraps 4096 real-number messages in 46 to 83.4 milliseconds on 192 threads to restore 1 to 9 multiplicative levels, outperforming the prior SHIP method by up to a factor of 3 on the same machine, and unlike SHIP it gains immediately from bootstrapping fewer messages, with a 256-message bootstrap taking just 15 to 34 milliseconds on 32 threads. For a single message, TUTTI takes 4.6 milliseconds on 32 threads, compared to 7.3 milliseconds for TFHE-rs performing a 4-bit bootstrap on the same machine and thread count, and the advantage persists on an Apple M5 Pro laptop, where TUTTI takes 2.4 milliseconds on 14 threads against 4.5 milliseconds for TFHE-rs. The authors conclude that CKKS and lightweight schemes such as TFHE still differ in functionality, key sizes, and security assumptions, but that multi-threaded latency is no longer one of those differences.
