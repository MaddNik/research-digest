---
title: "Levis: Extension-Free Multi-Key Fully Homomorphic Encryption in the Plain Model"
date: 2026-10-02 08:19:00 +0200
categories: [FHE]
tags: [multi-key-fhe, plain-model, gsw, cofactor-compatibility]
link: https://eprint.iacr.org/2026/2263
byline: "Baoyu Li, Binwu Xiang, and Kang Yang (IACR ePrint 2026/2263, Sep 29 2026)"
description: "A new technique called Cofactor Compatibility removes the costly ciphertext-extension step from plain-model multi-key FHE, giving up to 139-fold evaluation speedups."
---

Multi-key fully homomorphic encryption lets computation run over ciphertexts encrypted under independently generated keys, and Min, Park, and Song recently gave the first RLWE-based MKFHE scheme in the plain model, meaning without trusted or interactive setup, at CRYPTO 2026. That construction requires extending each local compact GSW ciphertext into a joint-key GSW-like ciphertext before evaluation, costing O(d k squared) gadget products per input for k parties and gadget length d. The authors first construct Levis-fast, an extension-free MKFHE scheme in the plain model that eliminates this O(d k squared) cost using a new technique called Cofactor Compatibility, which establishes a common projective decryption relation across ciphertexts encrypted under independently generated local keys so they can be evaluated homomorphically without the extension step. They further give a compact variant, Levis-small, that cuts the communication of each fresh ciphertext from O(d k squared) to O(d) ring elements using only a lightweight lifting operation. A proof-of-concept implementation shows that for k equal to 2, 4, and 8 parties, Levis-fast achieves evaluation speedups of 67.7, 52.8, and 139.4 times over the prior scheme, while Levis-small cuts communication by 2.5 to 14.2 times and still speeds up evaluation by 11.8 to 54.4 times.
