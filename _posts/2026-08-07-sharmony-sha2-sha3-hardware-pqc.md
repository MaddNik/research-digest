---
title: "SHARMONY: Composing SHA-2 and SHA-3 Hardware for Crypto-Agile PQC"
date: 2026-08-07 08:31:00 +0200
categories: [Hardware Security]
tags: [hardware-implementation, hash-hardware, fpga]
link: https://eprint.iacr.org/2026/1572
byline: "Liga Anwar et al. (IACR ePrint 2026/1572, Jul 31 2026)"
description: "SHARMONY is a unified FPGA hardware architecture that shares components between SHA-2 and SHA-3 implementations to reduce area while supporting crypto-agile post-quantum cryptography."
---

Different standardized post-quantum cryptography schemes rely on either SHA-2 or SHA-3 and SHAKE hash primitives, motivating a combined hardware design that can support both efficiently. SHARMONY shares area-critical components between the two hash families, including a 25 by 64-bit register bank, round-constant storage, and unified padding and control logic, while remaining compliant with FIPS 180-4 and FIPS 202. It also adds a duet execution mode that uses the otherwise unused upper half of a 64-bit datapath to process two independent SHA-224 or SHA-256 streams in parallel, which benefits Merkle-tree-based constructions used in hash-based post-quantum schemes. Implemented on an Artix-7 FPGA, the design uses 5873 lookup tables and 2310 flip-flops and reaches 1959 megabits per second throughput for SHA-256, a 100 to 152 percent improvement over the SHA-256 engines in SLotH, Sphincslet, OpenTitan, and Caliptra. Compared to combined designs built from separate SHA-2 and SHA-3 implementations, SHARMONY reduces lookup table usage by an average of 40 percent and flip-flop usage by an average of 55 percent.
