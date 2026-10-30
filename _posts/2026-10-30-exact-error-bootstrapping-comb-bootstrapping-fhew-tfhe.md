---
title: "Exact Error Bootstrapping and Comb Bootstrapping in FHEW/TFHE"
date: 2026-10-30 08:18:00 +0200
categories: [FHE]
tags: [tfhe, bootstrapping, blind-rotation, large-plaintexts]
link: https://eprint.iacr.org/2026/2630
byline: "Philippe Chartier and Mohammed Lemou (IACR ePrint 2026/2630, Oct 24 2026)"
description: "A new comb bootstrapping technique that refreshes the encryption error instead of the message modulus speeds up TFHE-rs refresh operations by up to 9.1 times and 8-bit integer multiplication by 6.5 times."
---

In FHEW and TFHE, bootstrapping normally evaluates the decryption function through a blind rotation whose resolution limits the usable message space. This paper instead bootstraps the error: by rounding the ciphertext at a resolution that is a multiple of the message modulus, the message is preserved exactly, and reduction modulo a small integer yields a noise-free encryption of the error that a single blind rotation can lift and subtract exactly, letting the message modulus be constrained solely by the noise rather than by the rotation resolution. Because the error takes far fewer distinct values than the ring degree, a single blind rotation in this comb bootstrap can refresh several ciphertexts simultaneously, and between refreshes an integer stays encrypted in one ciphertext, allowing modular additions and multiplications without programmable bootstrapping. Built on TFHE-rs for 8-bit integers on a single thread, the error refresh is 3.5 times faster than TFHE-rs's own refresh, 9.1 times faster with the comb bootstrap, multiplication is 6.5 times faster, and in a residue number system, multiplication of integers of 2 to the 32 or larger is 19 times faster than in TFHE-rs, though evaluating any function other than a refresh still requires programmable bootstrapping.
