---
title: "Not Discrete Enough: On the Inherent Insecurity of dTPMs for Measured Boot"
date: 2026-08-21 08:27:00 +0200
categories: [Hardware Security]
tags: [tpm, measured-boot, physical-attack, attestation]
link: https://arxiv.org/abs/2608.14736
byline: "Christian Werling et al. (arXiv:2608.14736, Aug 13 2026)"
description: "A practical attack shows that brief physical access to a discrete TPM lets an attacker reset and replay PCR measurements, undermining measured-boot-sealed secrets such as disk encryption keys."
---

The authors challenge the assumption that discrete TPMs are inherently more secure than firmware- or SoC-integrated TPMs for measured boot. They show that an attacker with brief physical access to a TPM 2.0 chip, combined with the ability to boot an attacker-controlled system, can reset and replay platform measurements, defeating the sealing of secrets like disk-encryption keys behind measured boot state. They argue that firmware TPMs and SoC-integrated TPMs actually present a smaller practical attack surface than discrete external modules, since the latter's communication bus is externally accessible. The paper concludes that measured boot alone, whatever the TPM form factor, is insufficient and should be paired with user-supplied credentials rather than relied on as a standalone hardware root of trust.
