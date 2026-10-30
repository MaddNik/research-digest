---
title: "On the Inapplicability of Residue-Confined Error Attacks to CRT-FHE with Non-Degenerate Error Distributions"
date: 2026-10-30 08:17:00 +0200
categories: [FHE]
tags: [crt-fhe, rlwe, cryptanalysis-rebuttal, error-distribution]
link: https://eprint.iacr.org/2026/2633
byline: "Anil Kumar Pradhan (IACR ePrint 2026/2633, Oct 24 2026)"
description: "This rebuttal shows that a previously claimed key-recovery attack on CRT-based FHE relies on a deliberately degenerate, effectively zero-error instantiation, and does not apply when the scheme uses its intended centered-binomial error distribution."
---

This paper responds to a cryptanalysis claiming key recovery and plaintext recovery against a CRT-based fully homomorphic encryption scheme the author introduced in earlier work. The author demonstrates that the reported recovery attack relies entirely on a deliberately constructed error distribution whose support lies in the kernel of the CRT encoding function, which makes the effective encryption error identically zero and reduces the attacked construction to a noiseless RLWE instance. Under the scheme's intended centered-binomial error distribution, the probability that an entire error polynomial falls into the encoder's kernel is shown to be negligible at the reported parameters, so the degenerate attack does not transfer to properly noise-bearing CRT-FHE ciphertexts. The author concludes that the earlier key-recovery and plaintext-recovery results concern only the artificial zero-error instantiation and do not demonstrate a practical security compromise of CRT-FHE under its intended error sampling.
