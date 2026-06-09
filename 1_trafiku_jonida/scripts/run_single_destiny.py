import sys
import os
# Shton folderin kryesor në sistem që Python të gjejë modulet tona
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.nasch import NaSchModel
from src.visualization.spacetime import save_spacetime
import numpy as np

# Në këtë rast po testojmë një dendësi mesatare ($\rho = 0.25$) ku pritet të shfaqen valët e para të trafikut.
def main():
    # Parametrat e simulimit të vetëm
    L = 100         # Gjatësia e rrugës (100 qeliza)
    T = 120         # Hapat kohorë (sa sekonda zgjat simulimi)
    v_max = 5       # Shpejtësia maksimale
    p = 0.2         # Probabiliteti i ngadalësimit
    density = 0.25  # Dendësia e makinave (25% e rrugës plot)

    # Krijojmë objektin e modelit
    model = NaSchModel(L, v_max, p)
    
    # Shpërndajmë makinat në rrugë
    num_cars = int(density * L)
    pos = np.random.choice(L, num_cars, replace=False)
    model.road[pos] = np.random.randint(0, v_max + 1, num_cars)
history = []
    
    for t in range(T):
        # Ruajmë gjendjen aktuale (1 nëse ka makinë, 0 nëse është bosh)
        current_state = np.where(model.road != -1, 1, 0)
        history.append(current_state)
        
        # Kalojmë në sekondën tjetër duke zbatuar rregullat NaSch
        model.step()
        # Kthejmë listën në një matricë NumPy
    history_matrix = np.array(history)
    
    # Ruajmë grafikun te folderi i rezultateve
    output_path = "results/figures/spacetime_density_025.png"
    save_spacetime(history_matrix, output_path)
    print(f"Simulimi u krye me sukses! Grafiku u ruajt te: {output_path}")

if __name__ == "__main__":
    main()
    
        
