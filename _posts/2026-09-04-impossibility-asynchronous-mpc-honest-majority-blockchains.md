---
title: "(Im)possibility of Asynchronous MPC with Honest Majority over Blockchains"
date: 2026-09-04 08:20:00 +0200
categories: [Cryptography]
tags: [multiparty-computation, asynchronous-protocols, blockchain, secret-sharing]
link: https://eprint.iacr.org/2026/1860
byline: "Ashish Choudhury et al. (IACR ePrint 2026/1860, Sep 2 2026)"
description: "A blockchain-hybrid model study shows the classical n greater than 3t resilience bound for asynchronous MPC is inherent without public-key trusted setup, but constructs an asynchronous MPC protocol tolerating Byzantine faults for n greater than 2t once public-key trusted setup is assumed."
---

This work studies asynchronous verifiable secret sharing (AVSS) and asynchronous multiparty computation (AMPC) in a blockchain-hybrid model where parties have black-box access to an ideal asynchronous blockchain functionality that only provides persistence and eventual liveness, motivated by the deployment of MPC in blockchain applications such as privacy-preserving payments and threshold wallets. The authors ask whether blockchain access can improve on the classical resilience bound of n greater than 3t, where n is the total number of parties and t is the number compromised by an adversary, giving a comprehensive set of lower and upper bounds across three settings: no trusted setup, trusted setup with Minicrypt assumptions, and trusted setup with public-key assumptions. They show that without a trusted setup, or with a setup restricted to Minicrypt assumptions, the classical n greater than 3t resilience bound for AMPC is inherent, even against weaker fail-stop or omission adversaries, while AVSS is achievable for n greater than 2t in both settings, establishing a separation between AVSS and AMPC in the regime 2t less than n at most 3t. In contrast, under public-key assumptions with trusted setup, the authors construct an AMPC protocol tolerating Byzantine adversaries whenever n is greater than 2t, using threshold homomorphic encryption, threshold signatures, commitments, and zero-knowledge proofs to keep on-chain communication independent of circuit size. This is a minor revision of a paper accepted at TCC 2026.
