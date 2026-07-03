---
title: "Shorter Hash-based Signatures via Bucket Thinning"
date: 2026-07-03 08:08:00 +0200
categories: [PQC]
tags: [hash-based-signatures, slh-dsa, sphincs-plus, signature-compression]
link: https://eprint.iacr.org/2026/1328
byline: "Ren et al. (IACR ePrint 2026/1328, Sat 27 Jun 2026)"
description: "A bucket-thinning technique shrinks the few-time signature layer of SPHINCS-plus-style schemes, producing shorter hash-based signatures in most parameter settings."
---

SLH-DSA, the standardized stateless hash-based signature scheme built on the SPHINCS-plus framework, has well-understood security but comparatively large signatures. Building on recent forced-pruning work that reduces the size of the few-time signature component but relies on a conservative cover bound, this paper introduces BPORS+FP, a bucket-thinned variant of the PORS+FP construction. It places independent PORS child keys under an outer FORS-like bucketing layer, and for each selected child key reduces the number of prior uses via binomial thinning, which lets the SPHINCS-plus level cover term be evaluated at a smaller effective use count and creates room for smaller parameters. The construction combines this thinning effect with a global forced-pruning size threshold. The evaluation reports shorter signatures than plain PORS+FP in five of six standard SPHINCS-plus parameter rows, with the 128-bit fast row as the one exception.
