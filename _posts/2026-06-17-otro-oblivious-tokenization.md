---
title: "OTRO: Oblivious Tokenization Path with Square-Root ORAM"
date: 2026-06-17 08:33:00 +0200
categories: [Hardware Security]
tags: [hardware-security, side-channel, mpc]
link: https://arxiv.org/abs/2606.17358
byline: "Jonghyun Lee et al. (arXiv:2606.17358, Jun 15 2026)"
description: "An oblivious tokenizer for confidential LLM serving that blocks access-pattern leakage on Intel TDX with minimal latency cost."
---

The CPU-side large language model tokenizer is a security gap in confidential
computing stacks built on CPU and GPU trusted execution environments, because its
table-driven lookups produce memory access patterns that recent work has shown can
recover user prompts on production Intel TDX. Naively applying tree-based oblivious
RAM such as PathORAM stops the leakage but slows the tokenizer by roughly thirteen
times. OTRO instead uses square-root ORAM for fast single-access lookups and avoids
its costly periodic rebuild through three techniques: a pool of replicated read-only
ORAM instances, an epoch-based rotation policy padded with dummy accesses, and
chunked key-value-cache-aware tokenization that overlaps rebuilds with GPU prefill.
Implemented in HuggingFace Tokenizers and nano-vLLM inside a TDX-enabled
confidential virtual machine with an NVIDIA H100, OTRO holds time-to-first-token
overhead to at most 4.5 percent. It keeps tokenizer-induced latency under 10 percent
of total time-to-first-token and adds less than half a gigabyte of memory. The
result reduces observable leakage across multiple model families and sizes.
