---
title: "Finding a Shortest Vector and More in $2^{n/2+o(n)}$ Time using $q$-ary Coset Difference Tree"
date: 2026-09-04 08:13:00 +0200
categories: [PQC]
tags: [shortest-vector-problem, closest-vector-problem, lattice-cryptanalysis, coset-difference-tree]
link: https://eprint.iacr.org/2026/1859
byline: "Minki Hhan (IACR ePrint 2026/1859, Sep 2 2026)"
description: "A new randomized algorithm solves the exact shortest vector problem for n-dimensional lattices in 2 to the n over 2 time and space using a q-ary coset difference tree inspired by Wagner's generalized birthday algorithm."
---

This paper gives a new randomized algorithm for the exact shortest vector problem that runs in time and space 2 to the n over 2 for an n-dimensional lattice. The algorithm can be viewed as a q-ary analogue of the midpoint Hessian technique for an odd prime q, exploiting the fact that the gradient of the periodic Gaussian function at v over q is nearly proportional to a shortest vector v, even after aggregation over a relatively large random affine coset. The relevant coset gradient is computed along a chain of intermediate lattices using a combinatorial procedure inspired by Wagner's generalized birthday algorithm, which yields the stated time and space complexity. A variant of the algorithm also solves the exact closest vector problem with a distance guarantee within the same time and space bounds for random targets and random lattices drawn from the Haar-Siegel measure, giving another route to faster lattice cryptanalysis relevant to the security estimates of lattice-based schemes.
