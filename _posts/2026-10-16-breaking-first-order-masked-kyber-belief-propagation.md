---
title: "Breaking First-Order Masked Kyber with Belief Propagation Alone"
date: 2026-10-16 08:30:00 +0200
categories: [Hardware Security]
tags: [power-analysis, masked-kyber, belief-propagation, side-channel-attack]
link: https://eprint.iacr.org/2026/2448
byline: "Vahid Jahandideh and Lejla Batina (IACR ePrint 2026/2448, Oct 12 2026)"
description: "A belief-propagation solver recovers the full secret key of a first-order masked Kyber768 implementation on an ARM Cortex-M4 from about 2,200 power traces using only authentic ciphertexts."
---

The authors recover the long-term key of a first-order masked Kyber768 implementation on an ARM Cortex-M4 from about 2,200 decapsulation power traces, using only authentic ciphertexts that pass the usual ciphertext-validity checks, by combining weak second-order leakage from both arithmetic shares even though the secret is freshly re-shared before every decapsulation. A profiled neural network estimates Hamming-weight distributions for the two shares of each noisy message coefficient, and these are combined into likelihoods on the decryption noise, a known affine function of the secret key and the public-key error, which a belief-propagation solver accumulates across traces while an Onsager correction compensates for feedback between factors. The solver recovers all 1,536 secret and error coefficients without any lattice reduction, whereas at the same trace budgets a least-squares estimator performs no better than guessing all zeros and a greedy inequality solver fails even with exact Hamming weights. The authors also show that a primal-lattice cascade attack does not reduce the required number of traces, since below the belief-propagation recovery threshold its output stays too diffuse for practical lattice recovery, and that belief-propagation-derived hints only lower the estimated BKZ block size from 624 to 505 at 2,000 traces, still leaving the lattice attack impractical on its own.
