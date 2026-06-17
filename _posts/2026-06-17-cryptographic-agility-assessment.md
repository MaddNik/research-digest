---
title: "An Assessment Framework for Application-Level Cryptographic Agility"
date: 2026-06-17 08:14:00 +0200
categories: [PQC]
tags: [cryptographic-agility, migration, api-design]
link: https://arxiv.org/abs/2606.13425
byline: "Navaneeth Rameshan et al. (arXiv:2606.13425, Jun 11 2026)"
description: "A seven-dimension framework for assessing how ready software cryptographic APIs are for the post-quantum transition."
---

The authors argue that the post-quantum transition requires wholesale replacement
of algorithms across all software, yet today's cryptographic APIs were not built
with agility in mind. They introduce a component-based framework that characterizes
application-level cryptographic agility along seven orthogonal dimensions,
including three coupling dimensions, a decoupling mechanism, a governance authority
dimension, and two migration-capability enablers. Evaluating six representative
APIs (PKCS#11, OpenSSL 3.0, JCA, Google Tink, AWS KMS, and HashiCorp Vault
Transit) against the framework, they find three pervasive and independent gaps: no
system supports intent-based key creation, none provides policy-driven algorithm
selection distinct from access control, and none offers first-class operations for
transforming the algorithm of existing keys. They conclude that each gap alone is
enough to block agile migration, explaining why the post-quantum transition remains
largely a software engineering problem.
