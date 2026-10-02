---
title: "Consensus in One Shot: Fast Agreement Beyond Classical Limits"
date: 2026-10-02 08:25:00 +0200
categories: [Cryptography]
tags: [one-shot-signatures, state-machine-replication, quantum-cryptography, consensus]
link: https://eprint.iacr.org/2026/2269
byline: "Omri Shmueli and Ilan Tennenhouse (IACR ePrint 2026/2269, Sep 29 2026)"
description: "Using one-shot signatures, a quantum-assisted consensus protocol beats classical good-case latency barriers while keeping all communication classical."
---

Good-case latency, how quickly honest parties reach agreement when the sender is honest, hits a hard classical barrier once a third or more of parties are corrupted: synchronous broadcast then needs latency at least the conservative delay bound plus the real one, and under partial synchrony consistency and liveness cannot both hold at that corruption level. The authors study using quantum information to get past these barriers with one-shot signatures, a primitive that stops even a corrupt signer from issuing signatures on two different messages under the same verification key, giving cryptographic non-equivocation without relying on trusted hardware. Assuming one-shot signatures and a public-key infrastructure, against quantum polynomial-time static corruptions they build, under synchrony, a client-free state-machine-replication protocol with optimal good-case latency tolerating any number of corruptions below n, and under partial synchrony a protocol with twice that latency that stays consistent under any number of corruptions and live once more than half the parties are honest. In the partial-synchrony case, a corrupt majority can only stall progress, never create conflicting histories, a guarantee the authors note is classically impossible without assumptions like trusted hardware even when liveness is required against just a single corrupt party. Both protocols use entirely classical communication, with quantum computation confined locally to each party.
