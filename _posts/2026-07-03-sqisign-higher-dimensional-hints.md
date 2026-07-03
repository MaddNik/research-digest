---
title: "Elliptic Extraction and Pushable Hints for Higher-Dimensional SQIsign"
date: 2026-07-03 08:09:00 +0200
categories: [PQC]
tags: [sqisign, isogeny-signatures, provable-security, fiat-shamir]
link: https://eprint.iacr.org/2026/1337
byline: "Bkakria (IACR ePrint 2026/1337, Mon 29 Jun 2026)"
description: "A proof-theoretic analysis separates which security assumptions in higher-dimensional SQIsign variants are genuinely new hardness assumptions versus simulation artifacts."
---

Higher-dimensional SQIsign variants use product and Kani-style isogeny representations to make response isogenies compact, checkable, or compatible with non-smooth degrees, which raises the question of whether these representations introduce genuinely new higher-dimensional hardness or merely relocate additional assumptions into the simulation. This paper gives a proof-theoretic separation between the two layers, identifying a recoverability condition under which an accepted higher-dimensional response publicly induces an elliptic Hom element, from which special soundness extracts an elliptic OneEnd witness under the usual challenge-separation hypotheses. The remaining higher-dimensional assumptions are then formulated as non-interactive hint distributions. This yields two concrete results: an exact Fiat-Shamir-with-hints EUF-CMA theorem for SQIsign2D-West, with security loss expressed through named simulation and hint assumptions, and for SQIPrime2D, an explicit acknowledgment that the published auxiliary sampler is not proven, replaced by a defined UAux variant with an explicit additive sampling loss when only an approximate sampler is available.
