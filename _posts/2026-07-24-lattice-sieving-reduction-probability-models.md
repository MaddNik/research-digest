---
title: "On Reduction Probability Models in Lattice Sieving"
date: 2026-07-24 08:10:00 +0200
categories: [PQC]
tags: [lattice-sieving, cryptanalysis, sphere-model, security-estimates]
link: https://eprint.iacr.org/2026/1465
byline: "Marc Stevens and Michael Yonli (IACR ePrint 2026/1465, Jul 17 2026)"
description: "A refined probabilistic model of lattice sieving shows that practical sieving algorithms achieve reduction probabilities up to 8 times higher than predicted by the standard sphere model."
---

The paper examines how vectors produced by lattice sieving algorithms distribute relative to the sphere model, which is commonly used to predict reduction probabilities in cryptanalysis of lattice problems such as those underlying schemes like ML-KEM. The authors show that practical sieving algorithms outperform the theoretical sphere model predictions by a constant factor as lattice dimension grows. They extend the sphere model to uniform and non-uniform ball variants and find that the input distribution affects only the total reduction probability, not the shape of the output length distribution. Their refined models show reduction probability improvements ranging from 1.5 times to 8 times over the original sphere model. These findings matter for estimating the concrete cost of lattice sieving attacks used to set security parameters.
