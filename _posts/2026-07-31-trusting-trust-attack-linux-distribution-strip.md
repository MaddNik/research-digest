---
title: "Trusting-Trust Attack against an Entire Linux Distribution through Binary Manipulation"
date: 2026-07-31 08:27:00 +0200
categories: [Hardware Security]
tags: [supply-chain, reproducible-builds, toolchain-attack]
link: https://arxiv.org/abs/2607.24888
byline: "Julien Malka et al. (arXiv:2607.24888, Jul 27 2026)"
description: "The authors construct a full trusting-trust attack using GNU strip, an ordinary ELF-manipulating build utility rather than a compiler, that persists through the NixOS bootstrap and backdoors nearly every binary in a built graphical installer."
---

Ken Thompson's classic trusting-trust attack is usually considered specific to compilers, since a compromised compiler can insert and self-propagate a backdoor into everything it builds, including future copies of itself. This paper shows the same class of attack is possible with GNU strip, a utility that only manipulates already-compiled ELF binaries and never inspects or generates source code. By tampering with a single strip binary in the NixOS binary seed used to bootstrap the whole distribution, the payload propagates across successive generations of strip and survives into the final standard build environment even after the tampered seed leaves the dependency closure. On a real nixpkgs revision the attack successfully builds a complete graphical installer, backdooring almost all of its binaries and enabling malicious control of the affected packages. This demonstrates that supply-chain trust assumptions in reproducible-build toolchains extend well beyond compilers to any binary-manipulating build tool.
