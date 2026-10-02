---
title: "Coordinated Electromagnetic Side-Channel Attacks for Voter-Ballot Linking: A Case Study of the Brazilian E-Polling System"
date: 2026-10-02 08:40:00 +0200
categories: [Hardware Security]
tags: [em-side-channel, e-voting, software-defined-radio, voter-privacy]
link: https://arxiv.org/abs/2609.32988
byline: "Leandro Hyeda et al. (arXiv:2609.32988, Sep 26 2026)"
description: "A two-adversary electromagnetic attack reconstructs the vote shown on an e-voting machine's display and links it to the voter who cast it, demonstrated through-wall against the Brazilian e-voting interface."
---

The authors show how two coordinated adversaries, named Eve and Mallory, can combine an electromagnetic side-channel attack to reconstruct the vote displayed on an e-voting machine and link that vote to a specific voter. In their scenario, Eve has access to a place adjacent to the e-polling room, such as a restroom or unsupervised room, and reconstructs the displayed vote by intercepting unintended electromagnetic emanations associated with the video signal, while Mallory observes when the targeted voter is voting and reports this over the Internet to Eve. To validate the most critical stage of the attack, the authors conduct a software-defined radio experiment using the official Brazilian e-voting interface and demonstrate through-wall vote reconstruction, though they use conventional monitors rather than official electronic voting machines. The findings are offered as insight into information forensics and as support for security recommendations to government authorities responsible for e-voting systems.
