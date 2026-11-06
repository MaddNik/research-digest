---
title: "Can Fully Homomorphic Encryption on Public Blockchains Protect Sensitive Medical Consultations? A Security and Privacy Assessment"
date: 2026-11-06 08:19:00 +0200
categories: [FHE]
tags: [fhevm, blockchain-privacy, metadata-leakage, access-control]
link: https://eprint.iacr.org/2026/2771
byline: "Nizamuddeen Shahruddeen (IACR ePrint 2026/2771, Nov 4 2026)"
description: "A security assessment of a Zama fhEVM medical-consultation prototype finds that fully homomorphic encryption protects message content but leaks metadata about who consulted whom and when."
---

Fully homomorphic encryption now lets smart contracts on public blockchains hold encrypted data whose decryption is governed by contract logic, raising the question of whether this can protect sensitive medical consultations where patients fear exposure. This paper assesses ConfidentialCare, a prototype built on Zama's fhEVM and the Ethereum Sepolia testnet, in which patient symptoms are encrypted in the browser and only an authorized doctor can decrypt them. Across three versions of the system, evaluated through metadata inspection, access-control testing, and attack experiments, consultation content remained confidential in every tested case and the design collected no names, emails, or accounts. However, public on-chain metadata revealed which wallet consulted which doctor, the doctor's specialty, the timing, and the approximate message length, information that would be permanently exposed if a wallet were ever linked to a real patient. The authors also found that a doctor granted access could re-share a patient's encrypted data through both a confused-deputy flaw in the application contract and directly through fhEVM's access control list, and that a time-limited, revocable delegation redesign fixed the re-sharing issue, with Zama's live key-management service enforcing revocation within the same block in all six trials.
