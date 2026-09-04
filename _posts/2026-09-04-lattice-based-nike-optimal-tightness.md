---
title: "Lattice-based NIKE with optimal tightness"
date: 2026-09-04 08:09:00 +0200
categories: [PQC]
tags: [non-interactive-key-exchange, learning-with-errors, tight-reduction, lattice-based]
link: https://eprint.iacr.org/2026/1845
byline: "Roman Langrehr et al. (IACR ePrint 2026/1845, Aug 31 2026)"
description: "A new lattice-based non-interactive key exchange scheme achieves a security reduction whose loss is only linear in the number of users, improving on the quadratic loss of all prior lattice-based NIKE schemes, and the authors prove this loss is optimal."
---

This paper presents a new variant of non-interactive key exchange (NIKE) based on the learning with errors assumption, with a security reduction whose loss is only linear in the number of users, improving on every prior reduction for lattice-based NIKE schemes, which had quadratic loss. The tight reduction covers both the setting with super-polynomial modulus-to-noise ratio and negligible correctness error, and the more challenging setting with polynomial modulus-to-noise ratio and inverse-polynomial correctness error. The authors also prove a matching lower bound on tightness for a natural class of lattice-based NIKE schemes that captures all existing variants, showing their security loss is optimal up to constant factors. This is described as the first tightness lower bound for lattice-based NIKE, generalizing an earlier bound by Hesse, Hofheinz, and Kohl from Crypto 2018 that did not apply to lattice-based constructions. A major revision of this work appeared at TCC 2026.
