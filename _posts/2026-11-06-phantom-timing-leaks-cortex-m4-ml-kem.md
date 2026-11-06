---
title: "Phantom Timing Leaks on Cortex-M4: A Pre-registered Evaluation of ML-KEM Decapsulation"
date: 2026-11-06 08:30:00 +0200
categories: [Hardware Security]
tags: [ml-kem, timing-side-channel, constant-time, cortex-m4]
link: https://eprint.iacr.org/2026/2744
byline: "Amadou Tidiane Anne (IACR ePrint 2026/2744, Nov 3 2026)"
description: "A pre-registered dudect-style evaluation finds that all nine tested PQM4 ML-KEM decapsulation implementations on a Cortex-M4 show small but statistically significant timing differences traced mainly to the measurement harness."
---

Fixed-versus-random timing tests in the style of dudect are a cheap first check for constant-time behavior, and on microcontrollers a cycle counter makes them exact to the cycle. This paper reports a pre-registered evaluation of ML-KEM decapsulation on an STM32F411 Cortex-M4, covering nine PQM4 implementations across ML-KEM-512, 768, and 1024, plus a positive control with the pre-KyberSlash division formulas restored, using 44 campaigns of 100,000 trials each with per-trial correctness checking. With invalid ciphertexts, no timing difference is detected in 18 of 18 campaigns while the restored-division control is detected every time, but with fresh valid ciphertexts, all nine implementations show flagged differences of 4 to 15 cycles with very large test statistics; a matched control running identical code before the measured call removes the difference for seven of the nine implementations, while one implementation still shows a large statistic even when both measured classes decapsulate identical bytes. The authors attribute these deterministic few-cycle differences to the measurement harness itself, driven by flash wait states, instruction cache behavior, and prefetching that change depending on the surrounding code. The per-trial correctness checks also exposed a real functional bug in PQM4's ML-KEM-1024 m4fstack implementation, producing 220 wrong shared secrets out of 49,830 trials, which upstream had fixed shortly before this evaluation; all data, binaries, and code are published.
