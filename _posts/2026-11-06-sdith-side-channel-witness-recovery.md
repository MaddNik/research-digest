---
title: "Syndrome Decoding out of the Head: Structure-Aided Side-Channel Witness Recovery on SDitH"
date: 2026-11-06 08:35:00 +0200
categories: [Hardware Security]
tags: [sdith, side-channel-analysis, code-based-signatures, power-analysis]
link: https://eprint.iacr.org/2026/2760
byline: "Jaeyeon Lee, Jaeho Jeon, and Young-Sik Kim (IACR ePrint 2026/2760, Nov 4 2026)"
description: "A profiled power analysis combined with the structural constraints of regular syndrome decoding fully recovers the secret witness of the SDitH code-based signature scheme from a single trace per key."
---

Regular syndrome decoding underlies several code-based signature schemes, including SD-in-the-Head, or SDitH, whose secret witness has exactly one nonzero coordinate per block, with the selected positions required to satisfy a public syndrome equation. This paper shows how these structural constraints can be exploited to recover a complete witness even from imperfect side-channel information, by training convolutional neural networks on a profiled power analysis of the witness-embedding operation in the SDitH Round 3 reference implementation to classify the mux digits encoding each regular block and rank candidate positions. To correct errors in these neural network predictions, the authors combine the rankings with the public syndrome and the regularity constraints, formulating recovery as an affine correction system with block-validity constraints, and develop a quotient-syndrome decoder that identifies blocks whose true position falls outside the initial candidate list without needing to exhaustively enumerate block subsets. Evaluated on an ARM Cortex-M4 using measured power traces with a single target trace per key, the attack recovers all 100 test witnesses under -Os compiler optimization using 4,000 profiling traces, and 91 out of 100 under -O3 optimization using 16,000 profiling traces, with every successful recovery matching all 616 serialized witness bits.
