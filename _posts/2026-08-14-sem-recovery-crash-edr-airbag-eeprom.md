---
title: "World-First SEM-based Recovery of Crash EDR Data from the EEPROM of a Severely Damaged SRS Module Using CrashScan"
date: 2026-08-14 08:32:00 +0200
categories: [Hardware Security]
tags: [chip-forensics, sem-imaging, data-remanence]
link: https://arxiv.org/abs/2608.10152
byline: "Sergei Skorobogatov and Peter Vertal (arXiv:2608.10152, Aug 10 2026)"
description: "Physical, semi-invasive forensic analysis recovered intact EEPROM data from an automotive airbag module whose processor and flash memory were destroyed by fire and electrical damage in a severe crash."
---

This is a hardware forensics and invasive-analysis paper rather than an attack or defense paper. The authors describe recovering a complete event-data-recorder report from an automotive Supplemental Restraint System, or airbag, module after a severe accident in which the processor and flash memory suffered visible electrical damage and package perforation. Their investigation found that overvoltage and high current had driven local temperatures above 3000 degrees Celsius, melting internal wires and partially evaporating the silicon substrate, yet the on-chip EEPROM array only micrometers away retained its data intact. Using specialized sample preparation, scanning electron microscope imaging, and their CrashScan forensic extraction software, the team achieved full data recovery. The authors present this as the first practical, affordable method for recovering data from memory chips damaged mechanically, electrically, or by fire, with potential applications beyond automotive forensics including medical, aviation, and aerospace incident investigation. Because it shows that supposedly destroyed secure memory can still be read out via physical means, it is directly relevant to the tamper-resistance and data-remanence side of secure hardware design.
