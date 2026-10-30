---
title: "SPA: Structure-Preserving Approximation of Gated Activations under FHE"
date: 2026-10-30 08:23:00 +0200
categories: [FHE]
tags: [ckks, polynomial-approximation, gelu, encrypted-inference]
link: https://arxiv.org/abs/2610.32065
byline: "Rui Li, Wenyuan Wu, and Weijie Miao (arXiv:2610.32065, Oct 23 2026)"
description: "SPA exploits the shared algebraic structure of GELU, SiLU, and Swish-style activations to approximate only their even residual as a polynomial in x squared, achieving up to a 10.40 times speedup over prior CKKS methods at comparable or lower error."
---

Nonlinear activation evaluation remains a major bottleneck for neural network inference under fully homomorphic encryption, since FHE supports efficient addition and multiplication but lacks native support for exponentials, reciprocals, or value-dependent selection, forcing costly high-degree polynomial approximations. The authors observe that several widely used activations, including GELU, SiLU, fixed-parameter Swish, and the scalar nonlinear branches of GEGLU and SwiGLU, share the algebraic structure A(x) = x times g(x) where g(negative x) = 1 minus g(x). Their method, SPA, retains the exact odd component x/2 and approximates only the even residual as a polynomial in x squared, removing redundant odd degrees of freedom and yielding a comparison-free arithmetic kernel that enables lower-cost polynomial evaluation at a given error target. Plaintext experiments on Gemma-4-E2B and Llama-3.2-3B show SPA largely preserves downstream task performance without weight updates, and on fixed-interval CKKS benchmarks over the range negative 5 to 5, SPA-balanced achieves a 3.25 times speedup over a recent method for erf-GELU at comparable error, SPA-accurate achieves 79.22 percent lower root mean squared error and a 10.40 times speedup over another recent method for QuickGELU, and for SiLU, SPA-accurate achieves 19.02 percent lower root mean squared error and a 2.06 times speedup over a third recent method.
