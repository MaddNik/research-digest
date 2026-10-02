---
title: "Chinese NGCC Algorithms: The First Week of AI Cryptanalysis"
date: 2026-10-02 08:09:00 +0200
categories: [PQC]
tags: [ngcc, ai-cryptanalysis, standardization, vulnerability-disclosure]
link: https://eprint.iacr.org/2026/2266
byline: "Markku-Juhani O. Saarinen (IACR ePrint 2026/2266, Sep 29 2026)"
description: "A week of largely AI-assisted cryptanalysis against China's new NGCC post-quantum competition surfaced 191 findings, 78 of them rated Critical, across 89 of the 119 candidates."
---

On September 20, 2026, the Chinese Institute of Commercial Cryptography Standards opened its Next-generation Commercial Cryptographic Algorithms program with 119 first-round candidates, 34 signature schemes, 41 key encapsulation mechanisms, 9 key exchange protocols, and 35 hash functions, following the template of the open NIST competitions for AES, SHA-3, and post-quantum cryptography. The author reports that during the first seven days of the competition, harvested sources show 191 active findings published against 89 candidates, 78 of them rated Critical, covering universal forgeries, signing-key recovery, trivial hash collisions, broken implicit rejection, and seeds too short for the claimed security level. The author's own independent evaluation effort, using an agentic AI workflow described in the paper, discovered, verified, and disclosed 110 of those issues, 47 of them Critical, with the remainder found by other researchers, some also AI-assisted. Early AI-assisted findings mostly targeted implementations, while by the end of the week reproduced AI-assisted attacks also included new design-level key recovery. The paper describes the workflow, review loop, and classification ruleset, and separately benchmarks all candidates, finding that NGCC hash selection can significantly affect final public-key performance because some candidate implementations spend a large share of their cycles on placeholder hash functions.
