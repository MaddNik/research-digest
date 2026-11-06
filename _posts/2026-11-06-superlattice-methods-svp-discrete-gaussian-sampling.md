---
title: "Superlattice methods for the shortest vector problem and discrete Gaussian sampling"
date: 2026-11-06 08:13:00 +0200
categories: [PQC]
tags: [lattice-cryptanalysis, shortest-vector-problem, discrete-gaussian-sampling, quantum-algorithms]
link: https://eprint.iacr.org/2026/2761
byline: "Minki Hhan et al. (IACR ePrint 2026/2761, Nov 4 2026)"
description: "New superlattice-based algorithms improve the worst-case time and space complexity for solving the shortest vector problem and sampling discrete Gaussians at any width."
---

This paper gives new worst-case algorithms for the shortest vector problem, or SVP, and discrete Gaussian sampling, or DGS, at arbitrary widths, both built by generating lists on a dense superlattice and combining vectors down a chain to the target lattice, using random shifts to control how often each vector is represented. For SVP, the optimized algorithm runs in time 2 to the 0.409n power and space 2 to the 0.259n power, up to subexponential factors, improving on the authors' own prior 2 to the n-over-2 power worst-case bound. For Haar-random lattices, the costs match the known 2 to the 0.292n power time and 2 to the 0.208n power space bounds from prior heuristic work. For quantum SVP, the authors obtain worst-case time and space of 2 to the 0.247n power, improving on the best known heuristic quantum SVP time of 2 to the 0.256n power without relying on heuristic assumptions. For discrete Gaussian sampling at any width with distribution error 2 to the negative kappa power, the algorithm runs in worst-case time 2 to the 0.292n power and space 2 to the 0.208n power, up to polynomial factors in kappa, improving on the previous best cost of 2 to the n power for sampling at arbitrary widths. The authors also derive faster algorithms for approximate SVP and CVP, bounded distance decoding, and estimating the Gaussian mass and smoothing parameter of any lattice, all central to assessing the concrete security of lattice-based post-quantum schemes.
