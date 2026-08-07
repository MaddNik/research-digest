---
title: "Formal Security Analysis of the Olvid Messenger"
date: 2026-08-07 08:15:00 +0200
categories: [Cryptography]
tags: [protocol-analysis, key-exchange, secure-messaging]
link: https://eprint.iacr.org/2026/1622
byline: "Noemi Terzo et al. (IACR ePrint 2026/1622, Aug 5 2026)"
description: "The first independent formal security analysis of the cryptographic core of Olvid, an end-to-end encrypted messenger used by French government officials."
---

Researchers built detailed formal models of Olvid's authenticated key exchange and continuous key agreement protocols and verified them under an active Dolev-Yao adversary that can compromise parties. The analysis confirms Olvid achieves mutual authentication, session key secrecy, forward secrecy, and replay protection. However, it also shows that, contrary to Olvid's own claims, the protocol does not satisfy stronger modern security models such as eCK that other secure messengers like Signal meet. The authors additionally report a potential timing leakage they discovered along the way and discuss the protocol's anonymity claims.
