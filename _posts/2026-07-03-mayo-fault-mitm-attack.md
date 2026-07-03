---
title: "Fault assisted Man-In-The-Middle Attack on MAYO"
date: 2026-07-03 08:25:00 +0200
categories: [Hardware Security]
tags: [fault-injection, post-quantum-signatures, multivariate-cryptography, key-recovery]
link: https://eprint.iacr.org/2026/1327
byline: "Shinde et al. (IACR ePrint 2026/1327, Fri 26 Jun 2026)"
description: "A single injected fault during MAYO key generation lets an attacker fully recover the secret oil matrix and transparently forge signatures as a man-in-the-middle."
---

This paper targets the key-generation step of MAYO, a post-quantum multivariate signature scheme, rather than the more commonly studied signing step. By injecting one fault into the computation of a specific public-key component, the authors force the resulting public key into a simplified linear relationship with the secret oil matrix. From that faulty public key they build an overdetermined linear system over a finite field that fully recovers the oil secret. Because the attack corrects the faulty public key afterward, the victim's counterpart never sees anything wrong, letting the adversary act as an undetected man-in-the-middle that produces valid signatures on the victim's behalf. The attack was demonstrated on a fault-simulated MAYO implementation, illustrating that key-generation routines, not just signing routines, are a meaningful fault-attack surface for multivariate cryptography.
