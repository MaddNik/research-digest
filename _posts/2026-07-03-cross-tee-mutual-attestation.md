---
title: "Know Thy Neighbor: Cross-TEE Mutual Attestation"
date: 2026-07-03 08:28:00 +0200
categories: [Hardware Security]
tags: [trusted-execution-environments, remote-attestation, formal-verification]
link: https://arxiv.org/abs/2607.00695
byline: "Andrade et al. (arXiv:2607.00695, Wed 01 Jul 2026)"
description: "A formally verified protocol called Hema lets trusted applications running on different types of TEEs mutually attest to each other efficiently."
---

The paper addresses a practical gap in trusted execution environment deployments: when two trusted-application instances need to communicate securely, they typically rely on bidirectional remote attestation, but existing approaches to this become inefficient once the two instances run on different TEE types, for example one on Intel SGX and another on a different platform. The authors introduce the Heterogeneous Mutual Attestation protocol, called Hema, which is formally verified and supports mutual attestation between trusted-application instances whether they share the same TEE type or run on different ones. They argue Hema offers efficiency and security advantages over existing cross-platform attestation approaches. The work targets a real interoperability problem as cloud deployments increasingly mix heterogeneous TEE hardware from different vendors.
