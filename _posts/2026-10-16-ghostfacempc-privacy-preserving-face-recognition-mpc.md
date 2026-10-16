---
title: "GhostFaceMPC: Privacy-Preserving Face Recognition with Multi-Party Computation"
date: 2026-10-16 08:26:00 +0200
categories: [Cryptography]
tags: [secure-multiparty-computation, face-recognition, biometrics, neural-network-quantization]
link: https://eprint.iacr.org/2026/2499
byline: "Davide Carnemolla et al. (IACR ePrint 2026/2499, Oct 15 2026)"
description: "GhostFaceMPC is the first end-to-end face recognition system that evaluates a deep convolutional feature extractor and the subsequent matching entirely under secure multi-party computation."
---

Facial recognition has become central to modern authentication, security, and personalization systems, but its adoption is hindered by privacy risks around unauthorized access to sensitive biometric data. GhostFaceMPC addresses this by presenting the first end-to-end, privacy-preserving face recognition system that evaluates a deep convolutional neural network feature extractor and the matching step under secure multi-party computation, protecting facial data at every stage from feature extraction and storage through matching without ever exposing raw images or biometric embeddings. The authors introduce a multi-party-computation-friendly quantization of the GhostFaceNet model together with circuit optimizations that make face recognition under secure multi-party computation practical rather than purely theoretical. The implementation and code are released publicly, giving a concrete reference point for building privacy-preserving biometric authentication systems.
