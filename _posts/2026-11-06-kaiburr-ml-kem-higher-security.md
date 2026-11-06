---
title: "Kaiburr: ML-KEM at (much) higher security"
date: 2026-11-06 08:14:00 +0200
categories: [PQC]
tags: [ml-kem, lattice-cryptography, parameter-selection, frodokem]
link: https://eprint.iacr.org/2026/2730
byline: "Swechchha Adhikari, Vadim Lyubashevsky, and Peter Schwabe (IACR ePrint 2026/2730, Nov 3 2026)"
description: "Kaiburr generalizes ML-KEM's noise distribution so it can scale to much higher MLWE security levels than simply increasing the module rank allows."
---

As standardized post-quantum cryptography is deployed, engineers continue to debate concrete parameter choices, including whether to favor structured-lattice ML-KEM, unstructured-lattice FrodoKEM, or hybrid combinations of post-quantum schemes. This paper investigates how to scale ML-KEM to much higher security levels of the underlying module learning-with-errors problem, observing that simply increasing the module rank quickly runs into a decryption-failure-probability limit. The authors propose a generalization of the noise distribution that allows scaling to much larger module rank and MLWE hardness while preserving ML-KEM's core structure, including its arithmetic modulo 3329 in a polynomial ring reduced modulo X to the 256th power plus 1, and its simple, constant-time secret and noise generation. They select three concrete parameter sets for this high-security variant, called Kaiburr, and present benchmarks for optimized implementations on 64-bit Intel CPUs and on the Asymmetric Cryptography Coprocessor of the open-source Pavona silicon framework. Based on these benchmarks, they argue that a hybrid of FrodoKEM-976 and Kaiburr-1792 offers both better performance and protection against a broader range of hypothetical future attacks than FrodoKEM-1344 alone.
