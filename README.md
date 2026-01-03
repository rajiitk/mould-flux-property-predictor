# Mould Flux Property Predictor

A research-oriented web application for predicting viscosity behavior of multi-component mould fluxes used in the continuous casting of steel.  
The tool is designed to support **flux design, screening, and academic analysis** by combining semi-empirical viscosity models with industrial constraints.

---

## 🔬 Background and Motivation

In continuous casting, mould flux properties play a critical role in:

- Lubrication between the solidifying shell and mould
- Heat transfer control
- Surface quality and crack prevention

Viscosity is one of the most influential properties governing these functions.  
However, purely theoretical or semi-empirical models often underpredict viscosity under industrial conditions.

This project addresses this gap by:
- Implementing a modified Riboud–Urbain type viscosity model
- Explicitly separating **intrinsic (model) viscosity** from **industrial (operational) viscosity**
- Providing clear visualization of viscosity–temperature behavior

---

## ⚙️ Models Implemented

### 1. Basicity
- Basicity is calculated as:
  
  \[
  \text{Basicity} = \frac{\text{CaO}}{\text{SiO}_2}
  \]

- Used as a key structural parameter influencing melt depolymerization.

---

### 2. Viscosity Model (Physics-Based)

A modified Riboud–Urbain type relation is used:

\[
\ln(\eta) = A + \frac{B}{T}
\]

where:
- \( \eta \) is viscosity (Pa·s)
- \( T \) is temperature (K)
- \( A \) and \( B \) are composition-dependent coefficients

#### Composition effects included:
- CaO/SiO₂ (basicity)
- Amphoteric behavior of Al₂O₃
- Network-modifying effects of Na₂O, Li₂O, B₂O₃
- Viscosity-lowering effect of CaF₂

This gives the **raw model viscosity**, representing intrinsic melt behavior.

---

### 3. Industrial Viscosity Constraint

To reflect real continuous casting conditions, an industrial lower bound is imposed:

\[
\eta_{\text{industrial}} = \max(\eta_{\text{model}}, 0.05 \text{ Pa·s})
\]

This accounts for:
- Multiphase slag films
- Presence of crystallites
- Shear and radiation effects
- Practical operational limits

Both **model viscosity** and **industrial viscosity** are reported separately to preserve physical interpretation.

---

## 🧪 Inputs

The application accepts the following inputs:

### Oxide Composition (wt%)
- CaO
- SiO₂
- Al₂O₃
- Na₂O
- B₂O₃
- Li₂O
- MgO
- CaF₂

### Temperature
- Temperature in Kelvin (K)

---

## 📊 Outputs

The tool provides:

- Basicity (CaO/SiO₂)
- Al₂O₃/SiO₂ ratio
- Model viscosity (Pa·s)
- Industrial viscosity (Pa·s)
- Viscosity–temperature (η–T) plots:
  - Raw model viscosity
  - Industrial-corrected viscosity
  - Combined comparison plot

Plots are generated automatically and saved in publication-quality resolution.

---

## 📈 Visualization Strategy

To avoid masking physical trends:

- **Model viscosity** is used for:
  - Understanding intrinsic melt behavior
  - Temperature sensitivity analysis
  - Model calibration

- **Industrial viscosity** is used for:
  - Flux design decisions
  - Operational suitability assessment

Both curves are visualized separately and together for clarity.

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/rajiitk/mould-flux-property-predictor.git
cd mould-flux-property-predictor
