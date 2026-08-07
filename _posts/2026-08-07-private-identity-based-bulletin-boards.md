---
title: "Private Identity-based Bulletin Boards for Anonymous Messaging and Other Online Services"
date: 2026-08-07 08:21:00 +0200
categories: [Cryptography]
tags: [anonymous-communication, identity-based-encryption, mpc]
link: https://eprint.iacr.org/2026/1611
byline: "Karim Eldefrawy et al. (IACR ePrint 2026/1611, Aug 5 2026)"
description: "A distributed anonymous messaging system for low-connectivity, censorship-prone networks that lets users post and retrieve messages via identity-based encryption without prior key exchange."
---

The paper targets anonymous message posting and retrieval in settings with limited connectivity and active censorship risk. The construction uses identity-based encryption so senders need no prior key exchange with recipients, and it is designed so that a single non-colluding server cannot learn recipient identities or access patterns beyond disclosed parameters such as the epoch or retrieval count. Contributions include formal security definitions for this class of system, a hierarchical identity-based encryption construction with searchable properties, and an efficient multi-server design intended to reduce trust in any one server. The authors also report a working prototype demonstrating the scheme's practical viability.
