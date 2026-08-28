---
title: "From Fleet to Lab: Revisiting the Security and Complexity of Industrial Rowhammer Mitigation"
date: 2026-08-28 08:35:00 +0200
categories: [Hardware Security]
tags: [rowhammer, memory-controller, dram-security, mitigation]
link: https://arxiv.org/abs/2608.26072
byline: "Hritvik Taneja and Moinuddin Qureshi (arXiv:2608.26072, Aug 26 2026)"
description: "FiRM redesigns memory-controller Rowhammer mitigation to remain secure through tracker-to-sampling mode transitions, addressing a vulnerability the authors find in Microsoft's deployed Sigries defense."
---

Rowhammer mitigation at the memory controller faces a tradeoff between tracking storage and mitigation rate: precise trackers like Misra-Gries avoid unnecessary mitigations but need large CAM structures, while sampling schemes like PARA need no storage but trigger frequent mitigations even without an attack. Microsoft's recently deployed Sigries defense combines an under-provisioned Misra-Gries tracker with a row-sampling fallback and claims the sampling-to-tracker transition is safe, but the authors' analysis shows this transition is also vulnerable, with a round-robin attack across sub-banks reducing Sigries' mean time to failure to about 1 second, eight orders of magnitude below the 13 years achieved by PARA. The authors propose FiRM, which co-designs the tracking and sampling modes, including their transitions, to remain secure throughout, incurring zero slowdown for benign workloads and replacing the complex CAM-based tracker with simple SRAM filters. They present two variants, probabilistic FiRM-P and deterministic FiRM-D, both of which the authors report have lower storage overhead than Sigries while avoiding both its insecurity and its complexity.
