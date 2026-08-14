---
title: "ANTMAN: An Efficient and Interpretable RTL-Level Run-Time Detection Framework for Stealthy Branch Predictor Attacks on BOOM"
date: 2026-08-14 08:31:00 +0200
categories: [Hardware Security]
tags: [branch-predictor-attack, risc-v, rtl-runtime-detection]
link: https://arxiv.org/abs/2608.09498
byline: "Muhammad Hassan et al. (arXiv:2608.09498, Aug 10 2026)"
description: "A hardware-embedded, register-transfer-level runtime monitor detects stealthy branch-predictor side-channel attacks on the BOOM RISC-V processor before secrets are leaked, with zero false positives in evaluation."
---

The paper targets the lack of runtime detection mechanisms for microarchitectural side-channel attacks that exploit branch predictor state on out-of-order RISC-V processors, specifically the BOOM core. ANTMAN is described as a secure-by-design, interpretable, non-intrusive detection framework implemented at the register-transfer level, using association rules extracted offline from predictor behavior and then embedded directly in hardware as an always-on monitor. The framework is designed to terminate execution before a secret can be disclosed, and the authors report zero false positives across their evaluated configurations. A notable claim is generalization: the detector can flag previously unseen variants within the same class of branch-predictor attacks, not just attacks it was explicitly trained on. Evaluation covers both simplified and more complex predictor configurations on the BOOM RISC-V core.
