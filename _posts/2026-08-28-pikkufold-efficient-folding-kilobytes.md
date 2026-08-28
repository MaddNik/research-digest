---
title: "PikkuFold: Efficient Folding in a Few Kilobytes"
date: 2026-08-28 08:28:00 +0200
categories: [Cryptography]
tags: [lattice-based-folding, succinct-proofs, johnson-lindenstrauss, avx-512]
link: https://eprint.iacr.org/2026/1809
byline: "Michał Osadnik (IACR ePrint 2026/1809, Aug 26 2026)"
description: "PikkuFold is a lattice-based folding protocol that communicates only 5.5 kilobytes per folding step, far less than state-of-the-art schemes such as Cyclo and SALSAA."
---

Folding is a powerful technique for building efficient succinct proof systems for streaming-style computations, and the author presents PikkuFold, a lattice-based folding protocol that improves on state-of-the-art schemes such as SALSAA and Cyclo. One folding step communicates 5.5 kilobytes beyond the commitments to its fresh inputs, compared to at least 30 kilobytes for Cyclo and at least 60 kilobytes for SALSAA on similar instances, while keeping prover time comparable and verification in the millisecond range. The construction is built on layered random projections whose algebraic structure is fast to verify and whose final image is short enough to send directly to the verifier, cutting out the cost of auxiliary commitments, and PikkuFold is the first lattice-based folding construction that requires no in-protocol commitments beyond those of the fresh inputs. The paper also contributes a Johnson-Lindenstrauss theorem for biased ternary matrices modulo q with certified concrete constants, replacing prior heuristic parametrizations, and a detailed analysis of a short-challenge sampler with fixed Hamming weight and operator-norm rejection that the author suggests could improve a wide family of lattice-based protocols as a drop-in replacement.
