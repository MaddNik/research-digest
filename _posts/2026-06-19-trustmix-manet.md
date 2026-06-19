---
title: "TrustMix: How to Mix Messages in a Mobile Ad-hoc Network"
date: 2026-06-19 08:14:00 +0200
categories: [Cryptography]
tags: [mix-network, anonymity, linkable-ring-signatures, random-oracle-model]
link: https://arxiv.org/abs/2606.20251
byline: "Yu Shen et al. (arXiv:2606.20251, Jun 18 2026)"
description: "A mix protocol for mobile ad-hoc networks that needs no central trusted authority and proves anonymity in the random oracle model."
---

TrustMix is a mix protocol for mobile ad-hoc networks that requires no trusted central
authority. Users locate nearby trusted parties and forward messages through group-based
routing structures to achieve anonymity, with message shuffling at each group stage. The
design ensures that compromised participants cannot break anonymity unless every member of
a group is adversarial. Rate limiting is enforced using linkable ring signatures, which
detect excessive message transmission while preserving user privacy. Security is proven in
the random oracle model, and a proof-of-concept Android implementation across five devices
demonstrates practical throughput and improved anonymity.
