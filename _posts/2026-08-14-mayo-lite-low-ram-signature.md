---
title: "MAYO Lite: a Low-RAM Implementation of the MAYO Signature Scheme"
date: 2026-08-14 08:14:00 +0200
categories: [PQC]
tags: [mayo-signature, multivariate-cryptography, smart-cards]
link: https://eprint.iacr.org/2026/1634
byline: "Sven Bauer et al. (IACR ePrint 2026/1634, Aug 7 2026)"
description: "MAYO Lite cuts RAM usage for MAYO signature verification by 97 to 99 percent compared to the reference implementation, enabling deployment on smart cards and microcontrollers."
---

MAYO is a multivariate-polynomial-based post-quantum signature candidate, but its reference implementation requires substantial memory that is unavailable on constrained devices such as smart cards. This paper from Siemens AG researchers presents MAYO Lite, an implementation that cuts RAM consumption for signature verification by 97 to 99 percent relative to the reference code, at the cost of increased computation time while keeping code footprint similar. The approach relies on three techniques: expanding the public key incrementally rather than loading it fully into memory, reorganizing matrix computations to avoid redundant operations, and using precomputed values to streamline accumulation steps. The authors benchmark their approach across multiple standard MAYO parameter sets as well as additional variants relevant to ongoing standardization discussions.
