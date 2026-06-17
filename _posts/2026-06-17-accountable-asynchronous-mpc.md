---
title: "Accountable Asynchronous Multi-Party Computation"
date: 2026-06-17 08:25:00 +0200
categories: [Cryptography]
tags: [mpc, asynchronous, accountability, secret-sharing]
link: https://eprint.iacr.org/2026/1245
byline: "Pierre Civit et al. (IACR ePrint 2026/1245, Jun 11 2026)"
description: "The first accountable asynchronous MPC protocol, which either preserves safety or yields publicly verifiable evidence implicating faulty parties when corruptions exceed the resilience threshold."
---

In non-synchronous networks, classic partition arguments imply that any t-resilient
protocol among n parties cannot ensure safety for many meaningful functionalities
once corruptions reach f greater than or equal to n minus 2t, which motivates
building in accountability to detect and deter safety violations. The authors
present the first accountable asynchronous MPC protocol that securely evaluates any
asynchronously computable arithmetic circuit. It ensures correctness, privacy,
input-independence, and guaranteed output delivery whenever f is at most t which is
below n over 3, and provides strong accountability in a higher corruption range
where either all hypersafety properties continue to hold without guaranteed output
delivery, or every honest party obtains publicly verifiable evidence implicating at
least n minus 2t faulty processes. The construction follows the standard
offline/online paradigm and assumes only a transparent setup, namely a
bulletin-board public key infrastructure and a common random string. The main
technical contribution is an accountable additively homomorphic high-threshold
asynchronous complete verifiable secret sharing functionality with amortized linear
communication. This yields an online phase with latency proportional to the circuit
depth and amortized communication proportional to circuit size times n.
