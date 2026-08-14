---
title: "Preprocessed Private Function Evaluation: Achieving Sublinear Online Complexity for Lookup Tables"
date: 2026-08-14 08:23:00 +0200
categories: [Cryptography]
tags: [private-function-evaluation, secure-computation, lookup-tables]
link: https://eprint.iacr.org/2026/1631
byline: "Tanping Zhou et al. (IACR ePrint 2026/1631, Aug 7 2026)"
description: "A preprocessed variant of private function evaluation achieves sublinear online query complexity for lookup tables, answering queries over ten times faster than existing approaches."
---

Private function evaluation lets one party obliviously compute a private function on a private input without revealing either the function or the input beyond the output. This work introduces Preprocessed Private Function Evaluation (PPFE), which shifts most computational cost into an offline preprocessing phase so that online queries become sublinear in the table size. For lookup tables of size two to the twenty-fourth power, their construction answers queries in roughly 3 milliseconds, over ten times faster than existing approaches. The authors report the scheme scales well to thousands of adaptive queries, making it practical for repeated table lookups in secure computation applications.
