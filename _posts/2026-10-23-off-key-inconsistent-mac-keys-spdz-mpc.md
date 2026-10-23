---
title: "Off-Key: Inconsistent MAC Keys Compromise Privacy in SPDZ-Family MPC"
date: 2026-10-23 08:24:00 +0200
categories: [Cryptography]
tags: [spdz, mpc, mac-keys, privacy-attack]
link: https://eprint.iacr.org/2026/2533
byline: "Marcel Keller et al. (IACR ePrint 2026/2533, Oct 19 2026)"
description: "The Off-Key attack shows that corrupted parties in SPDZ-family secure multi-party computation can recover secret values or test guesses through selective failure whenever a deployment allows message authentication code keys to be inconsistent across batches, threads, or process runs."
---

SPDZ-family protocols for maliciously secure multi-party computation protect secret-shared values with message authentication codes (MACs) under a secret-shared global key, and their security requires all values and preprocessing used together to be authenticated under the same key. The authors present Off-Key, a privacy attack that exploits violations of this key-consistency requirement. Depending on which specific MAC check protocol is used, a corrupted party can either recover the value of a shared secret from a single authentication check, or test a guess through selective failure by modifying a MAC share and observing whether a masked check succeeds. While the attack does not compromise the theoretical security guarantees of the underlying protocols, the authors demonstrate the key-consistency vulnerability in evaluated versions of MP-SPDZ, SCALE-MAMBA, and FANNG-MPC, all of which allow a corrupted party to use different keys across batches, threads, or process runs, and they identify the state that enforces key consistency in representative preprocessing protocols, showing how preserving and reusing it prevents the attack.
