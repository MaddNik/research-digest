---
title: "STAR: Scalable TEE-based Anonymous Rate-limiter"
date: 2026-10-30 08:37:00 +0200
categories: [Hardware Security]
tags: [trusted-execution-environments, anonymous-authentication, rate-limiting, memory-access-side-channel]
link: https://arxiv.org/abs/2610.38602
byline: "Kosei Akama et al. (arXiv:2610.38602, Oct 28 2026)"
description: "STAR uses server-side trusted execution environments with countermeasures against secret-dependent memory access patterns to deliver anonymous rate limiting at tens of microseconds per request and about 13.9 thousand requests per second per CPU core."
---

Rate limiting is needed to protect Internet services from attacks such as TLS and HTTP floods, but identifying users to enforce those limits can compromise their privacy, and existing anonymous rate-limiting schemes either struggle to scale or assume services and authorities will not collude. This paper presents STAR, which uses server-side trusted execution environments to overcome both limitations, relying on TEEs to make lightweight cryptographic authentication efficient. Because malicious services could otherwise observe memory-access patterns inside the TEE to infer user secrets, the authors design countermeasures against secret-dependent memory accesses and assess their implementation using dynamic analysis, and they also design a secure sharding mechanism that distributes client requests to extend efficiency gains across multiple servers. The resulting system processes authentication requests in tens of microseconds and handles approximately 13,900 requests per second per CPU core, demonstrating that strong privacy guarantees can coexist with efficient authentication at scale.
