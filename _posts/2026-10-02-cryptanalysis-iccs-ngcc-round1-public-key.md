---
title: "Cryptanalysis of the ICCS NGCC Round-1 Public-Key Candidates"
date: 2026-10-02 08:10:00 +0200
categories: [PQC]
tags: [ngcc, public-key, design-flaws, ind-cca]
link: https://eprint.iacr.org/2026/2232
byline: "Zhenyu Xiong and Mingsheng Wang (IACR ePrint 2026/2232, Sep 27 2026)"
description: "An AI-assisted design-level review of 84 public-key submissions to China's NGCC competition finds eight unfixable flaws echoing familiar pitfalls from NIST PQC standardization."
---

The ICCS Next-Generation Commercial Cryptography round-1 call received 84 public-key candidates for public evaluation, and the authors present a design-level assessment targeting weaknesses that no local code fix can close. They identify eight such flaws, each recurring a pitfall already known from NIST PQC standardization: reducible-ring sub-ring projections that break IND-CPA security below the claimed level, public data that inadvertently fixes a value meant to stay secret and enables public-key-only forgery or keyless decapsulation, static-key reuse without a chosen-ciphertext transform, and rejection sampling whose sign handling leaks an equivalent signing key. All of the findings were obtained with AI assistance, and the authors release artifacts supporting the analysis on GitHub. The paper is explicitly framed as independent verification work feeding into the broader NGCC round-1 evaluation process.
