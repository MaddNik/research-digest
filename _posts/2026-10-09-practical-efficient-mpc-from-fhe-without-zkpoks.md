---
title: "Practical and Efficient MPC from FHE, without ZKPoKs"
date: 2026-10-09 08:30:00 +0200
categories: [Cryptography]
tags: [secure-multiparty-computation, fully-homomorphic-encryption, malicious-security]
link: https://eprint.iacr.org/2026/2403
byline: "Kelong Cong et al. (IACR ePrint 2026/2403, Oct 7 2026, CIC 2026)"
description: "A simplified FHE-based MPC protocol removes the zero-knowledge proofs of knowledge required by prior work, making the security proof simpler and more modular."
---

Fully homomorphic encryption enables low-round, low-communication multiparty computation protocols that are secure against static malicious corruptions, and this paper builds on an idea from the full version of Smart's FHE-based MPC protocol to completely remove the need for zero-knowledge proofs of knowledge in that construction. The resulting simplification makes the final security proof of the MPC protocol considerably simpler and more modular than the original. The new protocol relies on an FHE scheme equipped with an encrypted pseudorandom function functionality, and the authors formalize the security notion required of such encrypted PRFs. As an additional contribution, they prove that a recent encrypted PRF construction from Deo et al. is secure under this formal model, supporting the practicality of the simplified MPC protocol.
