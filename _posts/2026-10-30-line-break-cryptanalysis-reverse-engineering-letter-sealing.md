---
title: "LINE-Break: Cryptanalysis and Reverse Engineering of Letter Sealing"
date: 2026-10-30 08:27:00 +0200
categories: [Cryptography]
tags: [messaging-encryption, protocol-cryptanalysis, letter-sealing, reverse-engineering]
link: https://eprint.iacr.org/2026/2649
byline: "Diego F. Aranha, Adam Blatchley Hansen, and Thomas Kingo T. Mogensen (IACR ePrint 2026/2649, Oct 26 2026, ACM ASIA CCS 2026)"
description: "A security analysis of LINE's custom end-to-end encryption protocol Letter Sealing v2 shows that a TLS machine-in-the-middle attacker or malicious server can violate message integrity, authenticity, and confidentiality, with attacks verified experimentally on an iOS device."
---

This paper presents a security analysis of Letter Sealing v2, the custom end-to-end encryption protocol underlying LINE, a messaging platform used daily by millions of people across East and Southeast Asia, especially Japan, Taiwan, Thailand, and Indonesia. The authors find that Letter Sealing allows a TLS machine-in-the-middle attacker or malicious server to violate integrity, authenticity, and confidentiality of communications, with the protocol's stateless design permitting message replay, reordering, and blocking attacks that the user is never notified of. The lack of origin authentication further enables impersonation, letting a malicious user colluding with the adversary forge the authorship of messages in one-to-one or group chats, while stickers and URL previews leak plaintext that compromises confidentiality. The authors verified these findings by mounting a machine-in-the-middle attack on an iOS device and experimentally confirming the attacks against the authentic LINE application and an independent implementation, concluding that Letter Sealing does not meet the requirements expected of a modern end-to-end encrypted messaging protocol.
