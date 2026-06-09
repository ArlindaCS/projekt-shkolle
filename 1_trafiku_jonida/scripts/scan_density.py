# Ekzekutimi
# determinist (p=0)
# stokastik (p=0.2, 0.5)

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.nasch import NaSchModel
from src.analysis.traffic_metrics import calculate_flow
from src.visualization.spacetime import save_fundamental
import numpy as np

def run():
    L, v_max = 200, 5
    p_list = [0.0, 0.2, 0.5]
    rhos = np.linspace(0.05, 0.9, 20)
    
    results_flows = []
    for p in p_list:
        flows_for_p = []
        for rho in rhos:
            model = NaSchModel(L, v_max, p)
            # Inicializim i thjeshtë me densitet rho
            num_cars = int(rho * L)
            pos = np.random.choice(L, num_cars, replace=False)
            model.road[pos] = v_max
            
            # Burn-in 200 hapa, pastaj matja për 100 hapa
            for _ in range(200): model.step()
            f_sum = sum(calculate_flow(model.step()) for _ in range(100))
            flows_for_p.append(f_sum / 100)
        results_flows.append(flows_for_p)
        
    save_fundamental([rhos]*3, results_flows, p_list, "results/figures/fundamental.png")
    print("PROJEKTI U KRYE! Grafiku u ruajt te results/figures/fundamental.png")

if __name__ == "__main__":
    run()
