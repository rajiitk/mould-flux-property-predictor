# Mould Flux Property Predictor

A research-oriented web application for predicting viscosity behavior of multi-component mould fluxes used in continuous casting of steel.

## 🔬 Background
Mould flux properties strongly influence lubrication, heat transfer, and surface quality during continuous casting. 
This tool implements a modified Riboud–Urbain type viscosity model with industrial constraints to support flux design and screening.

## ⚙️ Models Implemented
- Basicity calculation (CaO/SiO₂)
- Modified Riboud–Urbain viscosity model
- Amphoteric Al₂O₃ correction
- Industrial viscosity lower bound (0.05 Pa·s)
- Viscosity–temperature (η–T) plotting:
  - Raw model viscosity
  - Industrial-corrected viscosity
  - Combined comparison

## 🧪 Inputs
- Oxide composition (wt%):
  - CaO, SiO₂, Al₂O₃
  - Na₂O, B₂O₃, Li₂O, MgO, CaF₂
- Temperature (K)

## 📊 Outputs
- Basicity (CaO/SiO₂)
- Al₂O₃/SiO₂ ratio
- Model viscosity (Pa·s)
- Industrial viscosity (Pa·s)
- Publication-quality η–T plots

## 🚀 How to Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
