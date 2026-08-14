---
title: "RealmEye: Virtual Machine Introspection for Arm CCA Realm VMs"
date: 2026-08-14 08:34:00 +0200
categories: [Hardware Security]
tags: [arm-cca, trusted-execution-environment, vm-introspection]
link: https://arxiv.org/abs/2608.12822
byline: "Ruofei Qu et al. (arXiv:2608.12822, Aug 13 2026)"
description: "RealmEye gives tenants out-of-VM introspection visibility into their own isolated Arm Confidential Compute Architecture Realm workloads without breaking the TEE's confidentiality guarantees."
---

Confidential virtual machines built on Arm's Confidential Compute Architecture (CCA) protect tenant workloads from a potentially malicious hypervisor, but that same isolation also blocks legitimate tenant-side introspection and security monitoring. RealmEye addresses this by placing its monitoring logic at the level of the Realm Management Monitor rather than inside the protected VM, allowing it to read memory and registers, take consistent snapshots by suspending the VM, and trap page-level access patterns without modifying the monitored Realm. A self-driven trigger mechanism keeps timing decisions internal to the Realm Management Monitor specifically to prevent a colluding hypervisor from tipping off an in-VM rootkit. Introspection results are delivered to the remote VM owner over hardware-attested channels, and compatibility layers let RealmEye plug into existing introspection tooling such as LibVMI and DRAKVUF. On an Arm Fixed Virtual Platform, the authors show RealmEye detecting process-hiding and syscall-table manipulation attacks inside the Realm, with cost scaling predictably with the number of monitored operations.
