# Project Plan

## 1. Research Question
Does physically motivated regularization improve cross-region generalization in graph-based landslide forecasting under geographic distribution shift?

---

## 2. Hypothesis
Physically motivated constraints reduce overfitting to region-specific terrain correlations and improve robustness under unseen geographic conditions.

---

## 3. Motivation
Landslide prediction models often fail outside their training regions due to reliance on location-specific spatial patterns rather than physically meaningful structure.

---

## 4. System Design

### Terrain Representation
- Nodes: terrain patches
- Edges: spatial + hydrological connectivity derived from elevation gradients

### Features
- elevation
- slope
- rainfall
- soil moisture
- vegetation
- historical landslides

---

## 5. Models

### Baselines
- CNN
- Vanilla GNN

### Proposed Model
- GNN + physically motivated regularization

---

## 6. Objective Function

\mathcal{L}_{total} = \mathcal{L}_{prediction} + \lambda \mathcal{L}_{constraint}

Where:
- L_prediction = prediction loss
- L_constraint = penalizes hydrologically inconsistent predictions

---

## 7. Geographic Split Strategy
- Train and test regions are geographically separated
- Prevents spatial leakage
- Ensures true distribution shift evaluation

---

## 8. Evaluation Metrics
- F1 score / accuracy
- False negatives
- Calibration error
- Cross-region performance drop

---

## 9. Ablation Studies
- Without graph structure
- Without constraint
- Full model

---

## 10. Failure Analysis
- Where constraints fail
- Where GNN fails
- Under what environmental conditions models degrade

---

## 11. Expected Contribution
A controlled experimental framework for studying physically motivated inductive bias under geographic distribution shift in geospatial machine learning.