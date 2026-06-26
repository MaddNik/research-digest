---
title: "Self-Sifting quantum key distribution"
date: 2026-06-25 08:12:00 +0200
categories: [Cryptography]
tags: [quantum-key-distribution, quantum-cryptography, bell-states]
link: https://arxiv.org/abs/2606.27299
byline: "Sarshar & Annabestani (arXiv:2606.27299, Wed 25 Jun 2026)"
description: "Two-way QKD protocol delaying sifting operations preventing mode-dependent attacks and enabling eavesdropper detection."
---

Quantum key distribution protocols typically perform sifting operations publicly, which can enable mode-dependent attacks from adversaries with knowledge of communication settings. This work introduces a novel two-way quantum key distribution protocol where Alice and Bob use one qubit from a maximally entangled Bell state as their quantum channel for key exchange. The protocol features a security mechanism based on a scrambling operator, with critical sifting operations postponed until after quantum communication completes and performed solely by Bob. Since the control mode is never publicly announced, attacks relying on mode-dependent adaptations or attempting to remain hidden within the control mode are inherently prevented. The traveling qubit does not directly encode key information, limiting information extraction from quantum channel attacks. Notably, ordinarily-discarded communication rounds can detect eavesdroppers. The authors comprehensively analyze ancilla-based attacks and demonstrate their detectability through this protocol design.
