---
title: "CHERI-D Reincarnate: efficient multicore CHERI temporal memory safety through allocation reincarnation"
date: 2026-09-11 08:28:00 +0200
categories: [Hardware Security]
tags: [cheri, memory-safety, use-after-free, fpga]
link: https://arxiv.org/abs/2609.11590
byline: "Yuecheng Wang et al. (arXiv:2609.11590, Sep 10 2026)"
description: "CHERI-D Reincarnate extends the CHERI capability architecture to allow immediate reuse of freed memory for temporal memory safety, cutting memory-sweep frequency and quarantine overhead in a multicore FPGA implementation."
---

Prior work called CHERI-D provides temporal memory safety for the CHERI capability architecture using a finite-width generation ID stored at a fixed location, but requires quarantining an object once its ID is exhausted. The authors propose CHERI-D Reincarnate, which mitigates use-after-free bugs while permitting immediate reuse of freed memory through allocation reincarnation: instead of quarantining a memory slot when its ID is exhausted, the design dynamically assigns the slot a new ID, quarantining and later reclaiming only the exhausted IDs rather than the underlying memory. The system adds coherent ID caching while keeping a fully decentralized ID organization, and connects physical coherence events to a virtually addressed object ID buffer through lightweight reverse-map and filter mechanisms to support multicore execution. Implemented as a hardware-software co-design across a CHERI-Toooba FPGA softcore, QEMU, LLVM/Clang, and CheriBSD, the design substantially reduces memory-sweep frequency and quarantine memory across evaluated workloads while adding only low performance and hardware overhead.
