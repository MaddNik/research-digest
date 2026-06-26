---
title: "G-Lox: Group-Adaptive, Privacy-Preserving Bridge Distribution with Two-Party Computation"
date: 2026-06-19 08:12:00 +0200
categories: [Cryptography]
tags: [mpc, blockchain, privacy]
link: https://arxiv.org/abs/2606.19620
byline: "Baigang Chen et al. (arXiv:2606.19620, Jun 17 2026)"
description: "A bridge-distribution system that keeps adaptive group-level logic hidden from any single server using secure two-party computation."
---

G-Lox is a censorship-circumvention bridge-distribution system that preserves Lox-style
distributor blindness while enabling hidden, stateful group-level adaptation. It uses a
two-server privacy architecture in which the adaptive assignment logic remains hidden from
any single server, with secure multi-party computation protocols managing private state
access and state-dependent updates. The system supports features such as blockage
reporting and transport-aware reassignment. Reported client overhead is low, with
per-iteration communication in the low-kilobyte range; at M equals 1024 it sends about
1968 bytes and receives about 1280 bytes in roughly 0.25 seconds. Simulations indicate
improved robustness over existing Lox and rBridge-like systems.
