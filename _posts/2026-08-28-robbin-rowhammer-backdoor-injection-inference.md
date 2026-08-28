---
title: "ROBBIN: Rowhammer-Based Backdoor Injection during Inference"
date: 2026-08-28 08:34:00 +0200
categories: [Hardware Security]
tags: [rowhammer, backdoor-attack, dram, fault-injection]
link: https://arxiv.org/abs/2608.23774
byline: "Saion K. Roy et al. (arXiv:2608.23774, Aug 24 2026)"
description: "ROBBIN is a hardware-aware Rowhammer backdoor injection attack that selects DRAM page mappings for model weights based on a target chip's actual, device-specific bit-flip characteristics."
---

Existing Rowhammer-based inference-time backdoor attacks design their bit-flip strategies purely at the algorithmic level, without accounting for the bit-flips that the underlying DRAM hardware will actually produce, causing collateral bit-flips at unintended locations that degrade both attack success rate and normal-input accuracy, with performance varying significantly across different DRAM devices. The authors present ROBBIN, a hardware-aware Rowhammer backdoor injection attack that first characterizes the bit-flip patterns of a target DRAM chip and then uses this information to iteratively select DRAM page mappings for model weights that maximize attack success while preserving accuracy under Rowhammering. By treating every hammering-induced bit-flip as part of the attack design rather than dismissing collateral flips as side effects, ROBBIN produces backdoors that remain robust across devices. Evaluated on ResNet-20 and VGG-16 with CIFAR-10 across three commodity DDR4 chips, ROBBIN consistently achieves close to 90 percent attack success rate while maintaining test accuracy above 83 percent.
