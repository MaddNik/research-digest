---
title: "Intent-Based Cryptographic API Design for Cryptographic Agility"
date: 2026-06-17 08:15:00 +0200
categories: [PQC]
tags: [cryptographic-agility, api-design, key-migration]
link: https://arxiv.org/abs/2606.13445
byline: "Navaneeth Rameshan et al. (arXiv:2606.13445, Jun 11 2026)"
description: "Design principles and Protocol Buffers patterns for cryptographic APIs that let organizations swap algorithms without rewriting application code."
---

This companion paper tackles the limitation that most deployed cryptographic APIs
are built around specific algorithms, offer little policy-based selection, and
provide no clean path to migrate existing keys to newer algorithms. The authors
derive the principles needed for a cryptographically agile API from five
architectural characteristics: abstraction, stability, temporal flexibility,
separation, and extensibility. They show how these principles map onto concrete
Protocol Buffers design patterns, including an intent vocabulary based on scopes
that decouples key creation from algorithm identities and supports transparent
algorithm substitution. Governance is handled by an abstract policy API that does
not prescribe a policy format, while keys are referenced by stable identifiers and
support rotation, transformation, and migration operations that track both the
original identity and its evolution history. The stated goal is to make updating
cryptography an operational process rather than a code rewrite.
