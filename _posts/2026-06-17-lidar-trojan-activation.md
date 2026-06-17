---
title: "Anywhere, Any-Stymie: Remote Activation of Trojan Malware on LiDAR with Modulated Signals"
date: 2026-06-17 08:34:00 +0200
categories: [Hardware Security]
tags: [supply-chain, hardware-trojan, sensor-security, autonomous-systems]
link: https://arxiv.org/abs/2606.17562
byline: "R. Spencer Hallyburton et al. (arXiv:2606.17562, Jun 16 2026)"
description: "Dormant firmware malware embedded in a LiDAR pipeline is remotely triggered by a modulated optical signal to manipulate point clouds."
---

The authors identify an attack surface in which dormant malware embedded in the
LiDAR sensing pipeline stays inactive during normal operation and can be triggered
externally after deployment, without needing access to sensor hardware or networking
at attack time. They build malware capable of low-level point-cloud manipulation and
embed it into LiDAR firmware, developed in a closed research test environment with
vendor support rather than by exploiting a production supply-chain flaw. An optical
trigger delivers a modulated signal into the sensing environment to selectively
activate the malware, which then performs real-time false object injection and real
object suppression. Evaluation establishes feasibility at 300 feet static and during
recorded drive-by runs reaching 35 miles per hour, with injected person-like
artifacts remaining semantically detectable by a state-of-the-art 3D object
detector. The work demonstrates safety-critical impact on a deployed tactical
autonomous vehicle and argues for stronger integrity guarantees across the LiDAR
development and deployment pipeline.
