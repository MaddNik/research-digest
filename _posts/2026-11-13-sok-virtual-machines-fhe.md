---
title: "SoK: Understanding Virtual Machines over Fully Homomorphic Encryption"
date: 2026-11-13 08:19:00 +0200
categories: [FHE]
tags: [fhe-compilers, virtual-machines, hardware-accelerators]
link: https://eprint.iacr.org/2026/2816
byline: "Song Bian et al. (IACR ePrint 2026/2816, Nov 7 2026)"
description: "A systematization of knowledge covering more than 125 works identifies three distinct forms of virtual machines over fully homomorphic encryption and compares their programming models, compilers, and hardware acceleration needs."
---

The authors survey the current literature on fully homomorphic encryption from a virtual machine perspective, observing that programs behave in an intrinsically different way over FHE than on plaintext, forming a new computation paradigm that is fundamentally constrained by the obliviousness of data. To better understand the computational properties involved, they compile more than 125 works into a cross-layer systematic view of FHE virtual machines, focusing on understanding the concrete programming models over encrypted data, and identify three distinct forms of such virtual machines: the SISD VM, the SIMD VM, and the hybrid VM. To aid this systematization, they also discuss how current FHE compilers and hardware accelerators can be applied to improve the usability and performance of each VM type. In an experimental evaluation, they test eight VM instructions at varying precision as well as two end-to-end application programs to quantitatively assess the concrete design trade-offs of each paradigm, concluding that FHE virtual machines of different types exhibit distinct utility and performance characteristics that call for new cross-layer design methodologies.
