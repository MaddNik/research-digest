---
title: "The supersingular isogeny problem in time and memory p^(1/3+o(1))"
date: 2026-07-24 08:08:00 +0200
categories: [PQC]
tags: [isogeny, supersingular-isogeny-problem, cryptanalysis, parameter-selection]
link: https://eprint.iacr.org/2026/1486
byline: "Benjamin Wesolowski (IACR ePrint 2026/1486, Jul 20 2026)"
description: "A new heuristic algorithm solves the supersingular isogeny problem in time and memory p to the power of one third plus o(1), improving on the prior best complexity of p to the power of one half times a polylogarithmic factor."
---

The paper studies the supersingular isogeny problem, the hard problem underlying isogeny-based post-quantum cryptography. Assuming a plausible heuristic about the smoothness of certain random integers, the author shows the problem can be solved in time and memory on the order of p to the power of one third plus o(1). This beats the previous best known bound of roughly p to the power of one half times a polylogarithmic factor in p. Since this problem's hardness directly determines secure parameter sizes for isogeny-based schemes, the result has direct implications for parameter selection. The author notes that the practical impact depends on clarifying the constant factors hidden in the o(1) exponent and on the real cost of the memory requirements.
