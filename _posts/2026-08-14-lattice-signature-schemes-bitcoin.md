---
title: "Lattice-based Signature Schemes for Bitcoin"
date: 2026-08-14 08:09:00 +0200
categories: [PQC]
tags: [bitcoin, dilithium, falcon, hawk]
link: https://eprint.iacr.org/2026/1628
byline: "Dmytro Zakharov et al. (IACR ePrint 2026/1628, Aug 6 2026)"
description: "A self-contained survey of Dilithium, Falcon, and Hawk evaluates lattice-based signatures as a post-quantum replacement for Bitcoin's discrete-logarithm signatures."
---

Written by researchers at Blockstream Research, this paper reviews three lattice-based signature schemes as candidates for transitioning Bitcoin to post-quantum security, developing all necessary background so readers need no prior lattice cryptography knowledge. It highlights that combined signature and public key sizes can fall below 1.6 kilobytes for some schemes, alongside robust underlying security assumptions and algebraic structure with potential for future threshold or multi-signature functionality. The authors discuss practical Bitcoin deployment concerns, including on-chain footprint, long-term security for dormant funds, Falcon's reliance on floating-point operations, and wallet key derivation. Hawk is retained in the analysis despite having been withdrawn from NIST standardization following a key-recovery attack, since the authors consider its design paradigm still of independent interest.
