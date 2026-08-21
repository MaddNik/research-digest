---
title: "Verifiable Compression of Images"
date: 2026-08-21 08:21:00 +0200
categories: [Cryptography]
tags: [zero-knowledge-proofs, image-provenance, c2pa, verifiable-computation]
link: https://eprint.iacr.org/2026/1717
byline: "Yue Zhang et al. (IACR ePrint 2026/1717, Aug 17 2026)"
description: "A zero-knowledge proof system called SPEG lets JPEG-compressed images retain verifiable provenance under the C2PA signing standard."
---

The paper addresses the problem that AI-generated imagery has made image authenticity harder to establish, and that the C2PA standard's digital signatures on original images break once an image is lossily compressed, for example as a JPEG, during normal sharing workflows. Prior zero-knowledge proof systems could handle basic edits but not lossy JPEG compression specifically. The authors introduce SPEG, a proof system that lets a prover show a C2PA signature is still validly attributable to an image even after JPEG compression, without revealing the uncompressed original. It supports two modes, a general one compatible with any hash function and a faster one built on polynomial commitments. Key techniques include moving the non-algebraic parts of JPEG encoding outside the arithmetic proving circuit and removing unnecessary range checks on floating-point operations. Reported performance is 47 seconds to prove a JPEG compression of a full-HD image with the hash-based variant and 2 seconds with the polynomial-commitment variant.
