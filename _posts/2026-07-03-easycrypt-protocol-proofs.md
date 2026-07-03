---
title: "Principles for pRHL Proofs of Cryptographic Protocols: How to Convince EasyCrypt that your Protocol is Secure"
date: 2026-07-03 08:23:00 +0200
categories: [Cryptography]
tags: [formal-verification, easycrypt, protocol-proofs]
link: https://eprint.iacr.org/2026/1334
byline: "Barbosa et al. (IACR ePrint 2026/1334, Mon 29 Jun 2026)"
description: "This paper diagnoses why formalizing interactive protocol security proofs in the EasyCrypt proof assistant is so much harder than formalizing primitive-level proofs."
---

EasyCrypt has been successfully used to formalize security proofs for many cryptographic primitives, but attempts to formalize objects with interactivity, such as protocols, have fared much worse. The authors investigate the underlying reasons by formalizing a simple interactive key agreement protocol, walking through a first complete but exploratory proof, a failed attempt at a more structured proof, and what they consider an essential proof. From this progression they identify which proof features drive the complexity of formalization in the probabilistic relational Hoare logic that underlies EasyCrypt. They argue that the core difficulty in formalizing interactive protocol security in the computational model comes from proofs needing both state invariants, to support cryptographic reasoning, and temporal invariants, to support reasoning about the protocol's structure over time. The authors suggest this observation could guide new reasoning tools bridging primitive-focused and protocol-focused formal verification.
