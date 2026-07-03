---
title: "Refined Evaluation Methods of Decryption Failure Rate in Lattice-Based Public-Key Encryption with Message Encoding"
date: 2026-07-03 08:13:00 +0200
categories: [PQC]
tags: [lattice-based-encryption, decryption-failure-rate, barnes-wall-lattices, error-analysis]
link: https://eprint.iacr.org/2026/1350
byline: "Zhou et al. (IACR ePrint 2026/1350, Tue 30 Jun 2026)"
description: "A more precise mathematical framework tightens decryption-failure-rate bounds for lattice-based encryption schemes that use message encoding."
---

Decryption failure rate is a critical correctness and security metric for lattice-based public-key encryption, but the paper argues that most existing evaluation methods for schemes with message encoding rely on oversimplified assumptions and rough approximations that produce loose or inaccurate bounds. The authors propose a refined framework covering two decoding paradigms. For Maximum Likelihood Decoding schemes, they characterize the minimal vectors of Barnes-Wall lattices to derive tighter union bounds by exploiting encoding lattice structure. For Bounded Distance Decoding schemes, they introduce a method based on the noncentral chi-squared distribution to model mixed Gaussian and discrete noise, replacing less accurate pure Gaussian approximations. They further extend the framework to algebraic-lattice-based encryption by analyzing the variance and correlation of polynomial product coefficients, proposing a weighted chi-squared distribution with saddlepoint approximation for correlated coefficients. The methods are validated on representative lattice-based schemes including CNTR.
