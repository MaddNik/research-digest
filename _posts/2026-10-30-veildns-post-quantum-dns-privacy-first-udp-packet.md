---
title: "VeilDNS: Post-Quantum DNS Privacy from the First UDP Packet"
date: 2026-10-30 08:16:00 +0200
categories: [PQC]
tags: [post-quantum-kem, dns-privacy, udp-protocol, forward-secrecy]
link: https://eprint.iacr.org/2026/2629
byline: "Aditya Singh Rawat, Mahabir Prasad Jhanwar, and Rei Safavi-Naini (IACR ePrint 2026/2629, Oct 24 2026)"
description: "VeilDNS uses a post-quantum KEM and AEAD to encrypt DNS queries and answers within a single UDP exchange, achieving up to 3.5 times higher cold-session throughput than ML-DSA-authenticated DNS-over-TLS, DNS-over-HTTPS, or DNS-over-QUIC."
---

DNS was designed around single-exchange UDP traffic, which exposes client queries in cleartext, while existing encrypted alternatives such as DoT, DoH, and DoQ require a TLS or QUIC handshake before private queries can be sent, a cost that grows as those handshakes adopt post-quantum authentication. This paper introduces VeilDNS, a DNS-native protocol that uses a post-quantum key encapsulation mechanism and authenticated encryption with associated data to encrypt DNS questions and answers and authenticate the resolver within a single UDP exchange, giving clients query privacy from their very first packet given an authenticated resolver KEM key. VeilDNS supports both stateless and stateful modes, with the stateful mode reducing recurring computation and bandwidth, and an optional mode provides forward secrecy from the second query onward, all while preserving the standard DNS wire format so it still runs on UDP port 53. Compared with ML-DSA-authenticated Do(T/H/Q) on a well-provisioned network profile, VeilDNS's stateless and stateful modes achieve up to 3.5 times higher cold-session throughput, 4.8 times lower average latency, 4.7 times lower CPU time, 13.7 times fewer bytes, and 15.8 times fewer packets, with a 12.4 times throughput gain on a constrained network profile, and the authors use the Tamarin prover to establish query confidentiality, response authentication, and forward secrecy.
