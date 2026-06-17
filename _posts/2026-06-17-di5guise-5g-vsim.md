---
title: "Di5Guise: 5G Privacy with vSIM"
date: 2026-06-17 08:36:00 +0200
categories: [Hardware Security]
tags: [secure-hardware, fpga, attestation, 5g-privacy]
link: https://arxiv.org/abs/2606.16943
byline: "Shirin Ebadi et al. (arXiv:2606.16943, Jun 15 2026)"
description: "A virtualized SIM on secure hardware that decouples device identity from subscriber identity to break operator-level user correlation."
---

SIM cards anchor authentication and security in cellular networks but can themselves
cause privacy loss, because current eSIMs carry a fixed device profile (a secret
key, a certificate, and a unique eUICC identifier) that permanently binds every
provisioned subscriber profile to that one device. An attacker with a cellular
operator vantage point can therefore correlate subscriber identities back to a
single device and assemble a pattern of life even when users rotate identities or
obfuscate traffic. Di5Guise breaks this correlation by decoupling device identity
from subscriber identity using vSIM, a virtualized SIM that supports dynamic device
profile provisioning so each subscriber profile maps to a distinct, unlinkable
device profile. It establishes trust with the operator by ensuring vSIM runs on
secure hardware in a trustworthy state. The authors prototype Di5Guise on an FPGA
board and integrate it with srsRAN for full compatibility with existing 5G
infrastructure. Using a user correlation model, they show re-identification accuracy
drops from 93 percent to 49 percent when combined with obfuscation.
