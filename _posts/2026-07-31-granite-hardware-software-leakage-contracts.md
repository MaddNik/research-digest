---
title: "Granite: A Modular Methodology for Foundational Verification of Hardware-Software Leakage Contracts"
date: 2026-07-31 08:26:00 +0200
categories: [Hardware Security]
tags: [side-channel, formal-verification, timing-leakage, risc-v]
link: https://arxiv.org/abs/2607.27480
byline: "Stella Lau et al. (arXiv:2607.27480, Jul 29 2026)"
description: "Granite is a formal-verification methodology that proves a pipelined RISC-V processor's cycle-by-cycle timing is fully determined by an instruction-set-level leakage contract."
---

The paper targets the gap between instruction-set-level leakage contracts, used to reason about constant-time cryptographic code, and the actual microarchitectural behavior of a processor implementation. It introduces leakage-aware refinement via determinism, establishing functional correctness and confidentiality together as trace equivalence between the specification and the RTL implementation. Specifications constrain only functional correctness and information-flow dependencies, not specific cycle counts or latencies, and secret-independent nondeterminism is handled by parameterizing specs with untrusted deterministic functions over public data only. The methodology composes with certified static analysis so the proof chain eliminates intermediate specifications from the trusted computing base. The result is a modular, foundational connection between instruction-set leakage contracts and cycle-by-cycle microarchitectural execution.
