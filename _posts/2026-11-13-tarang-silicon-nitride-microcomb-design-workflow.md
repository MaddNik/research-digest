---
title: "TARANG: an open-source, cost-controlled design workflow for silicon nitride microcomb chips"
date: 2026-11-13 08:05:00 +0200
categories: [Photonics]
tags: [silicon-nitride, microcomb, integrated-photonics, design-automation]
link: https://arxiv.org/abs/2611.16469
byline: "Divyanshu Tiwari, Esraaj Sarkar Gupta, Anshuman Kumar (arXiv:2611.16469, Nov 12 2026)"
description: "TARANG is an open-source Python package that takes a silicon nitride microcomb platform from tabulated refractive indices to a fabrication-ready mask in fourteen priced simulation stages."
---

Designing a microresonator frequency comb chip means solving a chain of coupled problems: a waveguide with anomalous dispersion that survives fabrication errors, a ring with the right free spectral range and quality factor, a bus gap that sets the coupling regime, and grating couplers, all made in one lithography step. The authors present TARANG, an open-source Python package that carries a silicon nitride platform from tabulated refractive indices to a GDSII mask in fourteen stages, built on cloud mode, FDTD, and eigenmode-expansion solvers, where every simulation is priced before it runs and capped, and every result is cached and numerically checked. They show that a common way of steadying dispersion calculations, snapping the simulation grid onto the waveguide core's faces, leaves field samples vulnerable to floating-point rounding, and that averaging solves with the grid just inside and just outside the faces makes the group-velocity dispersion independent of the computer and stable to about 1 picosecond per nanometer per kilometer across meshes. Two complete air-clad designs are presented, at 1550 nanometers with a 700 by 1000 nanometer core and at 780 nanometers with a 350 by 500 nanometer core, each with a 200 gigahertz ring, critical and over-coupled gaps, grating couplers, and a fiber-to-fiber budget. The predicted dispersion agrees with two measured devices from the literature to within 1 and 4 percent, and an independent Lugiato-Lefever solver forms stable single solitons from the exported parameters of both designs, which the authors say are ready for fabrication.
