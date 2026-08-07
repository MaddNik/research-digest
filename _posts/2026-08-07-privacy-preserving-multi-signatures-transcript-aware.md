---
title: "Privacy-Preserving Multi-Signatures: Achieving Transcript-Aware Privacy"
date: 2026-08-07 08:20:00 +0200
categories: [Cryptography]
tags: [signature-scheme, multi-signature, privacy]
link: https://eprint.iacr.org/2026/1574
byline: "Yanzibo Zhou et al. (IACR ePrint 2026/1574, Aug 3 2026)"
description: "A MuSig2-based multi-signature construction that preserves signer privacy even when the signing transcript itself is exposed over a public channel, a threat model prior schemes did not account for."
---

The authors identify a gap in existing multi-signature privacy notions, which do not consider that the transcript of the signing protocol can be observed on public channels, potentially leaking signer identities even when the final signature looks private. They introduce "transcript-aware privacy" to capture this stronger requirement and present a construction based on MuSig2-H. The scheme achieves UNF-3 unforgeability in the algebraic group model plus random oracle model under the discrete logarithm assumption, and preserves full signer privacy in the signature-only setting. In the transcript-aware setting the scheme achieves a weaker "set privacy" guarantee, revealing only the size of the signer set while keeping individual identities hidden. The paper also gives a concrete realization of the key-aggregation proof sharing procedure conducted over public channels.
