---
title: "Aker: Efficient Two-Party SLH-DSA"
date: 2026-11-20 08:08:00 +0200
categories: [PQC]
tags: [slh-dsa, threshold-signatures, secure-multiparty-computation, hash-based-signatures]
link: https://eprint.iacr.org/2026/2899
byline: "Yaron Salman, Ben Riva, Dmitry Kogan (IACR ePrint 2026/2899, Nov 15 2026)"
description: "Aker is a maliciously secure two-party signing protocol for SLH-DSA, NIST's stateless hash-based signature standard, compatible with an unmodified FIPS 205 verifier."
---

Threshold signing is widely used to protect cryptographic keys, but extending it to post-quantum signatures has been difficult because SLH-DSA, NIST's stateless hash-based signature standard in FIPS 205, lacks the algebraic structure that efficient threshold protocols for lattice-based signatures typically exploit. The authors present Aker, a maliciously secure two-party signing protocol that remains compatible with an unmodified FIPS 205 verifier. It combines generic secret-sharing multiparty computation with four optimizations that exploit the structure of the SLH-DSA hypertree, including evaluating active layers concurrently, caching public keys so only the signing leaf needs multiparty evaluation, reusing upper-layer signatures across messages, and sampling one-time subtree components locally. Some of these optimizations require stateful signers and place a lower limit on the number of signatures per key. In a server-server deployment combining these techniques with a new GPU engine for maliciously secure Boolean GMW, online signing for SLH-DSA-128f between two single-GPU cloud servers takes 2.09 seconds, or 0.76 seconds with a lower signature limit, while in a client-server deployment online signing needs only four low-bandwidth communication rounds after an offline session.
