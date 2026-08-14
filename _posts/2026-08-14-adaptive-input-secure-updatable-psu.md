---
title: "Adaptive-Input-Secure Updatable Private Set Union"
date: 2026-08-14 08:24:00 +0200
categories: [Cryptography]
tags: [private-set-union, mpc, oblivious-key-value-store]
link: https://eprint.iacr.org/2026/1626
byline: "Seongbong Choi et al. (IACR ePrint 2026/1626, Aug 6 2026)"
description: "The first semi-honest, adaptive-input-secure protocol for updatable private set union supports two-sided additions and deletions across multiple epochs, up to 98.9 times faster than re-running a static protocol."
---

In multi-epoch private set union (PSU) deployments, a receiver may adaptively choose its next epoch's input after observing the previous epoch's union result, a setting prior updatable private-set-intersection frameworks did not extend to cover PSU. The authors close this gap by constructing the first semi-honest updatable PSU protocol that supports two-sided add and delete updates under adaptive inputs. Their core building block is an updatable oblivious key-value store with distributional erasure properties, built by combining Band-OKVS with a pseudorandom function so that per-epoch encoding cost scales linearly, rather than quadratically, in the band width. Experimentally, the protocol achieves a 30.9 to 98.9 times speedup over the alternative of re-executing a static PSU protocol from scratch at every epoch.
