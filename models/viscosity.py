import math

def calculate_viscosity(composition, temperature):
    """
    Modified Riboud / Urbain-type viscosity model
    for multi-component mould fluxes.

    Returns viscosity in Pa·s
    """

    # ---- mandatory components ----
    CaO   = composition.get("CaO", 0.0)
    SiO2  = composition.get("SiO2", 0.0)
    Al2O3 = composition.get("Al2O3", 0.0)

    # ---- optional modifiers ----
    Na2O = composition.get("Na2O", 0.0)
    B2O3 = composition.get("B2O3", 0.0)
    Li2O = composition.get("Li2O", 0.0)
    MgO  = composition.get("MgO", 0.0)
    CaF2 = composition.get("CaF2", 0.0)

    # ---- sanity checks ----
    if temperature <= 0 or SiO2 <= 0:
        return None

    # ---- ratios ----
    basicity = CaO / SiO2
    alumina_ratio = Al2O3 / SiO2

    # -------------------------------------------------
    # Riboud / Urbain-style composition-dependent terms
    # -------------------------------------------------

    # Pre-exponential term
    A = (
        -1.8
        + 0.6 * basicity
        + 0.03 * Al2O3
        - 0.02 * Na2O
        - 0.03 * B2O3
        - 0.02 * Li2O
    )

    # Amphoteric correction for Al2O3
    if alumina_ratio > 1.2:
        A -= 0.25 * (alumina_ratio - 1.2)

    # Activation-energy-like term
    B = (
        6000
        - 900 * basicity
        + 40 * Al2O3
        - 120 * (Na2O + Li2O)
        - 80 * B2O3
        - 60 * CaF2
    )

    # ---- viscosity calculation ----
    log_eta = A + (B / temperature)
    viscosity_raw = math.exp(log_eta) * 1e-3  # Pa·s (model prediction)

    # ---- industrial lower bound correction ----
    viscosity_corrected = max(viscosity_raw, 0.05)

    return round(viscosity_raw, 4), round(viscosity_corrected, 4)

