---
title: "Square Root of All Evil: The Dangers of Falcon's Superfluous Square Roots"
date: 2026-09-18 08:09:00 +0200
categories: [PQC]
tags: [falcon, fault-attack, fn-dsa, implementation-security]
link: https://eprint.iacr.org/2026/2046
byline: "Hiroto Kaihara et al. (IACR ePrint 2026/2046, Sep 15 2026, ACM CCS 2026)"
description: "Researchers show that Falcon's floating-point square root computations are unnecessary and, worse, an exploitable fault-attack target that leaks the full signing key from a single glitch."
---

Falcon is one of the three post-quantum signature schemes NIST has selected for standardization as FN-DSA, prized for its compactness but notoriously hard to implement correctly because of its reliance on floating-point operations, especially square root computations. The authors first show these square root computations are actually unnecessary, since Falcon's algorithm can be rewritten without them to give a simpler implementation that is equally fast or slightly faster. They then show the square roots also create a security risk by acting as a uniquely sensitive target for physical attacks, demonstrated with a fault attack against an ARM Cortex-M4 microcontroller. Injecting a single glitch into one square root computation, followed by generating around a million signatures with the unperturbed signing algorithm, leads to full key recovery with 100 percent success rate, and the resulting faulty signatures are hard to distinguish from valid ones. The authors describe this as the most devastating fault attack against Falcon to date, since prior attacks needed hundreds of millions of signatures, many injected faults, or produced easily distinguishable signatures, and they also flag supply-chain and dependency-management risks tied to the square root computations.
