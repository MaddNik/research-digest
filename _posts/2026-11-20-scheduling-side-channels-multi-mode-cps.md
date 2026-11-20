---
title: "Inferring Sensitive Events in Multi-Mode Cyber-Physical Systems via Scheduling Side Channels"
date: 2026-11-20 08:28:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, scheduling, cyber-physical-systems, timing-attacks]
link: https://arxiv.org/abs/2611.17761
byline: "Yifan Cai, Linh Thi Xuan Phan (arXiv:2611.17761, Nov 13 2026)"
description: "STAMP is a lightweight attack that infers sensitive physical events, such as a homeowner's arrival, from the scheduling-induced timing side channel created when a cyber-physical system switches operating modes."
---

Many cyber-physical systems operate in multiple modes, switching between different tasksets and timing parameters in response to physical events or user activity. The authors show that these mode changes create a timing side channel, because they alter the interference experienced by co-running tasks, letting an unprivileged co-resident observer infer sensitive events such as a homeowner's arrival or a vehicle's route from its own execution timing and, on multicore platforms, its core assignment. Existing schedule-based attacks and defenses miss this channel because they assume single-mode systems or target a specific known victim task. The authors present STAMP, a lightweight attack that needs no knowledge of task parameters or scheduling policy and works whether or not the system exposes its modes. On a ZoneMinder home-security deployment, STAMP identifies the operating modes with 94.7 percent accuracy on unseen hardware using under 0.5 percent of one core, and on ROS 2 AMCL with the Oxford RobotCar dataset it identifies which of seven route segments a vehicle traversed with 86.0 percent accuracy on unseen platforms. A schedule-randomization defense lowers detection recall to 0.53 but only lets 53.9 percent of jobs finish on time, and at higher noise levels on-time completion falls to 14.4 percent while introducing new leakage in 14.1 percent of the tested tasksets.
