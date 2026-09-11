---
title: "\"They don't care about this\": A Systematic Study of TEE Build Reproducibility in the Wild"
date: 2026-09-11 08:27:00 +0200
categories: [Hardware Security]
tags: [trusted-execution-environments, remote-attestation, reproducible-builds, sgx]
link: https://arxiv.org/abs/2609.11411
byline: "Annika Wilde et al. (arXiv:2609.11411, Sep 10 2026)"
description: "A study of 115 real-world TEE deployments finds that 91 percent are not reproducible, undermining remote attestation's ability to link a measurement back to the deployed source code."
---

Remote attestation lets external parties verify the authenticity and integrity of code running inside a trusted execution environment (TEE) through cryptographic measurements, but this depends on the verifier being able to trace a measurement back to the original source code, which requires reproducible builds. The authors analyze the reproducibility of 115 TEE deployments spanning Intel SGX, Intel TDX, and AMD SEV, finding that 91 percent were not reproducible and 80 percent failed to provide both source code and a reference build, the two prerequisites for reproducibility. To understand the causes, they contacted maintainers of 50 SGX projects and interviewed 12 developers from industry and academia, finding that only one participant treated reproducibility as a development priority, confirming the technical findings. Beyond readily fixable technical barriers such as embedded timestamps, the authors identify broader ecosystem challenges such as lack of control over the build environment in multi-stakeholder projects, and argue that achieving TEE reproducibility requires a holistic development approach rather than treating TEEs as a simple security badge.
