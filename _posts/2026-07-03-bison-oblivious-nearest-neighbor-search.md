---
title: "BiSON: Billion-Scale Oblivious Nearest-Neighbor Search in Milliseconds"
date: 2026-07-03 08:18:00 +0200
categories: [Cryptography]
tags: [oblivious-ram, secure-search, nearest-neighbor, mpc]
link: https://eprint.iacr.org/2026/1343
byline: "Das et al. (IACR ePrint 2026/1343, Tue 30 Jun 2026)"
description: "A new oblivious RAM based protocol lets billion-scale encrypted vector databases answer nearest-neighbor search queries in milliseconds while hiding both data and queries."
---

BiSON targets secure semantic search over vector databases, a setting where both the stored data and the incoming queries must stay hidden while still supporting fast approximate nearest-neighbor retrieval. The authors introduce a new disk-compatible oblivious RAM architecture that lets the protocol scale to billion-point datasets without sacrificing latency or privacy. Compared with the prior state of the art, BiSON reduces communication by up to 28 times, improves end-to-end latency by up to 23.5 times, and scales to databases two orders of magnitude larger. The authors report that BiSON's search accuracy remains comparable to state-of-the-art insecure approximate nearest-neighbor algorithms even at billion-point scale. This is positioned as the first practical, scalable solution for secure semantic search at cloud scale.
