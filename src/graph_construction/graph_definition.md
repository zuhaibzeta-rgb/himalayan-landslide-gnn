# Graph Construction Definition

## Purpose
This document defines how geographic terrain is converted into a graph structure for landslide forecasting.

---

## Nodes
Each node represents a terrain cell (grid-based spatial unit).

Each node contains features such as:
- elevation
- slope
- rainfall
- soil moisture
- vegetation index
- historical landslide occurrence

---

## Edges
Edges represent spatial and hydrological relationships between neighboring terrain cells.

Edges are constructed based on:
- geographic adjacency (4 or 8-neighborhood grid connectivity)
- elevation gradient directionality
- optional hydrological flow consistency

---

## Graph Type
The resulting structure is a weighted, directed/undirected spatial graph depending on terrain flow assumptions.

---

## Key Assumption
Nearby terrain cells exhibit correlated hydrological and geological behavior, but this correlation is not purely spatial and is influenced by elevation and slope structure.

---

## Purpose in Model
This graph structure enables the model to capture spatial dependencies that CNN-based approaches cannot explicitly represent.