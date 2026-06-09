# Shkrimi i Modeleve (Logjika Fizike)

# Ky kod përmban "trurin" e simulimit. Ne po krijojmë një automat qelizor ku rruga është një varg (array) dhe makinat lëvizin sipas rregullave lokale.
import numpy as np

class NaSchModel:
    def __init__(self, length, v_max, p):
        self.length = length  # Sa qeliza ka rruga
        self.v_max = v_max    # Shpejtësia maksimale
        self.p = p            # Probabiliteti i ngadalësimit rastësor
        self.road = np.full(length, -1) # -1 do të thotë qelizë e zbrazët

# Rregullat e Nagel-Schreckenberg
def step(self):
        new_road = np.full(self.length, -1)
        indices = np.where(self.road != -1)[0]
        
        for i in range(len(indices)):
            idx = indices[i]
            v = self.road[idx]
            
            # Gjetja e distancës me makinën para (Kushti Periodik)
            next_idx = indices[(i + 1) % len(indices)]
            distance = (next_idx - idx) % self.length
            
            # 1. Përshpejtimi: v -> v + 1
            if v < self.v_max: v += 1
            # 2. Frenimi: v -> distanca - 1
            if v >= distance: v = distance - 1
            # 3. Stokastika: ngadalësim me probabilitet p
            if v > 0 and np.random.random() < self.p: v -= 1
            
            # 4. Lëvizja: Pozicioni i ri
            new_road[(idx + v) % self.length] = v
            
        self.road = new_road
        return self.road



