---
title: "TensorZKP: Repurposing GPU Tensor Cores for High-Performance Zero-Knowledge Proofs"
date: 2026-06-17 08:26:00 +0200
categories: [Cryptography]
tags: [zero-knowledge, gpu-acceleration, snark, implementation]
link: https://eprint.iacr.org/2026/1250
byline: "Tao Lu et al. (IACR ePrint 2026/1250, Jun 13 2026)"
description: "The first GPU framework to map zero-knowledge proof computation onto Tensor Cores by reformulating proof modules as matrix multiplication tasks."
---

GPU Tensor Cores are specialized units for accelerating matrix multiplication and
have driven recent AI performance gains, yet existing GPU implementations of
zero-knowledge proofs rely exclusively on general-purpose SIMT cores and leave
Tensor Cores untapped. TensorZKP is presented as the first GPU framework to harness
Tensor Cores for proof acceleration, addressing the challenge that these cores are
designed for low-precision matrix multiplication. To bridge this gap the authors
develop Tensor-Core-compatible finite field arithmetic and reformulate proof
modules, specifically sum-check protocols and the Spielman code, into matrix
multiplication tasks. They further design an asynchronous warp-specialized framework
that pipelines memory access, Tensor Core matrix operations, and SIMT-based modular
reductions. The optimizations are instantiated with HyperPlonk as the polynomial
interactive oracle proof and Brakedown as the polynomial commitment scheme for
end-to-end proof generation. At a 2 to the 25 scale, the underlying building blocks
complete in fractions of a millisecond for operations such as inner product and
scalar-vector multiplication.
