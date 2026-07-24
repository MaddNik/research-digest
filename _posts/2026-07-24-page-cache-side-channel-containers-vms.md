---
title: "Isolation Failure From Shared Storage: Characterizing and Exploiting Page-Cache SCA Leakage Across Containers and VMs"
date: 2026-07-24 08:26:00 +0200
categories: [Hardware Security]
tags: [page-cache, microarchitectural-timing, cloud-isolation, cross-vm-leakage]
link: https://arxiv.org/abs/2607.17518
byline: "Alon Abudraham et al. (arXiv:2607.17518, Jul 21 2026)"
description: "The paper demonstrates that the host page cache, a shared hardware-adjacent resource, leaks unprivileged timing information across supposedly isolated containers and virtual machines."
---

The authors examine cloud isolation mechanisms and show that unprivileged timing measurements can reveal page-cache residency across container and VM boundaries, including in Docker, gVisor, and Kata Containers. The leakage persists through OverlayFS, virtio-fs, and loop-backed storage, but diminishes significantly with direct I/O and dedicated block devices. They present a practical demonstration recovering activity data from a WordPress-MySQL deployment. The work classifies this as an OS-mediated microarchitectural timing channel and recommends coordinated defenses spanning hardware, virtualization, and operating systems.
