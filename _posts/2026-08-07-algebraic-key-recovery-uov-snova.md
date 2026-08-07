---
title: "Extending the Applicability of Algebraic Key Recovery Attacks on the UOV Signature Scheme"
date: 2026-08-07 08:07:00 +0200
categories: [PQC]
tags: [multivariate, uov, snova, cryptanalysis]
link: https://eprint.iacr.org/2026/1620
byline: "Yasuhiko Ikematsu and Hiroki Furue (IACR ePrint 2026/1620, Aug 5 2026)"
description: "New algebraic key recovery attacks extend beyond a limitation of prior work on the UOV signature family and reduce the estimated security of certain SNOVA parameter sets to roughly 2 to the 103rd power operations."
---

This paper extends the applicability of algebraic key recovery attacks against the Unbalanced Oil and Vinegar (UOV) signature scheme and its variants. Earlier algebraic key recovery attacks were unable to function once the number of vinegar variables was at least twice the number of public polynomials. The authors present a method that overcomes this restriction by identifying and exploiting additional kernel elements that appear in that regime. Applying the extended attack to parameter sets of SNOVA, a UOV-family scheme in NIST's post-quantum standardization process, the authors demonstrate reduced security levels for certain configurations. Specifically, they report that one NIST security level I parameter set for SNOVA has an estimated security of only about 2 to the power of 103 gate operations, which is notably below its intended security target.
