---
title: "ToolPulse: Side-Channel Eavesdropping on Tool-Using LLM Agents"
date: 2026-11-20 08:29:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, cache-attacks, llm-agents, flush-reload]
link: https://arxiv.org/abs/2611.25470
byline: "Zihao Dan et al. (arXiv:2611.25470, Nov 19 2026)"
description: "A cache-based side-channel framework reconstructs the tool-execution workflow of commercial LLM agents by monitoring shared system libraries on the user's own machine."
---

Large language model agents increasingly translate user requests into sequences of local tool invocations, but prior cache-based side-channel attacks on locally deployed models assumed the attacker shares model components or hardware resources with the victim's inference process, an assumption that does not hold when commercial LLMs run remotely on vendor-controlled infrastructure. The authors observe that agentic execution still exposes a practical attack surface because the tools themselves run on the user's machine and commonly rely on shared system libraries, even though inference itself is remote. They systematically evaluate Flush+Reload and Prime+Probe for monitoring agentic tool invocations across three hardware platforms, finding that Flush+Reload enables accurate, real-time tool monitoring while Prime+Probe, despite supporting cross-VM attacks, incurs prohibitive overhead and suffers from cache-set aliasing. Building on this, they present ToolPulse, a cache-based side-channel eavesdropping framework that uses a Tool Recovery Attack to reconstruct an agent's tool-execution workflow, evaluated on 11 LLMs across Codex and Claude Code with the lowest F1 score exceeding 93 percent. They further demonstrate a Task Profiling Attack that infers user intent across Terminal-Bench task categories and a Trigger Localization Attack that identifies sensitive tool calls such as encryption and decryption or model training and inference, both of which keep high accuracy even under substantial system noise on a server shared by about 20 users.
