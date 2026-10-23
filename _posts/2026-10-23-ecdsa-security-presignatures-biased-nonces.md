---
title: "A Note on the Security of ECDSA with Presignatures or Biased Nonces"
date: 2026-10-23 08:26:00 +0200
categories: [Cryptography]
tags: [ecdsa, threshold-signatures, nonce-bias, fine-grained-complexity]
link: https://eprint.iacr.org/2026/2545
byline: "Geoffroy Couteau and Nikolaos Makriyannis (IACR ePrint 2026/2545, Oct 20 2026, Asiacrypt 2026)"
description: "The security of several deployed ECDSA variants used for faster distributed signing is shown to be equivalent, in the generic group and random oracle model, to the average-case hardness of the k-SUM problem from fine-grained complexity."
---

Several ECDSA security experiments have been proposed over the years to enable faster distributed signing, but these variants are not known to reduce to the standard ECDSA security game, and recent work by Groth and Shoup at Eurocrypt 2022 showed that some are vulnerable, particularly when combined with raw signing of hash digests and additive key derivation. Despite this, several such variants are implemented in public libraries and used in commercially deployed products without sound security foundations. This note revisits the security landscape of these alternative ECDSA modes of operation, showing as its main result that the security of some variants used in the wild is equivalent, in the generic group and random oracle model, to a standard conjecture from fine-grained complexity on the average-case hardness of the k-SUM problem. The authors complement this with lower bounds, conditioned on fine-grained complexity conjectures, on the running time of generic group model attacks against other standard modes of operation analyzed by Groth and Shoup, providing what they describe as a complete picture of the security landscape of ECDSA variants and an unexpected connection to old and new conjectures from fine-grained complexity.
