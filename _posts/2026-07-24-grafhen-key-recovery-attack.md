---
title: "A Practical Key-Recovery Attack on GRAFHEN"
date: 2026-07-24 08:15:00 +0200
categories: [FHE]
tags: [cryptanalysis, key-recovery, group-based-fhe, noise-free-fhe]
link: https://eprint.iacr.org/2026/1460
byline: "Jules Dumezy (IACR ePrint 2026/1460, Jul 17 2026)"
description: "The paper presents a practical key-recovery attack on GRAFHEN, a group-based fully homomorphic encryption scheme without noise."
---

GRAFHEN is a fully homomorphic encryption scheme built on group actions over symmetric groups and designed to avoid the noise growth typical of lattice-based FHE. This paper introduces an equivalent-key recovery framework for GRAFHEN instances and a practical attack called HEnbane. The attack recovers generators using bounded congruence closure, direct cancellation procedures, and conflict-driven search over partial permutation tables. The authors show that the published count of about 2 to the power 101 equivalence classes is not itself an attack-cost estimate at the recommended parameters, implying the scheme's real security is lower than the nominal count suggests. This is a cryptanalysis result rather than a new construction or accelerator.
