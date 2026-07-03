---
title: "The Most Efficient Protocol for PAKE: What Exact Stuff Do You Need to Hash at the End?"
date: 2026-07-03 08:21:00 +0200
categories: [Cryptography]
tags: [pake, key-exchange, universal-composability, protocol-design]
link: https://eprint.iacr.org/2026/1331
byline: "Xu (IACR ePrint 2026/1331, Mon 29 Jun 2026)"
description: "This paper resolves ambiguity in the OEKE-2F password-authenticated key exchange compiler by proving universal composability for all 16 possible variants of its final hashing step."
---

Password-authenticated key exchange lets two parties establish a session key from only a shared low-entropy password, and the OEKE-2F compiler, which turns a key encapsulation mechanism into a PAKE, is notable both for being the most computationally efficient universally composable PAKE known when instantiated with Diffie-Hellman, and for offering a generic route to post-quantum PAKE. The paper observes that the community has not agreed on exactly what gets hashed in the protocol's final message, since up to four different values, the password, the KEM public key, the first protocol message, and the KEM ciphertext, can optionally be included alongside the KEM key, giving 16 possible variants, only two of which had previously been studied. The author proves universal composability security for all 16 variants and finds that the hash-everything version requires the fewest security properties from the underlying KEM, with security requirements increasing as items are removed from the hash.
