from flask import Flask, render_template, request

from models.basicity import calculate_basicity
from models.viscosity import calculate_viscosity
from models.plotting import plot_viscosity_temperature

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        try:
            # -------- composition input --------
            composition = {
                "CaO": float(request.form["CaO"]),
                "SiO2": float(request.form["SiO2"]),
                "Al2O3": float(request.form["Al2O3"]),
                "Na2O": float(request.form["Na2O"]),
                "B2O3": float(request.form["B2O3"]),
                "Li2O": float(request.form["Li2O"]),
                "MgO": float(request.form["MgO"]),
                "CaF2": float(request.form["CaF2"]),
            }

            temperature = float(request.form["temp"])

            # -------- calculations --------
            basicity = calculate_basicity(
                composition["CaO"],
                composition["SiO2"]
            )

            alumina_ratio = composition["Al2O3"] / composition["SiO2"]

            viscosity_raw, viscosity = calculate_viscosity(
                composition,
                temperature
            )

            # -------- plotting --------
            plot_viscosity_temperature(composition)

            # -------- output (MERGED, nothing overwritten) --------
            result = {
                "basicity": round(basicity, 3),
                "alumina_ratio": round(alumina_ratio, 2),
                "viscosity_raw": round(viscosity_raw, 4),
                "viscosity": round(viscosity, 4)
            }

        except Exception as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
