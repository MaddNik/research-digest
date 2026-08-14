---
title: "SLAC: Access-Driven CPU-to-GPU Side-channel Attacks via System-Level Cache on Apple Silicon"
date: 2026-08-14 08:30:00 +0200
categories: [Hardware Security]
tags: [cache-side-channel, apple-silicon, microarchitectural-attack]
link: https://arxiv.org/abs/2608.09075
byline: "Tianhong Xu et al. (arXiv:2608.09075, Aug 10 2026)"
description: "GPU memory accesses on Apple Silicon leave observable footprints in the shared system-level cache, letting an unprivileged CPU process infer neural network and language model activity with up to 94.8 percent accuracy."
---

Apple Silicon chips share a system-level cache between CPU and GPU cores, and this paper demonstrates that GPU memory accesses leave set-level footprints in that shared cache which an unprivileged CPU process can observe. The authors build two concrete attack primitives, CPrime+CProbe and GPrime+CProbe, that exploit this shared-cache behavior to monitor GPU activity from the CPU side without special privileges. Using these primitives, they demonstrate practical attacks that recover information processed by Graph Neural Networks with 90 percent accuracy and infer input keywords processed by Large Language Models with up to 94.8 percent accuracy. The work identifies a new class of microarchitectural side-channel vulnerability specific to heterogeneous CPU-GPU cache architectures, rather than classical CPU-only cache attacks. The paper was accepted to ACM CCS 2026 and calls for redesigned system cache isolation in heterogeneous processors.
