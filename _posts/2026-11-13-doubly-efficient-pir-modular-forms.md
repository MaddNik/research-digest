---
title: "Doubly-Efficient Private Information Retrieval from Modular Forms"
date: 2026-11-13 08:28:00 +0200
categories: [Cryptography]
tags: [private-information-retrieval, modular-forms, matching-vectors]
link: https://eprint.iacr.org/2026/2836
byline: "Alexandra Henzinger, Seyoon Ragavan (IACR ePrint 2026/2836, Nov 9 2026)"
description: "New information-theoretic doubly-efficient private information retrieval protocols cut server storage to essentially one extra bit per database bit while improving server query time for three or more servers."
---

The authors present new information-theoretic protocols for s-server, doubly-efficient private information retrieval in sublinear server time with only one extra bit of storage per database bit on the servers, for every constant number of servers s of 2 or more. On an n-bit database, each server first builds and stores a preprocessing data structure of n plus 1 bits, unique to that server, after which it may discard the original database, and then answers a query by reading at most a bounded number of bits of its data structure. In the two-server setting, the protocols achieve server time on the order of n to the power of 0.82, matching the state of the art from Henzinger and Ragavan's EUROCRYPT 2026 work while shrinking storage from roughly n times the square root of log n bits to n plus 1 bits. With three or more servers, the protocols keep the n plus 1 bit storage while improving server time over all prior information-theoretic schemes with near-linear storage, for example achieving time on the order of n to the power of 0.74 with three servers and n to the power of 0.61 with ten servers, compared to n to the power of 0.79 and n to the power of 0.75 previously. The results build on matching-vector techniques generalized to handle degree-two computations in the exponent, introducing an intermediate abstraction called Fourier-sparse cone-delta functions that the authors construct through a connection to modular forms and complex analysis.
