---
title: "Parameter-efficient neural computing with programmable photonic meshes"
date: 2026-10-23 08:01:00 +0200
categories: [Photonics]
tags: [photonic-computing, programmable-photonics, tensor-networks, neural-networks]
link: https://arxiv.org/abs/2610.26429
byline: "Artem Popov et al. (arXiv:2610.26429, Oct 19 2026)"
description: "Programmable photonic meshes with electronically tuned interferometer phases can match or beat compressed tensor-train neural network layers while using fewer trainable parameters."
---

Memory capacity and data movement are growing bottlenecks for neural-network computing, which motivates compact, parameter-efficient representations. The authors propose implementing such representations in programmable photonic meshes, where compact electronic parameters set the interferometer phases while optical interference produces a dense, generally high-rank transformation. Because the parameterization stays electronic, its dimensionality and structure can be changed without altering the optical circuit itself, unlike prior photonic approaches tied to a specific tensor factorization. Numerical end-to-end training experiments show that these photonic layers match or outperform strongly compressed tensor-train and brickwork layers, often with fewer trainable parameters, and experiments in parameter-efficient fine-tuning of a language model show advantages over established digital adapters. The reduced trainable state lowers persistent memory requirements and points toward reduced data movement and bandwidth demands for photonic neural-network hardware.
