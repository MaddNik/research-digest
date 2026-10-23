---
title: "GKS FHE: Security Analysis"
date: 2026-10-23 08:18:00 +0200
categories: [FHE]
tags: [private-key-fhe, security-analysis, encrypted-search]
link: https://eprint.iacr.org/2026/2523
byline: "John Graham et al. (IACR ePrint 2026/2523, Oct 19 2026)"
description: "This paper presents a formal security analysis of the private-key Gribov-Kahrobaei-Shpilrain (GKS) fully homomorphic encryption scheme, which requires no bootstrapping, produces bit-exact decryption, and supports native encrypted search."
---

All traditional encryption schemes share a fundamental operational vulnerability in that encrypted data must be decrypted before use, and fully homomorphic encryption (FHE) eliminates this by enabling computation directly on encrypted data, though existing FHE schemes impose practical constraints that limit deployment. This paper presents a formal security analysis of the Gribov-Kahrobaei-Shpilrain (GKS) private-key FHE scheme, which the authors note requires no bootstrapping or de-linearization, produces bit-exact decryption, supports native encrypted search, and scales to unbounded depth. The paper is categorized by the authors as an analysis of attacks and cryptanalysis, indicating a focus on assessing the scheme's security properties rather than introducing a new construction. Given GKS's distinctive combination of bootstrapping-free operation and exact, bit-level decryption, this security analysis is a relevant data point for evaluating alternative, less conventional approaches to fully homomorphic encryption.
