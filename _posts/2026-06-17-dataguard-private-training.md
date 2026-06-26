---
title: "DataGuard: Guaranteeing Private Training in Systolic-array Based Accelerators"
date: 2026-06-17 08:37:00 +0200
categories: [Hardware Security]
tags: [hardware-security, hardware-acceleration, privacy]
link: https://arxiv.org/abs/2606.16809
byline: "Pawan Kumar Sanjaya et al. (arXiv:2606.16809, Jun 15 2026)"
description: "A hardware mechanism in ML accelerators that guarantees only differentially private results can leave the device, without trusting the federated learning application."
---

Federated learning keeps raw sensitive data on user devices while differential
privacy clips and adds noise to gradients to bound privacy loss to a budget chosen
by the data owner, but real deployments assume a third-party federated learning
application correctly implements differential privacy and grant it full access to
sensitive data. DataGuard is a hardware-based mechanism that guarantees the only data
able to leave the device is the result of computation meeting differential privacy
requirements, removing the need to trust the third-party application. Built into
systolic-array accelerators, it enforces that the data owner's privacy budget cannot
be exceeded during federated training. The authors evaluate DataGuard in simulations
of four accelerators across various machine learning models. They report area
overheads under 0.01 percent and performance slowdowns under 0.3 percent.
