Analiza (Llogaritja e Metrikave)
Këtu llogarisim fluksin, që është madhësia kryesore për Diagramin Fundamental.

import numpy as np

def calculate_flow(road):
    # Marrim vetëm makinat (aty ku vlera nuk është -1)
    speeds = road[road != -1]
    if len(speeds) == 0:
        return 0.0
    
    density = len(speeds) / len(road) # rho
    avg_v = np.mean(speeds)           # shpejtësia mesatare
    return density * avg_v            # J = rho * <v>
