---
title: "Perseus: A Full-Stack System for Homomorphic Model Inference"
date: 2026-11-06 08:16:00 +0200
categories: [FHE]
tags: [fhe-inference, ckks, llm-privacy, open-source]
link: https://arxiv.org/abs/2611.04488
byline: "Alessandro Zirilli et al. (arXiv:2611.04488, Nov 3 2026)"
description: "Perseus is a free, open Python library for end-to-end encrypted model inference that is 3.96 times faster than any other implementation on Llama-3-8B single-token decoding."
---

Fully homomorphic encryption promises to secure remote model inference by letting providers compute on encrypted user data, but it remains slow, and the effort to make it practical has been fragmented across mostly closed-source frameworks. This paper presents Perseus, a free and open Python software library that supports the full stack of encrypted model inference, from the cryptographic backend and data packing through encrypted nonlinearities and end-to-end model execution. Perseus introduces one optimization at each level of the stack: in-kernel regeneration of key-switching keys at the backend level, a complex variant of Cachemir packing at the data level, and a bootstrap placer that is aware of both packing and magnitude at the model level. The library achieves state-of-the-art latency across multiple models and modalities, staying within 3 percent of plaintext accuracy and perplexity, and is 3.96 times faster at single-token decoding than any other implementation on Llama-3-8B. The authors also launch a public speedrun on encrypted GPT-2 so that progress on practical FHE inference can compound.
