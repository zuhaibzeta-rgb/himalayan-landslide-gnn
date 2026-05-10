# Physically Motivated Graph Neural Networks for Cross-Region Landslide Forecasting

## Overview
Landslides are a major environmental hazard in mountainous regions such as Kashmir, where extreme rainfall variability, unstable terrain, and climate-driven hydrological changes increase risk.

Machine learning models often fail to generalize across unseen geographic regions due to distribution shift and overfitting to local terrain patterns.

This project investigates whether physically motivated inductive bias can improve cross-region generalization in graph-based landslide forecasting systems.

---

## Key Idea
- Terrain is modeled as a graph (nodes = terrain regions, edges = spatial/hydrological relationships)
- A Graph Neural Network is used for prediction
- A physically motivated regularization term enforces hydrological consistency
- Models are evaluated on unseen geographic regions

---

## Models Compared
- CNN baseline  
- Vanilla GNN  
- Physically regularized GNN  

---

## Evaluation Focus
- Cross-region generalization performance  
- Performance degradation under distribution shift  
- False negatives (critical for hazard prediction)  
- Calibration and robustness  

---

## Goal
To evaluate whether physically motivated inductive bias improves generalization in graph-based environmental machine learning systems under geographic distribution shift.

---

## Repository Structure
src/ – models, training, evaluation  
data/ – datasets and geographic splits  
experiments/ – baselines and runs  
configs/ – experiment settings  
results/ – outputs and metrics