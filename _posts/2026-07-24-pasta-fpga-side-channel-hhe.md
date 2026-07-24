---
title: "From PQC to HHE: Reusing a Co-Design Platform for Side-Channel-Protected PASTA"
date: 2026-07-24 08:16:00 +0200
categories: [FHE]
tags: [hybrid-fhe, pasta-cipher, transciphering, side-channel-protection, fhe-fpga]
link: https://eprint.iacr.org/2026/1485
byline: "Ahmet Malal et al. (IACR ePrint 2026/1485, Jul 20 2026)"
description: "The paper reuses a post-quantum cryptography hardware and software co-design platform to build a side-channel-protected FPGA accelerator for the PASTA cipher used in hybrid homomorphic encryption."
---

Hybrid homomorphic encryption lets a constrained client send compact symmetric ciphertexts while a server transciphers them into homomorphic ciphertexts, making HE-friendly symmetric ciphers such as PASTA practical. The authors reuse an existing post-quantum cryptography co-design platform to implement PASTA operations through an FPGA accelerator on an Artix-7 device. They add first-order arithmetic masking to protect the design against side-channel attacks. The masked and unmasked implementations achieve speedups of about 9.85 times and 9.68 times respectively over a software-only baseline. Test vector leakage assessment with 100,000 traces shows no first-order leakage from the masked multiplication.
