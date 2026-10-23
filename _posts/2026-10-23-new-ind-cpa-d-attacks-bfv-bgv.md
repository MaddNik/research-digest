---
title: "New IND-CPA-D Attacks on BFV and BGV"
date: 2026-10-23 08:19:00 +0200
categories: [FHE]
tags: [bfv, bgv, ind-cpa-d, key-recovery]
link: https://eprint.iacr.org/2026/2546
byline: "Hyeongmin Choe et al. (IACR ePrint 2026/2546, Oct 19 2026, ACM CCS 2026)"
description: "Three new attacks on heuristically parameterized BFV and BGV break IND-CPA-D security, with one implemented in OpenFHE fully recovering the secret key in a few minutes to a few hours."
---

IND-CPA-D security extends IND-CPA security to settings where the computation result is known to the adversary, a situation relevant to fully homomorphic encryption and necessary for FHE with threshold decryption. This work presents three new attacks on the BFV and BGV FHE schemes under this threat model when their parameters use heuristic assumptions commonly adopted to enable correctness. The first extends bootstrapping failure attacks from Cheon et al. at CCS 2024 on the DM/CGGI and CKKS schemes to both BFV and BGV, focusing on BGV instantiated with the powerful-basis representation of ring elements; the second skews the BFV ciphertext noise by crafting plaintexts for which the heuristic noise bounds for plaintext-ciphertext multiplication do not hold, outpacing those bounds; and the third skews the mask part of a BFV ciphertext by adding a random encryption of zero with a sufficiently large mask norm, outpacing noise growth in ciphertext-ciphertext multiplication. The first two attacks recover the secret key while the third instead breaks IND-CPA-D indistinguishability, and experiments using the HElib and OpenFHE libraries show the second attack, implemented in OpenFHE, fully recovers the secret key in a few minutes to a few hours depending on parameters.
