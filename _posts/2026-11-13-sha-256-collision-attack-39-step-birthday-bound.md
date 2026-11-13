---
title: "Collision Attacks on SHA-2: 39-Step SHA-256 below the Birthday Bound"
date: 2026-11-13 08:23:00 +0200
categories: [Cryptography]
tags: [sha-256, sha-512, hash-cryptanalysis, collision-attack]
link: https://eprint.iacr.org/2026/2867
byline: "Jiaying Gong et al. (IACR ePrint 2026/2867, Nov 11 2026)"
description: "A new message-word pinning technique extends practical collision attacks on reduced-round SHA-256 to 39 steps at an estimated cost below the 2 to the power of 128 birthday bound."
---

SHA-2 is the most widely deployed family of hash functions, and its security margin is measured by how many internal steps collision attacks can reach; the best prior classical attack reached 38-step SHA-256 at an estimated cost of 2 to the power of 104.3. The authors extend this to 39 steps while keeping an advantage over generic collision search, keeping the previously published 39-step differential characteristic but changing how its conditions are satisfied through a technique they call joint message-word pinning, which fixes two expanded message words to the values the characteristic prescribes. For each chaining value, they solve for assignments to two state words that carry no direct condition, where every returned assignment automatically gives both message words their prescribed values, by first fixing the value of a function with a small image and then solving the coupled equations for the two words in sequence. On 39-step SHA-256, pinning one word alone gives an estimated cost of 2 to the power of 123.4 scalar compressions per expected collision, and pinning both words reduces this by 14.6 bits to 2 to the power of 108.8, giving an upper bound of about 2 to the power of 124.6 on the expected cost of finding the first collision even under worst-case clustering, which is below the 2 to the power of 128 birthday bound. For 38-step SHA-256 the same ideas reduce the estimated cost per collision from 2 to the power of 104.3 to 2 to the power of 90.9, and on SHA-512 pinning one word reduces the cost from 2 to the power of 125.4 to 2 to the power of 100.7 for 38 steps and from 2 to the power of 178 to 2 to the power of 131.3 for 39 steps.
