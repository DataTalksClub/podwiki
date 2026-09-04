---
title: "Transfer Learning"
summary: "Reusing a pretrained convolutional network's learned features instead of training an image model from scratch."
related_course:
  - Docker
  - Git Worktrees
  - Gradient Boosting
  - Neural Networks
  - Serverless Deployment
  - Trading Strategy
---

Transfer learning is the module's answer to small datasets: take a large convolutional network pretrained on ImageNet, freeze its convolutional base, and train only a small classification head on your own images. The pretrained layers already encode useful visual features — edges, textures, shapes — so the head needs far fewer examples to converge.

The course applies this with Xception and similar architectures in Keras and PyTorch, and it is the standard technique in learner capstones: the published waste-classifier case study fine-tunes an Xception model to 93% test accuracy on roughly 15,000 images.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Module 8: Neural Networks and Deep Learning

## Related concepts

- [Neural Networks](/course-wiki/neural-networks/)
- [Serverless Deployment](/course-wiki/serverless-deployment/)
- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Docker](/course-wiki/docker/)
