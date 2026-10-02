---
title: "Silicon nitride nanophotonics for low-redundancy 3D convolution"
date: 2026-10-02 08:04:00 +0200
categories: [Photonics]
tags: [silicon-nitride, optical-computing, wavelength-multiplexing, chirped-bragg-grating]
link: https://arxiv.org/abs/2609.37246
byline: "Shuai Hu et al. (arXiv:2609.37246, Sep 29 2026)"
description: "A silicon nitride photonic accelerator removes redundant data movement in 3D convolution by mapping kernel coordinates onto wavelength and group delay."
---

Three-dimensional convolution is useful for extracting correlations in high-dimensional data, but overlapping receptive fields normally force a lot of redundant data movement. The authors demonstrate a silicon nitride 3D optical convolution accelerator that reconstructs receptive fields through coordinate-aware mapping from wavelength to group delay: a deterministically serialized input tensor is broadcast onto multiple wavelength channels, and an integrated chirped waveguide Bragg grating compensates the temporal offsets tied to each 3D kernel coordinate, so neighboring receptive fields form continuously without repeatedly reloading shared input samples. The grating provides a differential group delay of 2691 picoseconds and a dispersion of 124.8 picoseconds per nanometer. At 20 gigabaud, spatial-spectral processing of the Indian Pines hyperspectral dataset reaches a coefficient of determination up to 0.997 and 97.9 percent classification accuracy, compared with 98.9 percent digitally, while at 10 gigabaud the same optical convolution layer achieves 92.5 percent accuracy on a four-class KTH video-recognition task. The results show low-redundancy streaming 3D convolution across both spectral and temporal data dimensions using one optical delay architecture.
