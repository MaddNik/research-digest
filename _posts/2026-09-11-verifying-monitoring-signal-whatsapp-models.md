---
title: "From Specs to Apps: Verifying and Monitoring Models of Signal and WhatsApp"
date: 2026-09-11 08:20:00 +0200
categories: [Cryptography]
tags: [signal-protocol, runtime-monitoring, tamarin, formal-verification]
link: https://arxiv.org/abs/2609.11882
byline: "Moustafa Said et al. (arXiv:2609.11882, Sep 10 2026)"
description: "A runtime monitoring framework checks that live WhatsApp Web and Signal Desktop sessions conform to formal Tamarin models of the Signal protocol, uncovering undocumented differences between libsignal and WhatsApp's fork."
---

The Signal protocol secures communication for billions of users through WhatsApp and the Signal app, and its formal security guarantees are well studied in the computational and Dolev-Yao settings, but a gap remains between those guarantees and how implementations actually behave at runtime. The authors bridge this gap by applying SpecMon, a runtime monitor, to check whether observed executions of WhatsApp Web and Signal Desktop conform to formal protocol models, instrumenting both applications to capture their network and cryptographic interactions and building two multiset-rewrite models compatible with the Tamarin prover. They derive the first model of WhatsApp Web's implementation of the Signal protocol and the most detailed model to date of Signal's original protocol, and use monitoring to verify authentication and secrecy properties for the protocol's core components. The monitoring also reveals previously undocumented differences between the original libsignal library and WhatsApp's fork, and the authors show their approach detects deliberately injected security faults with low overhead.
