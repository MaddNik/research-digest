---
title: "OpenLLM: Modular and Scalable zkSNARKs for Verifiable LLM Inference"
date: 2026-08-07 08:18:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, snark, verifiable-computation]
link: https://eprint.iacr.org/2026/1578
byline: "Yunbo Yang et al. (IACR ePrint 2026/1578, Aug 2 2026)"
description: "A modular zkSNARK system that decomposes large language model inference into reusable atomic operators so an untrusted server's inference results can be verified without full end-to-end proof overhead."
---

The paper addresses the problem of verifying that a remote, untrusted server correctly performed large language model inference rather than skipping computation or returning wrong results. Because modern large language models use many non-linear operations that are costly to model in finite fields, prior zero-knowledge approaches to verifiable inference struggle with overhead, precision loss, and scaling to large models. OpenLLM decomposes inference into a set of reusable atomic operators, each with its own efficient zero-knowledge proof protocol, so that verification can be composed at the operator level independent of the model architecture. The authors design succinct non-interactive proof constructions for representative non-linear functions and evaluate the system across operator-level performance, full end-to-end inference, layer-wise scaling, and larger models. They report smaller proof sizes, lower verification cost, and improved numerical fidelity compared to prior end-to-end and interactive verifiable-inference approaches.
