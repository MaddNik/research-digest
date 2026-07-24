---
title: "Doubly-Efficient Secret-Key PIR with Low Storage Overhead"
date: 2026-07-24 08:20:00 +0200
categories: [Cryptography]
tags: [private-information-retrieval, locally-decodable-codes, storage-overhead, doubly-efficient-pir]
link: https://eprint.iacr.org/2026/1480
byline: "Caicai Chen et al. (IACR ePrint 2026/1480, Jul 20 2026)"
description: "A private information retrieval scheme that lets a client fetch a database record without revealing which one, using close to 1 times storage overhead and sublinear server computation."
---

The paper addresses secret-key private information retrieval, where a client hides its query from the server holding the database. It presents constructions achieving constant multiplicative storage overhead approaching a factor of 1, while also keeping server computation sublinear in the database size. The construction relies on new families of what the authors call t-smooth locally decodable codes, together with new decoding methods for Reed-Muller codes. In a practical benchmark, encoding a 37 gigabyte database required only 4.2 times storage expansion, and each query required the server to access less than 600 kilobytes of the encoded database.
