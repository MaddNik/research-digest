---
title: "Reliable Homomorphic Matching for Fuzzy Labeled PSI at Scale"
date: 2026-07-03 08:14:00 +0200
categories: [FHE]
tags: [private-set-intersection, bfv, soundness-error, fuzzy-matching]
link: https://eprint.iacr.org/2026/1322
byline: "Uzun (IACR ePrint 2026/1322, Fri 26 Jun 2026)"
description: "A new leveled-BFV-based matching kernel for fuzzy labeled private set intersection closes a soundness gap that let per-query false-accept error compound with database size."
---

The paper studies fuzzy labeled private set intersection systems built from a homomorphic set-threshold kernel that combines leveled BFV homomorphic encryption, a garbled circuit, and secret sharing to decide matches under encryption. It identifies a composition gap: the kernel's per-trial false-accept probability compounds across every record in the database, producing what the author calls a realization soundness error that grows with scale even when the plaintext matcher would reject the query. The author formalizes this soundness error as a composable security property, derives a closed-form bound on the receiver's advantage, and introduces CSTPSI, a kernel that runs independent token rounds to close the gap, proven secure in the semi-honest model. Evaluation shows the baseline kernel's soundness error reaches 100 percent at a million records while CSTPSI holds it at 0 in every tested configuration, and CSTPSI is reported as over 20 times faster with up to 93 percent less communication for large labels at moderate scale. A public reproducibility artifact accompanies the paper.
