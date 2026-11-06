---
title: "When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing"
date: 2026-11-06 08:20:00 +0200
categories: [FHE]
tags: [ckks, llm-agent-safety, confidential-computing, tee-ledger]
link: https://arxiv.org/abs/2610.41401
byline: "Yixiang Luo et al. (arXiv:2610.41401, Oct 30 2026)"
description: "SealCall combines CKKS-based encrypted similarity computation with a trusted execution environment ledger to audit LLM agent tool calls without exposing their contents to the auditor."
---

Large language model agents call external tools that may access private data, and specialized safety auditors who review these calls before execution risk exposing sensitive user information if they see the raw call contents. This paper proposes a privacy-preserving auditing paradigm that separates delegated audit computation from plaintext access and execution authority, instantiated in a framework called SealCall that combines learned audit representations, CKKS-based encrypted similarity computation, and execution control bound to audited tool calls. The system follows a confine-or-declare principle inside confidential virtual machines, so user-derived data stays confined by default but can leave only after being recorded, with recipient and reason, in a user-accessible, tamper-evident declaration log. The implementation pairs per-user information-flow control written in Rust with a TEE-based ledger and remote attestation. Evaluated on 1,252 public binary candidates, SealCall achieves a mean F1 score of 0.840 under grouped nested evaluation while preserving plaintext audit decisions in all measured cases, with a representative configuration completing each encrypted scoring operation in 0.176 seconds.
