---
title: "IISFA: Ineffective Instruction-Skip Fault Attacks on Bitslice Implementations"
date: 2026-10-23 08:32:00 +0200
categories: [Hardware Security]
tags: [fault-attack, bitslicing, instruction-skip, lightweight-ciphers]
link: https://eprint.iacr.org/2026/2536
byline: "Hanbeom Shin et al. (IACR ePrint 2026/2536, Oct 20 2026)"
description: "The IISFA attack recovers keys from redundancy-protected bitsliced block cipher implementations by exploiting instruction skips that leave outputs unchanged, succeeding in every trial against five bitsliced implementations of GIFT, SKINNY, and PIPO on an AVR microcontroller."
---

Redundancy countermeasures are designed to prevent differential fault analysis by withholding faulty ciphertexts, and ineffective fault analysis and statistical ineffective fault attacks instead exploit executions where an injected fault leaves the result unchanged. The authors present the Ineffective Instruction-Skip Fault Attack (IISFA) on bitsliced implementations protected by redundancy, observing that skipping a bitsliced instruction processing m S-boxes simultaneously leaves the group unchanged exactly when all m S-box inputs belong to a computable ineffective set, so each ciphertext the device outputs restricts all m n-bit subkeys to candidates whose S-box inputs lie in that set. The authors determine which key candidates remain indistinguishable under a single target instruction, give key-recovery procedures for known- and chosen-plaintext settings that combine different target instructions across queries, and calculate expected injection counts from the ineffective sets to make the search for efficient target sequences practical. They evaluate five bitsliced implementations of the GIFT, SKINNY, and PIPO ciphers on an 8-bit AVR microcontroller protected by a redundancy countermeasure using clock glitches, and all measured key-recovery campaigns succeed in every trial.
