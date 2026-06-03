import os
import sys
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.nasch import NaSchModel
from src.analysis.traffic_metrics import calculate_metrics
from src.visualization.spacetime import save_fundamental_diagram

os.makedirs('results/figures', exist_ok=True)
os.makedirs('results/tables', exist_ok=True)

# Gjenerojmë 25 pika të ndryshme dendësie nga 0.02 deri në 0.95
densities = np.linspace(0.02, 0.95, 25)
probabilities = [0.0, 0.2, 0.5]

results_flux = {}
table_data = []

for p in probabilities:
    fluxes = []
    for rho in densities:
        model = NaSchModel(road_length=200, density=rho, max_velocity=5, p_slow=p)
        # Simulojmë mjaftueshëm hapa që sistemi të stabilizohet
        history = model.simulate(time_steps=250)
        
        real_rho, avg_v, flux = calculate_metrics(history)
        fluxes.append(flux)
        
        # Ruajmë disa pika kyçe për tabelën tonë të raportit
        if p == 0.2 and round(rho, 2) in [0.1, 0.3, 0.7]:
            table_data.append((p, round(rho, 2), round(avg_v, 3), round(flux, 3)))
            
    results_flux[p] = fluxes

# Ruajmë diagramin fundamental
save_fundamental_diagram(densities, results_flux, "results/figures/fundamental_diagram.png")
print("Diagrami Fundamental u ruajt te 'results/figures/fundamental_diagram.png'")

# Ruajmë tabelën e metrikave në format teksti (Markdown/CSV)
with open("results/tables/metrics_summary.txt", "w") as f:
    f.write("| Probabiliteti (p) | Dendësia (rho) | Shpejtësia Mesatare (<v>) | Fluksi (J) |\n")
    f.write("|-------------------|----------------|---------------------------|------------|\n")
    for row in table_data:
        f.write(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |\n")
print("Tabela e metrikave u ruajt te 'results/tables/metrics_summary.txt'")
