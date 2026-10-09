---
title: "PRA-TLS: Attestation of a Client Application for TEE"
date: 2026-10-09 08:39:00 +0200
categories: [Hardware Security]
tags: [trusted-execution-environment, remote-attestation, intel-sgx]
link: https://arxiv.org/abs/2610.06061
byline: "Reina Sasaki et al. (arXiv:2610.06061, Oct 5 2026)"
description: "PRA-TLS extends remote attestation beyond the enclave itself to the untrusted client application that invokes it, using a trusted attester daemon verified with the Tamarin Prover."
---

Trusted execution environments protect sensitive computation inside an enclave, but that enclave is invoked by an untrusted application running in the rich execution environment, and even after the enclave itself has been attested, the boundary between enclave and application remains risky, since input arguments, return values, or the order of function calls can be tampered with. The authors propose Portable Remote Attestation TLS (PRA-TLS), an attestation protocol for the client application that invokes an enclave, introducing a trusted Attester Daemon that measures the state of the host environment and application code at runtime and provides these measurements as attestation evidence for a remote verifier. This mechanism allows the enclave to proceed only when the software environment is in the expected state and the application code is verified as legitimate. The authors define attack models and security requirements for the protocol, formally evaluate its security using the Tamarin Prover, and implement and evaluate the performance of a PRA-TLS prototype using Intel SGX.
