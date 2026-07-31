---
title: "CHARGE: Leveraging CWE Hierarchies for Hardware Security SystemVerilog Assertion Generation"
date: 2026-07-31 08:31:00 +0200
categories: [Hardware Security]
tags: [hardware-verification, soc-security, llm-assisted-security]
link: https://arxiv.org/abs/2607.27776
byline: "Xiao Tan et al. (arXiv:2607.27776, Jul 30 2026)"
description: "CHARGE uses CWE weakness hierarchies combined with a large language model to automatically generate SystemVerilog security assertions for unverified RTL modules, without requiring trusted design specifications."
---

Verifying that RTL hardware designs are free of security weaknesses typically requires manually written formal properties, which is labor intensive and depends on trusted specifications that may not exist for third-party or legacy IP. CHARGE instead uses the hierarchical structure of Common Weakness Enumeration entries together with a large language model to identify security-critical assets in a module and infer expected security behavior, generating SystemVerilog assertions directly from the RTL. Tested on the Hack at DAC 2018, 2019, and 2021 system-on-chip benchmark designs, CHARGE detected 27 of 42 known bugs, with 89 percent of generated assertions running successfully in Cadence JasperGold formal property verification and 92.2 percent being non-vacuous. Notably, CHARGE-generated properties caught three bugs that manually written properties had missed and identified a previously undiscovered bug in the Hack at DAC 2021 OpenPiton system-on-chip. An extended version of this work was accepted to IEEE and ACM ICCAD 2026.
