---
title: "High-Precision CKKS with Focal Units"
date: 2026-10-23 08:17:00 +0200
categories: [FHE]
tags: [ckks, bootstrapping, precision, cyclotomic-units]
link: https://eprint.iacr.org/2026/2531
byline: "Jung Hee Cheon and Junho Lee (IACR ePrint 2026/2531, Oct 20 2026)"
description: "Focused CKKS trades unused SIMD slots for precision using focused rescaling and key-switching based on cyclotomic units, giving roughly k times more precision bits when using only a 1/k fraction of the slots at the same cost as an ordinary multiplication."
---

In CKKS, higher precision requires a larger scaling factor, which increases modulus consumption during homomorphic arithmetic and leaves less modulus available after bootstrapping under a fixed modulus budget. The authors introduce Focused CKKS, which trades unused SIMD slots for precision through focused rescaling and key-switching based on cyclotomic units; these units reduce error in selected focus slots while allowing larger error in background slots. Using only a 1/k fraction of the available slots gives approximately k times as many bits of precision at the same scaling factor and CKKS parameter setting, and a high-precision multiplication under this scheme costs the same as an ordinary CKKS multiplication, with each focus slot supported by k-1 background slots; the construction also supports different precision requirements across different slots. The authors further construct a bootstrapping procedure tailored to Focused CKKS in which only the base modulus at the bottom level needs to grow with the target precision, while the remaining bootstrapping computation keeps roughly the same modulus consumption by using fewer slots, and adapting high-precision bootstrapping based on discrete CKKS further reduces this base modulus by approximately the same factor k.
