---
title: "When the Learning With Errors Problem Meets the Coherent Ising Machine: A Penalty-Free Algorithm-Hardware Co-Design"
date: 2026-06-22 08:15:00 +0200
categories: [Hardware Security]
tags: [post-quantum-cryptography, lattice-cryptanalysis, quantum-hybrid]
link: https://arxiv.org/abs/2606.22843
byline: "Jiang (arXiv:2606.22843, Sat 22 Jun 2026)"
description: "Hybrid quantum-classical LWE solver achieving penalty-free Bounded-Distance-Decoding through Coherent Ising Machine co-design."
---

The Learning With Errors problem forms the mathematical foundation of modern Post-Quantum Cryptography, and its cryptanalysis via lattice reduction, machine learning, and quantum-classical hybrids is essential for assessing PQC security. This work proposes CIM-BDD, a hybrid Bounded-Distance-Decoding solver reducing LWE to a Quadratic Unconstrained Binary Optimization problem through strictly penalty-free mapping. An algebraic elimination of the secret embeds LWE into a q-ary lattice, absorbing the modular arithmetic and recasting as a Closest Vector Problem; the squared error norm is then used directly as the QUBO energy, minimizing cryptographic noise as the objective rather than as a penalized constraint. To realize this on current Noisy Intermediate-Scale Quantum devices, the authors designed a special encoding method: a Continuous Relaxed Babai's Nearest Plane projection drives an adaptive mixed-radix encoder greatly reducing qubit count and QUBO coefficient range. A statistically bounded early-stopping threshold serves as a one-sided certificate and Decision-LWE distinguisher. Validation on the TU Darmstadt LWE Challenge provides end-to-end demonstration for both Search and Decision LWE of a 40-dimensional instance on the Coherent Ising Machine CPQC-550, establishing a new algorithm-hardware co-design paradigm for quantum-classical hybrid cryptanalysis.
