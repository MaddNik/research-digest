---
title: "RotPIR: Sublinear Single-Server PIR with Efficient Pre-Processing via Oblivious Homomorphic Rotation"
date: 2026-07-03 08:15:00 +0200
categories: [FHE]
tags: [private-information-retrieval, homomorphic-rotation, preprocessing]
link: https://eprint.iacr.org/2026/1336
byline: "Zhang et al. (IACR ePrint 2026/1336, Mon 29 Jun 2026)"
description: "RotPIR co-designs a client-preprocessing private information retrieval protocol with a new oblivious homomorphic rotation operator to make FHE-based preprocessing efficient."
---

The paper addresses client-preprocessing private information retrieval (PIR), which pushes the linear server work of single-server PIR into an offline phase so that online queries need only sublinear computation and communication. Prior approaches either stream the entire database during preprocessing, incurring linear communication, or use fully homomorphic encryption for preprocessing at prohibitive homomorphic-computation cost, as in the prior state of the art. RotPIR introduces a preprocessing framework built around a new homomorphic operator, oblivious homomorphic rotation, which rotates the database according to an encrypted offset and substantially accelerates offline server-side computation while avoiding full database streaming. The scheme keeps both online communication and computation sublinear. The authors report experimental results showing up to a 1000 times speedup in offline server-side computation relative to state-of-the-art client-preprocessing PIR protocols that avoid streaming the whole database.
