import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os
from models.viscosity import calculate_viscosity


def plot_viscosity_temperature(composition):
    """
    Generates viscosity–temperature plots for mould flux:
    1) Combined plot (raw + industrial)
    2) Raw model viscosity (log scale)
    3) Industrial viscosity (linear scale)
    """

    temperatures = list(range(1300, 1701, 25))

    viscosities_raw = []
    viscosities_corrected = []

    for T in temperatures:
        eta_raw, eta_corr = calculate_viscosity(composition, T)

        # Safety: avoid None values in plotting
        viscosities_raw.append(eta_raw if eta_raw is not None else 1e-4)
        viscosities_corrected.append(eta_corr if eta_corr is not None else 0.05)

    os.makedirs("static", exist_ok=True)

    # -------------------------------------------------
    # 1️⃣ Combined plot: raw + industrial
    # -------------------------------------------------
    plt.figure()
    plt.plot(
        temperatures,
        viscosities_raw,
        'o--',
        label='Model viscosity (raw)'
    )
    plt.plot(
        temperatures,
        viscosities_corrected,
        'o-',
        label='Industrial viscosity'
    )
    plt.axhline(
        0.05,
        color='red',
        linestyle=':',
        label='Industrial lower bound'
    )

    plt.xlabel("Temperature (K)")
    plt.ylabel("Viscosity (Pa·s)")
    plt.title("Viscosity–Temperature Curve (Mould Flux)")
    plt.legend()
    plt.grid(True)
    plt.savefig("static/viscosity_combined.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # 2️⃣ Raw model viscosity (log scale – physics view)
    # -------------------------------------------------
    plt.figure()
    plt.plot(temperatures, viscosities_raw, 'o--', color='blue')
    plt.yscale("log")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Viscosity (Pa·s, log scale)")
    plt.title("Model Viscosity vs Temperature (Log Scale)")
    plt.grid(True, which="both")
    plt.savefig("static/viscosity_model_log.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # 3️⃣ Industrial viscosity (application view)
    # -------------------------------------------------
    plt.figure()
    plt.plot(temperatures, viscosities_corrected, 'o-', color='orange')
    plt.xlabel("Temperature (K)")
    plt.ylabel("Viscosity (Pa·s)")
    plt.title("Industrial Viscosity vs Temperature")
    plt.grid(True)
    plt.savefig("static/viscosity_industrial.png", dpi=300)
    plt.close()
