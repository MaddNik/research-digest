---
title: "AI-Assisted Design of a Post-Quantum Cryptographic Accelerator: A Deployed-Silicon Case Study"
date: 2026-09-04 08:30:00 +0200
categories: [Hardware Security]
tags: [ml-dsa, ml-kem, fpga, verification]
link: https://arxiv.org/abs/2609.04058
byline: "Jungmin Park et al. (arXiv:2609.04058, Sep 3 2026)"
description: "A deployed ML-KEM-768 and ML-DSA-65 FPGA accelerator passed its full known-answer-test regression while carrying a norm check that outran block-RAM latency, and the authors close the gap with a golden-reference oracle driven by 301,343 randomized adversarial data-dependent signings with zero escapes."
---

Post-quantum migration is mandated on published deadlines, and silicon that ships with a defect cannot be patched remotely, but the authors show the standard acceptance gate, known-answer testing, cannot detect an entire class of ML-DSA defects: because ML-DSA signing resamples until a candidate meets its norm bounds, the executed code path varies with the message, while known-answer tests use fixed seed values that only reach the rejection-loop depths those seeds happen to trigger. Their own accelerator passed its full known-answer-test regression while carrying a norm check that outran block-RAM latency, leaving each candidate's final coefficients unverified, an escape that only surfaced at reject-loop iteration 5. To close this gap the authors replace the acceptance gate with a byte-exact golden-reference oracle paired with randomized adversarial soak testing that drives the rejection loop past any fixed test vector, achieving 301,343 data-dependent signings with zero escapes. The paper reports 232 logged experiments in which an agentic large language model drove design of a unified ML-KEM-768 and ML-DSA-65 accelerator with on-chip key custody, from RTL through PCIe bring-up on a single Kintex-7 XC7K160T FPGA at 98.5 percent slice occupancy, with an overall task success rate of 71.6 percent and the deployed baseline surviving the same 779,945-check zero-failure soak test across all six FIPS operations.
