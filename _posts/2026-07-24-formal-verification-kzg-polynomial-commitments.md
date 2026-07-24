---
title: "On the Formal Verification of Polynomial Commitments: two KZG constructions and the Algebraic Group Model"
date: 2026-07-24 08:19:00 +0200
categories: [Cryptography]
tags: [kzg, polynomial-commitments, formal-verification, algebraic-group-model]
link: https://eprint.iacr.org/2026/1490
byline: "Tobias Rothmann (IACR ePrint 2026/1490, Jul 21 2026)"
description: "A machine checked formalization in Isabelle/HOL of security proofs for the standard and batched KZG polynomial commitment schemes under the algebraic group model."
---

The paper formalizes polynomial commitment schemes and gives reusable definitions of correctness, binding, hiding, and knowledge soundness inside the Isabelle/HOL proof assistant. It introduces a constraint programming inspired approach to formalize the algebraic group model itself. Using the CryptHOL framework and Shoup's sequence of games methodology, the author verifies security proofs for both the standard KZG commitment and a batched KZG variant. The author states this is the first formalization of polynomial commitment schemes, the first formalization of the algebraic group model, and the first formal verification of security proofs for a concrete polynomial commitment scheme. The work is intended as groundwork for later formal verification of pairing based zero-knowledge proof systems that build on KZG.
