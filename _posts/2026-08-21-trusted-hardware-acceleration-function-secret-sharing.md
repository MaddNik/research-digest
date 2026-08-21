---
title: "Trusted Hardware Acceleration for Function Secret Sharing"
date: 2026-08-21 08:29:00 +0200
categories: [Hardware Security]
tags: [function-secret-sharing, hardware-accelerator, private-information-retrieval, trusted-hardware]
link: https://arxiv.org/abs/2608.16223
byline: "Pengzhi Huang, Kiwan Maeng, and G. Edward Suh (arXiv:2608.16223, Aug 17 2026)"
description: "A trusted hardware accelerator for function secret sharing speeds up secure inference and private information retrieval by generating keys on-device instead of distributing them externally."
---

The paper presents a distributed function accelerator for function secret sharing (FSS), a building block used in privacy-preserving systems such as secure inference and private information retrieval, whose computational cost is normally high. The accelerator pairs a high-throughput pseudorandom generator with a programmable component, and when run in a trusted mode it generates FSS keys on-device rather than requiring an external distribution step, cutting communication and storage overhead. The authors report roughly a tenfold reduction in end-to-end latency for secure inference, up to a twentyfold reduction in communication, more than fivefold energy savings for that workload, and for private information retrieval a fivefold throughput gain with a tenfold energy reduction, all with modest additional hardware area.
