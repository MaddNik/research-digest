---
title: "Domain-Invariant and Language-Model-Assisted Acoustic Side-Channel Attacks on Keyboards"
date: 2026-11-13 08:35:00 +0200
categories: [Hardware Security]
tags: [acoustic-side-channel, keystroke-inference, language-models]
link: https://arxiv.org/abs/2611.13922
byline: "Bikrant Bikram Pratap Maurya (arXiv:2611.13922, Nov 10 2026)"
description: "A domain-invariant acoustic model combined with language-model correction is shown to recover typed text from keystroke sounds even across unseen keyboards, users, noisy environments, and compressed audio channels."
---

Acoustic side-channel attacks recover typed text from the sound of keystrokes using only a commodity microphone and no access to the victim's device, and prior work established that such attacks succeed under idealized laboratory conditions, such as a single keyboard, a fixed microphone, a quiet room, and matched training and testing devices. This work asks whether keystroke inference survives the open world of unseen keyboards, diverse users, noisy environments, and compressed transmission channels, which matters for assessing real security risk. The author's answer is that it does survive these conditions, provided the acoustic model is made explicitly domain-invariant and its noisy predictions are corrected by a language model. The paper develops this domain-invariant, language-model-assisted approach as a way to recover text from keystroke acoustics under realistic, non-idealized conditions.
