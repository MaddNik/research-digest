---
title: "PAGE404: Breaking GPU Isolation Through Hardware-assisted Page Migration"
date: 2026-10-16 08:31:00 +0200
categories: [Hardware Security]
tags: [gpu-isolation, covert-channel, grace-hopper, multi-instance-gpu]
link: https://arxiv.org/abs/2610.20962
byline: "Ravan Nazaraliyev et al. (arXiv:2610.20962, Oct 14 2026)"
description: "New side- and covert-channel attacks on NVIDIA's Grace Hopper superchip exploit hardware-assisted page migration to leak information across Multi-Instance GPU partitions that are supposed to provide hardware-enforced isolation."
---

NVIDIA's Grace Hopper superchip tightly integrates a 72-core Arm CPU with a Hopper GPU over a cache-coherent interconnect, creating a unified memory domain with hardware-assisted page migration that uses access counters to promote frequently used pages from host memory to GPU DRAM. The authors study the security of this page migration support and identify two side-channel vulnerabilities, one rooted in the shared structure of the access counters and the other in how the UVM driver handles migration interrupts, and show that both channels are exploitable across Multi-Instance GPU partitions that are meant to provide strong, hardware-enforced isolation between co-located tenants. Proof-of-concept covert channels built on these vulnerabilities reach roughly 8,500 bits per second through eviction-based signaling and 8,100 bits per second through migration-delay-based signaling across MIG instances. The interrupt-based channel can also fingerprint inference workloads across different large language models and CPU benchmarks, and estimate the prompt length processed during LLM inference with high accuracy, exposing a security gap in hardware-managed heterogeneous memory systems and calling into question current MIG isolation guarantees.
