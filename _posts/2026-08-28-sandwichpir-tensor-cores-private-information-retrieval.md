---
title: "From Lattices to Tensor Cores: Accelerating Private Information Retrieval"
date: 2026-08-28 08:25:00 +0200
categories: [Cryptography]
tags: [private-information-retrieval, gpu-tensor-cores, single-server-pir]
link: https://eprint.iacr.org/2026/1816
byline: "Sidaarth Sabhnani and David J. Wu (IACR ePrint 2026/1816, Aug 27 2026)"
description: "SandwichPIR implements single-server private information retrieval almost entirely as dense 8-bit integer matrix multiplications on GPU tensor cores, answering queries with no offline communication."
---

The authors introduce SandwichPIR, the first single-server PIR protocol that implements the overwhelming majority of server computation as dense 8-bit integer matrix multiplications on GPU tensor cores while requiring no offline communication. For a 4 gigabyte database with 32 kilobyte records, SandwichPIR answers a query in 8.2 milliseconds while communicating 688 kilobytes, a server throughput of 488 gigabytes per second that is 88 times faster than the best CPU-based protocol without offline communication. Batching queries from many independent clients moves the server into a compute-bound regime, and a single Nvidia L40S GPU can process a batch of 128 queries to the same database in 21.0 milliseconds, an amortized 0.16 milliseconds per query and roughly 24 terabytes per second of effective throughput, with a fleet of 8 GPUs reaching nearly 270 terabytes per second on a 256 gigabyte database. The authors demonstrate the system by enabling private access to text-only English Wikipedia, retrieving an article of up to 128 kilobytes with 768 kilobytes of communication and under 200 milliseconds of estimated end-to-end latency, with a single GPU handling over 2,500 queries per second at an estimated cost of 0.20 dollars per million queries.
