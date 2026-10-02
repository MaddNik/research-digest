---
title: "ML-DSA masking sweetened with SUCRE: Shuffle-and-Unmask Countermeasure for REjection sampling"
date: 2026-10-02 08:37:00 +0200
categories: [Hardware Security]
tags: [ml-dsa, masking, side-channel-countermeasure, module-lwr]
link: https://eprint.iacr.org/2026/2248
byline: "Sonia Belaïd et al. (IACR ePrint 2026/2248, Sep 28 2026, TCHES 2026)"
description: "SUCRE masks and randomly permutes ML-DSA's rejection sampling step at once, giving four to six times faster masked execution than the prior Coron et al. countermeasure."
---

The authors present SUCRE, a countermeasure designed to physically protect the rejection sampling step of ML-DSA, one of NIST's standardized post-quantum signature schemes, against side-channel attacks. At its core is a masking gadget that securely unmasks a vector while simultaneously applying a random permutation of its coefficients, a lightweight mechanism that preserves the vector's infinity norm so rejection sampling can proceed as usual without any complex mask conversions. The authors formally prove that a d-probing adversary can learn at most some permuted set of rejected values, information they show should remain insufficient to endanger the signature scheme's security, with the security argument resting on a new variant of the Module Learning with Rounding assumption for which they give a dedicated concrete security analysis relative to the standard MLWR assumption. Their implementation of SUCRE runs four to six times faster than the masked non-bitsliced rejection-sampling implementation of Coron et al. from TCHES 2024, at the cost of higher memory usage, and since rejection sampling accounts for roughly 25 percent of total runtime in masked ML-DSA implementations, the speedup could meaningfully improve efficiency as ML-DSA is adopted on embedded platforms. The paper is a minor revision of an article published in TCHES 2026.
