---
title: "Flip a Failure into a Success: Improved Bit Flipping Decoding for QC-MDPC Codes"
date: 2026-08-07 08:02:00 +0200
categories: [PQC]
tags: [code-based, bike, decoding]
link: https://eprint.iacr.org/2026/1616
byline: "Paolo Santini et al. (IACR ePrint 2026/1616, Aug 5 2026)"
description: "A modified bit-flipping decoder for Quasi-Cyclic Moderate-Density Parity-Check codes exploits near-codeword information to reduce decoding failure rates in the BIKE key encapsulation scheme."
---

The paper targets the decoding step of Quasi-Cyclic Moderate-Density Parity-Check (QC-MDPC) codes, which underlie the BIKE post-quantum key encapsulation mechanism submitted to the NIST competition. The authors propose a modified Bit Flipping decoder, called BF-Max, that exploits knowledge about near-codewords by recognizing characteristic syndrome patterns during the decoding process. This allows the decoder to correct more errors than standard bit-flipping approaches while keeping computational cost comparable. According to the abstract, the proposed variant significantly outperforms the two decoders currently used by BIKE within the NIST competition, evaluated at security category 1 parameters. The work is directly relevant to the practical reliability and decoding failure rate analysis of code-based key encapsulation mechanisms under standardization consideration.
