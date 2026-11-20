---
title: "Byzantine Agreement with Signature Tokens"
date: 2026-11-20 08:20:00 +0200
categories: [Cryptography]
tags: [byzantine-agreement, quantum-cryptography, consensus, fault-tolerance]
link: https://eprint.iacr.org/2026/2890
byline: "Yuval Efron et al. (IACR ePrint 2026/2890, Nov 13 2026)"
description: "Byzantine agreement with a finite number of quantum signature tokens per party can beat the classical one-third fault-tolerance bound, reaching honest majority with logarithmically many tokens."
---

The authors study the power and limitations of quantum cryptography in distributed consensus protocols by examining Byzantine agreement in partial synchrony when each party has access to a finite number of signature tokens. Classically, this problem is solvable only when fewer than one-third of parties can be faulty, a bound established by Dwork, Lynch, and Stockmeyer in 1988. The authors prove that protocols using signature tokens can bypass this lower bound, designing a protocol that remains secure against up to a fraction of faults equal to (2 to the (k+1) minus 1) over (2 to the (k+2) minus 1) when each party holds k tokens. With k equal to the logarithm of the number of parties, the protocol solves Byzantine agreement in partial synchrony assuming only an honest majority, and the authors prove this logarithmic number of tokens is also necessary to achieve such a result. For the single-token case, they further prove that the fault-tolerance threshold of 3/7 achieved by their protocol is the best possible.
