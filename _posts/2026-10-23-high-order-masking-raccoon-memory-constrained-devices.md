---
title: "Efficient and Compact High-order Masking Raccoon on Memory Constrained Devices"
date: 2026-10-23 08:12:00 +0200
categories: [PQC]
tags: [raccoon-signature, masking, side-channel-resistance, lattice-signatures]
link: https://eprint.iacr.org/2026/2540
byline: "Junhao Huang et al. (IACR ePrint 2026/2540, Oct 19 2026, TCHES 2026)"
description: "The first efficient, compact implementation of high-order masked Raccoon on ARM Cortex-M4 outperforms the reference implementation by up to 2.25 times and, at masking orders 2, 4, and 8, outperforms masked Dilithium3 by up to 8.07 times."
---

Raccoon, presented at CRYPTO 2024, is a provably secure lattice-based signature scheme with O(d log d) masking overhead, and while it did not advance beyond the first round of NIST's additional call for post-quantum signatures, it remains attractive for its low masking overhead and strong provable side-channel resistance. This paper presents the first efficient and compact implementation of high-order Raccoon on ARM Cortex-M4, optimizing polynomial multiplication, sampling, and memory consumption. For multiplication, the authors present a consecutive 32-bit NTT/INTT implementation for Raccoon's two moduli with optimal 3+3+3 layer merging and extensive lazy reduction, including a novel negative double Montgomery reduction technique, and for sampling they resolve a bottleneck caused by frequent incremental SHAKE256 invocations by switching to a one-shot approach, yielding speedups of at least 1.80 times across all sampling routines. The resulting implementation outperforms the Raccoon reference implementation by 1.85 to 2.25 times, and high-order masked Raccoon-192 outperforms masked Dilithium3 by 3.12, 8.07, and 2.71 times at masking orders 2, 4, and 8 respectively, while supporting masking up to order 32 on resource-constrained IoT devices. Leakage evaluations confirm that the second-order implementation resists differential power analysis once micro-architectural transitional leakages are mitigated.
