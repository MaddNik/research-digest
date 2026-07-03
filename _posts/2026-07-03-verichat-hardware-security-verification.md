---
title: "VeriChat: An Agentic Conversational AI Assistant for Hardware Security Verification"
date: 2026-07-03 08:30:00 +0200
categories: [Hardware Security]
tags: [hardware-verification, agentic-ai, formal-verification, aes-implementation]
link: https://arxiv.org/abs/2607.01668
byline: "Saha et al. (arXiv:2607.01668, Thu 02 Jul 2026)"
description: "A retrieval-augmented, multi-agent conversational assistant helps hardware engineers with security verification and autonomously found and proved a covert vulnerability in an AES S-Box design."
---

The paper introduces VeriChat, a specialized conversational AI assistant built to support hardware security verification, a process that normally requires engineers to manage intricate design reviews, threat analysis, and verification workflows. General-purpose chatbots pose risks in this setting because they can fabricate information or rely on outdated knowledge, so VeriChat instead uses a retrieval-augmented, multi-agent workflow in which three specialized agents collaborate to reduce hallucinated answers and increase response trustworthiness. The system integrates open-source electronic design automation tools, including Icarus Verilog, Yosys, and SymbiYosys, to perform code validation, synthesis evaluation, simulation, and formal verification directly on hardware description language designs supplied by the user. In testing, VeriChat achieved a faithfulness score of 87.73 percent, exceeding leading proprietary chatbot alternatives on this metric. A case study shows the system autonomously identifying and formally proving a covert vulnerability in an AES S-Box design through ordinary conversational interaction.
