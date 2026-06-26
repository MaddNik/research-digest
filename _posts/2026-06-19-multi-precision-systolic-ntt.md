---
title: "Low-Cost Multi-Precision Systolic Arrays for Accelerating FHE NTTs on AI ASICs"
date: 2026-06-19 08:08:00 +0200
categories: [FHE]
tags: [hardware-acceleration]
link: https://arxiv.org/abs/2606.19866
byline: "George Alexakis et al. (arXiv:2606.19866, Jun 18 2026)"
description: "A modified systolic array that natively reconstructs full-precision output, letting AI ASICs run high-precision FHE NTTs faster."
---

This work targets a mismatch between AI accelerators and fully homomorphic encryption:
tensor processing units are optimized for 8-bit arithmetic, whereas FHE and its critical
Number Theoretic Transform demand high precision. The authors propose a modified systolic
array architecture that performs full-precision output reconstruction natively within the
array rather than relying on costly external handling. A synthesized 7-nanometer design is
reported. For transform sizes from 2 to the 12th power up to 2 to the 16th power on
128-by-128 matrix engines, the approach achieves at least a 1.33 times speedup. The result
lets existing AI matrix hardware be reused for FHE workloads with lower cost.
