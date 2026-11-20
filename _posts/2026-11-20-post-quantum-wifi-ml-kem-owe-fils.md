---
title: "Post-Quantum Migration of Wi-Fi Key Establishment: A Hybrid ML-KEM Design for OWE and FILS, Validated on OWE with hostapd"
date: 2026-11-20 08:12:00 +0200
categories: [PQC]
tags: [ml-kem, wi-fi, hybrid-key-exchange, implementation]
link: https://arxiv.org/abs/2611.21528
byline: "Jesus R. Abascal, Ana I. Gomez, Domingo Gomez-Perez (arXiv:2611.21528, Nov 16 2026)"
description: "A hybrid ML-KEM and elliptic-curve key establishment design for Wi-Fi's OWE and FILS protocols is validated with a working hostapd and wpa_supplicant implementation."
---

The Diffie-Hellman exchanges that protect Wi-Fi associations would be broken by a sufficiently capable quantum computer, letting an adversary record a connection today and decrypt it years later, so the authors target the two IEEE 802.11 protocols that perform key agreement during link setup: Opportunistic Wireless Encryption, which encrypts otherwise open networks, and Fast Initial Link Setup, designed for fast connections in dense or mobile deployments. They propose replacing the Diffie-Hellman exchange in each with a hybrid exchange that runs the classical elliptic-curve agreement alongside ML-KEM, FIPS 203, deriving the master key from both secrets so the connection stays protected if either component remains unbroken. The hybrid exchange reuses frames each protocol already sends and adds no extra round trip, letting an access point advertise hybrid mode alongside classical OWE. The design is validated with a working implementation on hostapd and wpa_supplicant for OWE, where both endpoints derive the same key in every measured connection, the enlarged association frames for the two smaller ML-KEM parameter sets still fit in a single frame under a conservative 1500-byte fragmentation threshold, and added connection time and computation stay below half a millisecond; the design is intended to carry over to FILS.
