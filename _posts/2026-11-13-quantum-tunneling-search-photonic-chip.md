---
title: "Non-Convex Optimization via Quantum Tunneling Search on a Photonic Chip"
date: 2026-11-13 08:03:00 +0200
categories: [Photonics]
tags: [photonic-computing, waveguide-arrays, optimization, analog-simulation]
link: https://arxiv.org/abs/2611.16791
byline: "Xi-Jun Yuan et al. (arXiv:2611.16791, Nov 12 2026)"
description: "A femtosecond-laser-written waveguide chip implements a quantum tunneling search algorithm that finds local and global minima of non-convex landscapes faster than classical stochastic gradient descent."
---

Non-convex optimization is central to modern machine learning, since many real-world objective functions or constraints are non-convex, and the resulting landscapes of local minima and saddle points hinder gradient descent-based methods from finding global optima. The authors present quantum tunneling search (QTS), an algorithm based on a quantum tunneling walk and local annealing that explores non-convex landscapes by exploiting the quantum tunneling effect. They map an objective function onto the potential term of a waveguide Hamiltonian by controlling the refractive index with femtosecond direct laser writing, and measure average probability distributions on 10 micrometer spaced waveguide arrays of 29 by 1 and 21 by 9 sites to reveal local minima of various one-dimensional and two-dimensional non-convex landscapes. Introducing a varying Hamiltonian approach further improves the search efficiency and allows identification of the global minimum. The work experimentally verifies that QTS is an effective non-convex optimization solver and demonstrates quantum speedups over classical stochastic gradient descent, serving as a practical application of near-term analog quantum simulators to machine learning.
