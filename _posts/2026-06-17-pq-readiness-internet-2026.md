---
title: "Measurement Study of Post-Quantum Readiness of Internet: 2026"
date: 2026-06-17 08:18:00 +0200
categories: [PQC]
tags: [cryptography, software-engineering, post-quantum, networking]
link: https://arxiv.org/abs/2606.16473
byline: "Vanishka Mohan Dubey et al. (arXiv:2606.16473, Jun 15 2026)"
description: "A large-scale measurement of hybrid post-quantum key exchange and certificate adoption across more than 32,000 internet domains."
---

This empirical study evaluates the post-quantum readiness of internet TLS
deployments by examining 32,011 domains across multiple sectors. The authors report
that 15.70 percent of domains, especially in critical sectors such as banking and
government, still rely on TLS 1.2. They find that 49.3 percent of domains support
hybrid post-quantum key exchange mechanisms while 50.7 percent continue to use
classical approaches. Notably, they observe zero percent adoption of hybrid
post-quantum certificates, leaving authentication infrastructure exposed to quantum
threats. The authors conclude that migration must cover both key exchange and
certificates to defend against harvest-now-decrypt-later attacks and reach full
quantum resilience.
