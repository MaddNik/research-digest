---
title: "LFSRs and Boolean Masking: An In-depth Security Analysis"
date: 2026-08-07 08:30:00 +0200
categories: [Hardware Security]
tags: [masking, side-channel, formal-verification]
link: https://eprint.iacr.org/2026/1614
byline: "Anna Guinet et al. (IACR ePrint 2026/1614, Aug 5 2026)"
description: "The paper presents the first formal verification framework that jointly analyzes a pseudorandom number generator, such as a linear feedback shift register, together with a masking countermeasure in the probing model."
---

Masking is a common countermeasure against side-channel attacks, and its formal security proofs are usually developed assuming an idealized source of uniform, independent randomness, without considering the actual random or pseudorandom generator used. This work introduces a verification framework that analyzes a pseudorandom number generator, in particular a linear feedback shift register, jointly with a masking scheme within the d-probing model. The method is based on the Walsh-Hadamard transform, adapting techniques from linear cryptanalysis into what the authors call the robust probing model. They demonstrate the approach on 4-bit and 8-bit S-boxes and corroborate the formal analysis with practical evaluation on an FPGA. The work indicates that the choice of randomness source can affect the real-world security of masking schemes beyond what standard idealized proofs capture.
