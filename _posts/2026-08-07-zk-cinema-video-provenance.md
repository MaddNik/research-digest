---
title: "zk-Cinema: Proving Video Provenance in Zero Knowledge"
date: 2026-08-07 08:17:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, snark, video-provenance]
link: https://eprint.iacr.org/2026/1598
byline: "Alexander Frolov et al. (IACR ePrint 2026/1598, Aug 4 2026)"
description: "A zero-knowledge proof system for proving that a video resulted from a claimed sequence of edits applied to signed source footage, without revealing the original content."
---

The authors show how to represent common video editing operations as matrix multiplications that are efficient for zero-knowledge provers, and introduce a SNARK-friendly video representation they call sfvr. They develop methods for incorporating signed data into SNARK proofs so that provenance claims can be tied back to authenticated source footage. Their end-to-end system builds on an optimized version of the NeutronNova folding scheme and includes a "Read-Write Streaming" variant designed to exploit parallel computation. The reported implementation achieves performance competitive with prior video-provenance proof approaches.
