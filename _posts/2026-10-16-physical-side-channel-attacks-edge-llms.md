---
title: "Physical Side-Channel Attacks on Edge LLMs: Extracting Output Tokens and User Prompts"
date: 2026-10-16 08:33:00 +0200
categories: [Hardware Security]
tags: [electromagnetic-side-channel, edge-llm, prompt-extraction, hardware-leakage]
link: https://arxiv.org/abs/2610.14215
byline: "Najeh Alhalawani et al. (arXiv:2610.14215, Oct 9 2026)"
description: "Electromagnetic side-channel measurements collected during on-device LLM inference on a Raspberry Pi 5 let attackers recover generated tokens and reconstruct user prompts without touching the software."
---

Running large language models on edge devices is largely motivated by privacy concerns about sending sensitive user data to cloud servers, but this paper shows that keeping inference local does not eliminate privacy risk, since an adversary with physical access can exploit hardware leakage to recover sensitive information without modifying the software at all. The authors present an electromagnetic side-channel attack targeting LLaMA-3.2-1B-Instruct running on a Raspberry Pi 5, demonstrating that EM traces collected during inference leak both generated tokens and user prompts. A profiling attack identifies generated tokens among 50 medical and privacy-related keywords with 97.2 percent accuracy, a reconstruction attack recovers the model's hidden representations to predict tokens from the full 128,000-token vocabulary with 94.3 percent accuracy on profiled classes and, for unseen words, ranks the correct token within the top 100 of the vocabulary in 67 percent of cases with a median rank of 54. A further hidden-state inversion attack uses the recovered hidden state to reconstruct user prompts semantically, and all of these attacks require only passive EM measurements and a limited number of training traces, showing that local execution alone does not guarantee confidentiality of generated tokens or user inputs.
