def calculate_basicity(cao, sio2):
    """
    Calculates basicity of mould flux
    Basicity = CaO / SiO2
    """
    if sio2 == 0:
        return None
    return round(cao / sio2, 3)
