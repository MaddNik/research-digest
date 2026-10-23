---
title: "Big Secrets Small Shares: Revisiting Secure Multi-Party Computation"
date: 2026-10-23 08:28:00 +0200
categories: [Cryptography]
tags: [secret-sharing, mpc, ramp-schemes, communication-complexity]
link: https://arxiv.org/abs/2610.27609
byline: "Wilton Kim et al. (arXiv:2610.27609, Oct 20 2026)"
description: "A new compact sharing scheme combines Damgard-Nielsen preprocessing with Cramer-Damgard-de Haan ramp secret sharing to achieve constant communication overhead per extension-field element in multi-party computation, when the extension degree scales linearly with the number of parties."
---

At CRYPTO 2007, Damgard and Nielsen introduced a preprocessing approach to multi-party computation (MPC) achieving linear communication complexity, while Cramer, Damgard, and de Haan proposed at EUROCRYPT 2007 a separate approach using ramp secret-sharing schemes to jointly share base-field components of extension-field secrets. This paper combines both ideas to achieve a non-asymptotic reduction in communication cost within a multi-phase MPC setup, introducing a modification of the ramp secret-sharing scheme called compact sharing, along with an MPC protocol tailored to it. Compact sharing masks the polynomial coefficients that would otherwise leak during degree reduction, and the resulting protocol provides perfect security against static semi-honest adversaries under an explicit trade-off between the corruption threshold and the extension degree. When the extension degree scales linearly with the number of parties, the gate-evaluation core of the protocol achieves constant communication overhead relative to an extension-field element, amortized over full preprocessing batches, with input and output communication counted separately.
