import numpy as np

class NaSchModel:
    def __init__(self, road_length=100, density=0.2, max_velocity=5, p_slow=0.3):
        """
        Inicializon modelin e trafikut Nagel-Schreckenberg.
        
        Parametrat:
        - road_length (int): Gjatësia e rrugës në qeliza (L)
        - density (float): Dendësia e makinave (rho), vlerat midis 0 dhe 1
        - max_velocity (int): Shpejtësia maksimale e lejuar (v_max)
        - p_slow (float): Probabiliteti i ngadalësimit stokastik (p)
        """
        self.L = road_length
        self.v_max = max_velocity
        self.p = p_slow
        self.N = int(density * road_length)
        
        # Rruga përfaqësohet nga një vektor ku -1 tregon qelizë të zbrazët,
        # ndërsa numrat >= 0 tregojnë shpejtësinë e makinës në atë qelizë.
        self.road = np.full(self.L, -1, dtype=int)
        
        # Shpërndarja e makinave në mënyrë të rastësishme pa mbivendosje
        if self.N > self.L:
            raise ValueError("Numri i makinave nuk mund të jetë më i madh se gjatësia e rrugës!")
            
        indices = np.random.choice(self.L, self.N, replace=False)
        for idx in indices:
            self.road[idx] = np.random.randint(0, self.v_max + 1)

    def _get_gap(self, pos, current_road):
        """Llogarit hapësirën (numrin e qelizave të zbrazëta) përpara makinës sime."""
        gap = 0
        for i in range(1, self.L):
            next_idx = (pos + i) % self.L
            if current_road[next_idx] != -1:
                return gap
            gap += 1
        return self.L - 1

    def step(self):
        """Ekzekuton një hap të plotë kohor duke zbatuar 4 rregullat sekuenciale."""
        current_road = self.road.copy()
        next_road = np.full(self.L, -1, dtype=int)
        
        for pos in range(self.L):
            v = current_road[pos]
            if v == -1:
                continue  # Qelizë e zbrazët, kalo te tjetra
                
            # Rregulla 1: Përshpejtimi shtues
            if v < self.v_max:
                v += 1
                
            # Rregulla 2: Frenimi i sigurisë (për të shmangur përplasjen)
            gap = self._get_gap(pos, current_road)
            if v > gap:
                v = gap
                
            # Rregulla 3: Ngadalësimi stokastik (psikologjia e shoferit ose vonesa)
            if v > 0 and np.random.rand() < self.p:
                v -= 1
                
            # Rregulla 4: Lëvizja fizike në rrjetë
            next_pos = (pos + v) % self.L
            next_road[next_pos] = v
            
        self.road = next_road
        return self.road.copy()

    def simulate(self, time_steps=100):
        """Simulon lëvizjen e trafikut për një numër të caktuar hapash kohorë."""
        history = np.zeros((time_steps, self.L), dtype=int)
        for t in range(time_steps):
            history[t, :] = self.step()
        return history
