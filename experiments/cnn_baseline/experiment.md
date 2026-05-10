# CNN Baseline Experiment

## Objective
Establish a non-graph baseline for landslide prediction using a Convolutional Neural Network.

This model ignores spatial graph structure and serves as a control for evaluating the benefit of graph-based modeling.

---

## Input Representation
Terrain data is represented as grid-based spatial raster images with channels:
- elevation
- slope
- rainfall
- soil moisture
- vegetation index

---

## Model
A standard CNN is used to learn spatial features without explicit graph structure.

---

## Hypothesis
The CNN will perform adequately in-region but degrade significantly under cross-region testing due to lack of structural inductive bias.

---

## Evaluation Plan
- Train on Region A (Himachal + Uttarakhand)
- Test on Region B (Kashmir)

Metrics:
- F1 Score
- Accuracy
- False Negative Rate
- Performance drop under distribution shift

---

## Purpose
This experiment establishes the baseline against which GNN and physics-constrained models will be compared.