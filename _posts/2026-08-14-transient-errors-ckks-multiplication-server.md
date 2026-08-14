---
title: "When and Where Faults Matter: A Study of Transient Errors in CKKS Multiplication"
date: 2026-08-14 08:19:00 +0200
categories: [FHE]
tags: [fault-injection, ckks, transient-errors]
link: https://arxiv.org/abs/2608.11147
byline: "Vattana Chan et al. (arXiv:2608.11147, Aug 11 2026)"
description: "Server-side homomorphic multiplication in unoptimized CKKS is sensitive to both the timing and the ciphertext-component location of injected transient errors."
---

Homomorphic encryption allows computation directly on encrypted data without decryption, and this paper studies where and when errors during FHE computation actually corrupt results, focusing on server-side homomorphic multiplication in the CKKS scheme. The authors show that errors injected into the two ciphertext components, referred to as c0 and c1, have different impacts depending on both which component is affected and when during the multiplication the error occurs. The study is framed as an initial characterization rather than a full system design, and it establishes that the timing and location of transient faults meaningfully change the correctness of the final FHE output.
