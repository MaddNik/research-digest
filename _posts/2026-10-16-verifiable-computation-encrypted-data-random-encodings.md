---
title: "Verifiable Computation on Encrypted Data from Homomorphic Encryption over Random Encodings"
date: 2026-10-16 08:19:00 +0200
categories: [FHE]
tags: [verifiable-computation, homomorphic-encryption, blind-proofs, matrix-vector-multiplication]
link: https://eprint.iacr.org/2026/2422
byline: "Jiayi Kang et al. (IACR ePrint 2026/2422, Oct 9 2026)"
description: "A new homomorphic encryption variant over random encodings closes a client-privacy gap in blind proofs for verifiable computation on encrypted data, with only a two-times proving overhead for encrypted matrix-vector multiplication."
---

Verifiable computation on encrypted data lets a client outsource computation while getting both privacy and integrity, and a promising approach called blind proofs uses homomorphic encryption to evaluate verifiable computation proofs on encrypted data. Despite their efficiency, blind proofs do not provide strong client privacy, because a malicious server can run reaction attacks to learn information about the client's inputs, intermediate values, or outputs. This work introduces Homomorphic Encryption over Random Encodings, formalizing a new security notion called indistinguishability under chosen-plaintext attacks in the presence of an equality oracle over encodings, and proves that combining a scheme meeting this notion with blind proofs that verify computation over the encodings yields protocols with strong client privacy. The authors instantiate a scheme for functions of bounded degree d using Shamir secret sharing at d plus 1 evaluation points under d plus 1 distinct homomorphic encryption keys, and demonstrate concrete efficiency for matrix-vector multiplication, a linear computation with degree 1, where the ratio of the prover's runtime to the homomorphic matrix-vector multiplication runtime is as low as two times in their prototype.
