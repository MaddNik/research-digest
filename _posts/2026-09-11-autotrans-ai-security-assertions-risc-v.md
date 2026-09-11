---
title: "AutoTrans: AI-Assisted Automatic Translation of Security Assertions for RISC-V Processors"
date: 2026-09-11 08:30:00 +0200
categories: [Hardware Security]
tags: [risc-v, security-assertions, formal-verification, llm-assisted]
link: https://arxiv.org/abs/2609.10057
byline: "Sharjeel Imtiaz et al. (arXiv:2609.10057, Sep 9 2026)"
description: "AutoTrans automatically translates verified hardware security assertions between different RISC-V processor targets using a hallucination-resistant LLM pipeline combined with formal verification, reaching 100 percent acceptance after human refinement."
---

Reusing verified security assertions across different RISC-V processor implementations is an expensive bottleneck in hardware security verification, since manual translation takes hours per assertion and raw LLM translation is fast but unreliable, often hallucinating port names that do not exist in the target RTL. The authors present AutoTrans, an automated framework that first uses a lightweight regular-expression-based SystemVerilog signal extractor to identify valid signals and prevent hallucination, then applies a prompt template with pinned inference parameters to guarantee byte-identical prompts across runs, and can generate security assertions directly from English-only security descriptions with no manual authoring. A formal verification step using JasperGold FPV then checks that generated assertions actually verify the target processor's security rather than silently entering the result set. Applied with Deepseek V4 to translate assertions between RISC-V cores such as IBEX and NS31A, AutoTrans achieves a 78 percent automatic translation acceptance rate without human intervention and 100 percent after human refinement.
