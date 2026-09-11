---
title: "A RAM-Efficient Implementation of Falcon"
date: 2026-09-11 08:09:00 +0200
categories: [PQC]
tags: [falcon, fn-dsa, lattice-signatures, embedded-implementation]
link: https://eprint.iacr.org/2026/1915
byline: "Thomas Pornin (IACR ePrint 2026/1915, Sep 7 2026)"
description: "A new implementation of the Falcon post-quantum signature scheme cuts RAM usage to about 11 kilobytes and speeds up signing on Arm Cortex M4, making it suitable for smart cards."
---

The author presents a RAM-efficient implementation of the Falcon lattice-based signature scheme, reducing memory usage to about 11 kilobytes, down from about 31 kilobytes in the previous implementation of Falcon-512. The new code is also faster on Arm Cortex M4 hardware, with average signature generation cost down to 13.45 million cycles. The optimizations include a novel variant of the fast Fourier transform, replacement of some floating-point operations with modular integer computations, delayed addition of input within the fast Fourier sampling process, and an alternate signature reassembly process, together removing more than half of the floating-point operations. The resulting implementation is small enough to run on constrained embedded systems such as smart cards.
