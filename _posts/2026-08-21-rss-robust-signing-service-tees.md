---
title: "RSS: Robust Signing Service using Threshold Signatures and TEEs"
date: 2026-08-21 08:26:00 +0200
categories: [Hardware Security]
tags: [tee, threshold-signatures, sev-snp, tdx]
link: https://eprint.iacr.org/2026/1670
byline: "Filip Rezabek et al. (IACR ePrint 2026/1670, Aug 12 2026)"
description: "A threshold signing service runs key generation and signing inside AMD SEV-SNP and Intel TDX confidential VMs, integrating GG20 ECDSA, FROST, and threshold BLS."
---

The authors build a robust signing service that executes threshold cryptographic key generation and signing within trusted execution environments, integrating the GG20 threshold ECDSA scheme, FROST, and threshold BLS into the EnGINE framework. They evaluate deployments on both AMD SEV-SNP and Intel TDX confidential virtual machines with up to 40 protocol participants. Key generation is the dominant cost, completing in seconds at 40 participants, while signing completes in tens of milliseconds. The paper concludes that confidential-VM execution adds manageable overhead relative to protocol complexity, but it explicitly does not address full attestation provisioning, rollback protection, or Byzantine participant behavior.
