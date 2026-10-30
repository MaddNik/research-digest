---
title: "Mikros: Bitwidth-Aware SNARKs over Extensions of Small Fields"
date: 2026-10-30 08:29:00 +0200
categories: [Cryptography]
tags: [snark, extension-fields, bitwidth-aware-proofs, zero-knowledge]
link: https://eprint.iacr.org/2026/2646
byline: "Mingshu Cong (IACR ePrint 2026/2646, Oct 26 2026)"
description: "Mikros packs witness vectors over a small base field into vectors over a degree-kappa extension field, producing the first bitwidth-aware permutation argument and a SNARK prover up to 2.55 times faster than the prior state of the art."
---

SNARK provers normally perform arithmetic over a large field for soundness even when witness entries are only a few bits wide, inflating both prover time and memory, and while recent work has made individual SNARK components bitwidth-aware, it covers only part of the prover and typically exploits binary-field structure specifically. Mikros is a framework for end-to-end bitwidth-aware SNARK construction based on algebraic vector packing, which packs length-N vectors over a base field into length-m vectors over a degree-kappa extension field, turning length-N relations over the base field into length-m relations over the extension field and making existing linear-time extension-field protocols bitwidth-aware. This unifies previously separate bitwidth-aware inner-product proofs, Hadamard-product proofs, and polynomial commitment schemes, and yields the first bitwidth-aware grand-product proof and hence the first bitwidth-aware permutation argument, composing into bitwidth-aware SNARKs for circuit satisfiability over extensions of arbitrary small fields. Although Mikros does not rely on binary-field structure, its prover is 2.19, 2.55, and 1.85 times faster on batches of 256 SHA-256 compressions, Keccak permutations, and BLAKE3 compressions respectively than Flock, the prior state-of-the-art bitwidth-aware SNARK over binary-extension fields.
