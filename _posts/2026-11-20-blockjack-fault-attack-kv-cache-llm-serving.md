---
title: "BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving"
date: 2026-11-20 08:25:00 +0200
categories: [Hardware Security]
tags: [fault-attacks, rowhammer, llm-serving, kv-cache]
link: https://arxiv.org/abs/2611.25945
byline: "Qifan Wang et al. (arXiv:2611.25945, Nov 19 2026)"
description: "BlockJack uses Rowhammer-style fault attacks on vLLM's software block-table address translation to redirect one tenant's key-value cache reads into another tenant's data."
---

Paged large language model serving frameworks such as vLLM manage the key-value cache with block tables analogous to operating system page tables, mapping each request's logical KV blocks to physical blocks in a software-managed address translation layer. While fault attacks like Rowhammer have previously redirected memory through OS page tables, and prior fault attacks on LLMs targeted model weights or cached KV contents directly, this KV-cache mapping layer had not been explored. The authors present BlockJack, the first fault attack on KV cache address translation in LLM inference, which corrupts block-table entries to redirect a request's KV cache reads into blocks assigned to another tenant's request without touching model parameters, prompts, or cached KV states. The attack achieves both a confidentiality violation, where victim information appears in the attacker's responses, and an integrity violation, where attacker-supplied context steers the victim's answers. Across seven models spanning the Qwen, Llama, Gemma, and Phi families, a faulted mapping exposes victim context, and on a 248-scene medical benchmark the integrity attack causes up to 41.1 percent of responses to recommend less urgent care while still appearing consistent with the victim's question. The authors demonstrate physical feasibility with Rowhammer, evaluate assignment validation as a defense, and report that vLLM and Sonar confirmed the vulnerability and proposed patches after responsible disclosure.
