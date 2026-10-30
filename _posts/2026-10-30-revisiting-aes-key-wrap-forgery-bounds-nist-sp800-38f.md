---
title: "Revisiting AES Key Wrap: Forgery Bounds, Structural Observations, and Recommendations for the Revision of NIST SP 800-38F"
date: 2026-10-30 08:31:00 +0200
categories: [Cryptography]
tags: [aes-key-wrap, nist-sp-800-38f, authenticated-encryption, forgery-attacks]
link: https://eprint.iacr.org/2026/2636
byline: "John Preuss Mattsson (IACR ePrint 2026/2636, Oct 25 2026)"
description: "A revisit of the AES Key Wrap modes KW, KWP, and TKW shows that NIST SP 800-38F's stated forgery probabilities ignore adaptive attacks and that KW does not achieve beyond-birthday-bound security, informing NIST's ongoing revision of the standard."
---

As NIST revises SP 800-38F, which specifies the AES Key Wrap modes KW and KWP, this paper presents an updated and expanded version of the author's technical comments submitted to that process. The author shows that the forgery probabilities stated in SP 800-38F do not account for adaptive attacks, derives corrected forgery probabilities for KW, KWP, and TKW, and shows that checking the expected plaintext length can considerably raise KWP's security level. Revisiting Kelsey's long-message observation, the paper corrects the stated collision conditions, shows that a successful forgery leaks a plaintext prefix, derives an encryption-only distinguisher, and concludes that KW does not achieve beyond-birthday-bound security. The author also explains the role of the step counter, analyzes the single-semiblock path of KWP and the tradeoff between the number of passes and the length limit, and offers concrete recommendations for the NIST revision, for implementers, and for future key-wrap designs.
