---
title: "Practical Differential Fault Attacks on the GPRS Standard Ciphers"
date: 2026-08-28 08:31:00 +0200
categories: [Hardware Security]
tags: [differential-fault-attack, stream-ciphers, gprs, fault-injection]
link: https://eprint.iacr.org/2026/1806
byline: "Zhengting Li et al. (IACR ePrint 2026/1806, Aug 26 2026)"
description: "The first differential fault attack on the GEA-like stream ciphers recovers the 64-bit secret keys of the GPRS standard ciphers GEA-1 and GEA-2 within minutes on a common laptop."
---

GEA-1 and GEA-2 are stream ciphers standardized for GPRS to protect data between a phone and base station, and the authors note that a range of current phones still support them. This paper proposes, for the first time, a differential fault attack on GEA-like stream ciphers under a random fault model, including an efficient dedicated algorithm for identifying the exact fault location. Applying this to GEA-1 and GEA-2, the attacks recover the ciphers' 64-bit secret keys with time complexities of 2 to the 33.807th power and 2 to the 33.858th power respectively, results the authors validate by simulating the full attacks on a ChipWhisperer Lite platform. The experiments show both GEA-1 and GEA-2 can be broken within sixteen minutes on a common laptop, and the authors propose possible countermeasures to protect data on the large installed base of GPRS devices; the work is published in IEEE Transactions on Dependable and Secure Computing.
