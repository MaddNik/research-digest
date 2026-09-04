---
title: "Enhanced Differential-Linear Cryptanalysis of ChaCha Based on Bit Puncturing"
date: 2026-09-04 08:24:00 +0200
categories: [Cryptography]
tags: [chacha, differential-linear-cryptanalysis, stream-cipher, bit-puncturing]
link: https://eprint.iacr.org/2026/1837
byline: "Xinhai Wang et al. (IACR ePrint 2026/1837, Aug 30 2026, IEEE Internet of Things Journal)"
description: "A new guessed-key covering technique and refined ReBitP framework give the best known key-recovery attacks on 7- and 7.5-round ChaCha256, up to 6.12 times faster than prior attacks."
---

ChaCha is one of the most widely deployed symmetric ciphers, underpinning the security of protocols and platforms including TLS 1.3, SSH, Noise, WireGuard, S/MIME 4.0, Linux, Android, Chromium and Chrome, Firefox, and Safari. This paper introduces a guessed-key covering technique that identifies partitioning-based functions whose required key bits are already covered by those guessed for bit-puncturing-based functions, letting the two be processed jointly, and builds on it a refined differential-linear cryptanalysis framework for ChaCha called ReBitP, which combines bit puncturing, partitioning, and a two-phase distillation strategy. The key idea is to fold a carefully chosen set of partitioning-technique functions with different tail lengths into the first phase without needing to guess additional key bits, giving early filtering that lowers both the first phase's time cost and the second phase's distillation-table construction cost. Applying ReBitP, the authors present enhanced key-recovery attacks on 7- and 7.5-round ChaCha256 with time complexities of 2 to the 142.08 and 2 to the 242.02 respectively, which are 2 to the 6.12 and 2 to the 1.58 times faster than the previous best attacks and are described as the best known key-recovery attacks on those round counts. The paper is a minor revision published in the IEEE Internet of Things Journal.
