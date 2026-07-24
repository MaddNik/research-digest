---
title: "Mu-qt-PEGASIS: Interactive Aggregate Signatures from Effective Isogenies in the Programmable Random-Oracle Model"
date: 2026-07-24 08:11:00 +0200
categories: [PQC]
tags: [isogeny, aggregate-signatures, class-group-action, pegasis]
link: https://eprint.iacr.org/2026/1474
byline: "Nouhou Abdou Idris and Mustapha Hedabou (IACR ePrint 2026/1474, Jul 19 2026)"
description: "A compiler builds interactive aggregate signatures from the qt-PEGASIS isogeny-based class-group action, achieving aggregate signature size that scales as O(t), independent of the number of signers."
---

The authors build an interactive aggregate signature scheme from qt-PEGASIS, an effective isogeny-based class-group action construction. They note that the torsor structure of the public-key space blocks the standard Schnorr-style or BLS-style verification equations used in conventional aggregate signatures, so they split verification into two layers: proof-authentication for public-key registration and aggregation, and transcript-consistency for the final aggregated signature. The scheme operates in the programmable random-oracle model and achieves MU-EUF-CMA security under the hardness of the Group Action Inverse Problem plus random-oracle assumptions. The resulting aggregate signature size is O(t), where t is a security-related parameter, independent of the number of signers being aggregated.
