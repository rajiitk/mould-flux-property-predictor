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
Open in browser:

http://127.0.0.1:5000

📌 Notes

Raw viscosity represents intrinsic melt behavior.

Industrial viscosity applies a lower bound to reflect operational constraints in continuous casting.

Raw and industrial viscosities are shown separately to preserve physical interpretation.

👤 Author

Raj Kamal Yadav
M.Tech – Materials Science & Engineering
Indian Institute of Technology Kanpur

📅 Version

v1.0 – M.Tech Thesis Work (2026)


### Save & exit
- `Ctrl + O` → Enter  
- `Ctrl + X`

### Commit & push
```bash
git add README.md
git commit -m "Add professional README"
git push

2️⃣ Add requirements.txt (REPRODUCIBILITY)

You may already have this, but confirm:

pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt for reproducibility"
git push

3️⃣ Add SCREENSHOTS (Highly Recommended)
Take screenshots

Web UI (inputs + results)

One viscosity plot

Save them as:

static/screenshot_ui.png
static/screenshot_plot.png

Allow screenshots to be tracked

Edit .gitignore:

nano .gitignore


Remove or comment this line:

static/*.png


Save (Ctrl+O, Enter, Ctrl+X).

Add screenshots to README

Edit README:

nano README.md


Add this section:

## 📷 Screenshots

### Application Interface
![UI](static/screenshot_ui.png)

### Viscosity–Temperature Plot
![Plot](static/screenshot_plot.png)

Commit & push
git add .
git commit -m "Add screenshots for documentation"
git push

4️⃣ Tag a VERSION (VERY PROFESSIONAL)
git tag v1.0
git push --tags


Now GitHub will show Release v1.0.

5️⃣ Add a CITATION file (RESEARCH-LEVEL)

Create:

nano CITATION.cff


Paste:

cff-version: 1.2.0
title: "Mould Flux Property Predictor"
message: "If you use this software, please cite it."
authors:
  - family-names: Yadav
    given-names: Raj Kamal
    affiliation: Indian Institute of Technology Kanpur
version: 1.0
date-released: 2026-01-02


Save & push:

git add CITATION.cff
git commit -m "Add citation file"
git push

6️⃣ Final Folder Structure (TARGET)

Your repo should now look like:

mould-flux-property-predictor/
├── app.py
├── models/
├── templates/
├── static/
│   ├── screenshot_ui.png
│   ├── screenshot_plot.png
├── requirements.txt
├── README.md
├── CITATION.cff
├── .gitignore
