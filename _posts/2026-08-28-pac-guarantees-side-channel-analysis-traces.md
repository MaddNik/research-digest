---
title: "How Many Traces Suffice? PAC Guarantees for Profiled and Non-profiled Side-Channel Analysis"
date: 2026-08-28 08:32:00 +0200
categories: [Hardware Security]
tags: [side-channel-analysis, pac-learning, trace-complexity, ascad]
link: https://eprint.iacr.org/2026/1770
byline: "Seyedmohammad Nouraniboosjin and Fatemeh Ganji (IACR ePrint 2026/1770, Aug 21 2026)"
description: "A Probably Approximately Correct framework gives finite-sample confidence guarantees on how many traces suffice for profiled and non-profiled side-channel key recovery, rather than relying purely on empirical trace counts."
---

Side-channel analysis is typically evaluated empirically by reporting how many traces are needed to reduce the rank of the correct key, without explaining how many traces suffice for reliable recovery or distinguishing an insufficient-data failure from an inherently weak attack. The authors address this by formulating profiled and non-profiled side-channel analysis as a Probably Approximately Correct learning problem, treating candidate-key scores as the common cryptanalytic object and separating finite-sample estimation error from the intrinsic separation between the correct key and competing hypotheses. This separation enables confidence guarantees for key rank. Instantiating the framework with representative profiled and non-profiled attacks chosen for analytical tractability, experiments on ASCAD-f and ASCAD-r show the profiled attack achieves exact recovery with tens of attack traces, while the non-profiled single-attack rank certificate guarantees exact recovery with about 1,000 traces, results the authors report as competitive with, and in the non-profiled case substantially below, trace counts identified in prior studies, while additionally providing finite-sample rank guarantees.
