---
title: "HermiCache: Enclave-Aware Cache Replacement for Trusted Execution Environments"
date: 2026-09-11 08:31:00 +0200
categories: [Hardware Security]
tags: [cache-side-channel, trusted-execution-environments, risc-v, keystone]
link: https://arxiv.org/abs/2609.10634
byline: "Oussama Elmnaouri et al. (arXiv:2609.10634, Sep 9 2026)"
description: "HermiCache is an enclave-aware cache replacement policy for RISC-V trusted execution environments that gives fine-grained, deterministic protection against cache-based side channels with only 6 percent processor area overhead."
---

Trusted execution environments protect enclave memory from untrusted software but remain vulnerable to cache-based side-channel attacks because of shared microarchitectural resources, and existing countermeasures such as cache partitioning or randomization do not always give designers fine-grained configuration or deterministic protection. The authors introduce HermiCache, a cache replacement design for RISC-V cores that targets these requirements, implementing it in the OpenHwGroup CVA6 core paired with a Keystone TEE software layer. The solution adds an area overhead of only 6 percent on the processor core, offering a lightweight and deterministic alternative for mitigating enclave cache side channels.
