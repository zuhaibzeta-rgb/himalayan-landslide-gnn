# Geographic Split Definition

## Purpose
This document defines the geographic partitioning strategy used to evaluate cross-region generalization in the landslide forecasting system.

The goal is to ensure that model evaluation reflects true distribution shift rather than spatial leakage.

---

## Train Regions
- Himachal Pradesh
- Uttarakhand

---

## Validation Region
- A held-out subregion of the central Himalayas (used for model tuning only)

---

## Test Region
- Kashmir (Jammu and Kashmir, India)

---

## Key Constraint
No spatial or geographic overlap is allowed between training and test regions.

All splits are constructed at the region level to ensure that the model is evaluated on unseen terrain distributions.

---

## Rationale
This split is designed to simulate real-world deployment conditions where models trained on one Himalayan region must generalize to completely unseen geographic terrain with different environmental and hydrological characteristics.