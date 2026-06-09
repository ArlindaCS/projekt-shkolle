Shkrimi i Modeleve (Logjika Fizike)

Ky kod përmban "trurin" e simulimit. Ne po krijojmë një automat qelizor ku rruga është një varg (array) dhe makinat lëvizin sipas rregullave lokale.
import numpy as np

class NaSchModel:
    def __init__(self, length, v_max, p):
        self.length = length  # Sa qeliza ka rruga
        self.v_max = v_max    # Shpejtësia maksimale
        self.p = p            # Probabiliteti i ngadalësimit rastësor
        self.road = np.full(length, -1) # -1 do të thotë qelizë e zbrazët
