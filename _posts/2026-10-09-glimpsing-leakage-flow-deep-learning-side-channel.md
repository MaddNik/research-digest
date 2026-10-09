---
title: "Glimpsing the Leakage Flow for Deep Learning-Based Side-Channel Analysis using Stochastic Leakage Model"
date: 2026-10-09 08:34:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, deep-learning, explainability]
link: https://eprint.iacr.org/2026/2358
byline: "Trevor Yap and Shivam Bhasin (IACR ePrint 2026/2358, Oct 5 2026, CASCADE 2027)"
description: "GlimpseDNN gives layer-by-layer, interpretable visualizations of how deep neural networks extract side-channel leakage from traces, revealing leakage even when it is not visible in the raw signal."
---

Deep learning has become the dominant method for profiled side-channel analysis, successfully recovering secret keys even against strong countermeasures, but deep neural networks remain largely black boxes, and evaluators do not know what leakage information is extracted and used across the network's layers. The authors introduce GlimpseDNN, a model-agnostic framework that provides layer-by-layer visualizations of how deep neural networks process physical leakage traces to achieve key recovery, built around a stochastic leakage model that both learns complex leakage behavior and remains interpretable through its learned weights. They validate the framework on simulated traces and on public datasets including ASCADf, ASCADr, and desynchronized ASCADf variants. Notably, they show that even when leakage is not visible in the original traces, GlimpseDNN can still find it by examining deeper layers of a well-trained network, giving evaluators a way to glimpse the underlying leakage and identify implementation vulnerabilities that inform more side-channel-resistant hardware design.
