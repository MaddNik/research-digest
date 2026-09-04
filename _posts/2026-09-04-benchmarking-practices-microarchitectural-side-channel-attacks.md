---
title: "Practice Makes (Im)Perfect: A Look Back at Benchmarking Practices for Microarchitectural Side-Channel Attacks"
date: 2026-09-04 08:28:00 +0200
categories: [Hardware Security]
tags: [microarchitectural-side-channels, benchmarking, reproducibility, covert-channels]
link: https://arxiv.org/abs/2609.03893
byline: "Iliana Fayolle et al. (arXiv:2609.03893, Sep 3 2026)"
description: "A survey of 83 microarchitectural side-channel attack papers from 2014 to 2024 identifies 19 recurrent benchmarking flaws, finding an average of 5.5 flaws per paper even at top-tier security and architecture venues."
---

Microarchitectural side-channel research has grown rapidly, increasing the need for rigorous benchmarking, but early attack papers relied on indirect proxies such as covert-channel bandwidth or key-recovery on naive AES and RSA implementations, and many subsequent papers kept replicating these de facto standards even though such benchmarks may not be the most relevant way to assess a new primitive's specific properties. The authors note that microarchitectural attacks are notoriously sensitive to experimental conditions, so minimal changes to a target system can significantly alter outcomes, meaning inadequate evaluation practices undermine reproducibility and the validity of comparisons even in top-tier venues. Surveying 83 attack papers published in top-ranked security and architecture conferences from 2014 to 2024, the authors identify and define 19 recurrent benchmarking flaws affecting evaluation completeness, relevance, soundness, and reproducibility, including unfair or absent comparisons, missing code or materials, and failure to evaluate key attack properties, finding an average of 5.5 such flaws per paper. Based on these findings, the authors propose key properties for properly evaluating new microarchitectural side-channel attacks and highlight trends over time and differences in practice between security and architecture conferences.
