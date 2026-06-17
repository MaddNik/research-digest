---
title: "The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs"
date: 2026-06-17 08:35:00 +0200
categories: [Hardware Security]
tags: [tee, attestation, confidential-computing, supply-chain]
link: https://arxiv.org/abs/2606.16358
byline: "Sipeng Xie et al. (arXiv:2606.16358, Jun 15 2026)"
description: "An attested API router that confines plaintext to a small hardware enclave so an untrusted host cannot read or alter LLM interactions."
---

Agents increasingly reach large language models through API routers, which
terminate the client's transport-layer security session and open a separate upstream
session, leaving the router holding the full interaction in plaintext as an
application-layer man-in-the-middle. Such a router can rewrite tool calls, swap
dependencies for typosquatted packages, trigger attacks only when audits are absent,
and exfiltrate secrets, and existing client-side defenses are evadable. The authors
propose AEGIS, a provider-transparent attested router whose data path is a
client-verified faithful passthrough that confines plaintext handling to a small
hardware-enclave component while leaving authentication, scheduling, accounting, and
management on the untrusted host. The client verifies the enclave before releasing
plaintext, so the host can neither read nor alter the interaction and plaintext
leaves only toward destinations fixed by the measured image. All four
malicious-router attack classes succeed against a plaintext-access baseline and are
blocked by AEGIS, including adaptive tests. The trusted path is 851 lines, carries
three provider-native APIs without conversion, and adds about six milliseconds of
local relay overhead per request.
