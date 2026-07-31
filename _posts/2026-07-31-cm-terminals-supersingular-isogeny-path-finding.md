---
title: "Complex-Multiplication Terminals for Supersingular Isogeny Path-Finding"
date: 2026-07-31 08:12:00 +0200
categories: [PQC]
tags: [isogeny, supersingular-curves, path-finding, complex-multiplication]
link: https://eprint.iacr.org/2026/1516
byline: "Zheng Tao et al. (IACR ePrint 2026/1516, Jul 24 2026)"
description: "A new stopping-set construction using complex-multiplication vertices speeds up the subfield-search phase of supersingular isogeny path-finding algorithms."
---

The paper enhances the Delfs-Galbraith style path-finding algorithm by expanding the recognizable terminal set beyond the standard set to include precomputed complex-multiplication vertices, built from roots of Hilbert class polynomials over finite fields with bounded discriminant parameters. This added terminal set is shown to grow asymptotically as the bound to the power three halves, with negligible overlap with the standard terminal set and negligible added per-step overhead. The authors provide procedures to convert a search that ends at a complex-multiplication vertex into a complete isogeny path. Experimental results show the method reduces both the number of visited vertices and the number of computational multiplications while remaining practical at cryptographic parameter sizes.
